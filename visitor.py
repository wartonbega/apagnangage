import itertools
import re
from locale import format_string
from logging.config import listen

from antlr4 import *
from antlr4.tree.Tree import TerminalNodeImpl

from APAGNANGAGEParser import APAGNANGAGEParser as Parser, APAGNANGAGEParser
from APAGNANGAGEVisitor import APAGNANGAGEVisitor

import errors
import securities
from special_return import *


class VariableScope:
    def __init__(self, parent, outstream, **kwargs):
        self.vars = {**kwargs}
        self.outstream = outstream
        self.parent: VariableScope = parent

    def varExist(self, varname):
        if varname in self.vars:
            return True
        if self.parent and self.parent.varExist(varname):
            return True
        return False

    def get(self, varname):
        return self.vars[varname]

    def get_check(self, varname):
        # vérifie si la variable existe et la renvoie, sinon lance une erreur
        if varname in self.vars:
            return self.vars[varname]
        if self.parent is not None and self.parent.varExist(varname):
            return self.parent.get(varname)
        errors.error(f"La variable {varname} n'existe pas", self.outstream)

    def set(self, varname, value):
        self.vars[varname] = value


class Visitor(APAGNANGAGEVisitor):
    def __init__(self, outstream: securities.OutputStream):
        super().__init__()

        # Le principe est le suivant, chaque corps de fonction
        # est stockée dans functions (associé au nom de la fonction)

        # À chaque fois qu'il y a un nouvel appel (de fonction, et tout)
        # on le rajoute sur la pile d'appel, ainsi que l'instance de la table de variable associée

        main_var_scope = VariableScope(None, outstream)
        self.current = "main"
        self.call_stack = [("main", main_var_scope)]
        self.functions: dict[str, Parser.StatementContext] = {}

        # Un stream de caractère de sortie
        self.outstream = outstream

    # Visit a parse tree produced by Parser#program.
    def visitProgram(self, ctx: Parser.ProgramContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Parser#statement.
    def visitStatement(self, ctx: Parser.StatementContext):
        if ctx.BREAK():
            return Break()
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Parser#assignment.
    def visitAssignment(self, ctx: Parser.AssignmentContext):
        if ctx.assign_string():
            self.visitAssign_string(ctx.assign_string())
        else:
            varname = ctx.ID().getText()
            value = self.visitExpression(ctx.expression())
            self.call_stack[-1][1].set(varname, value)

    def visitAssign_string(self, ctx: Parser.Assign_stringContext, do_assign=True):
        varname = ctx.ID().getText()
        content: str = self.format_string(
            re.match(r"^TU\s*FAIS\s*UN\s?(.*?)\s?DANS$", ctx.STRING_ASSIGN().getText())[1]
        )
        if do_assign:
            self.call_stack[-1][1].set(varname, content)
            return content
        else:
            return content, varname

    def visitExpression_int(self, ctx: Parser.Expression_intContext):
        return len(ctx.INT().getText())

    # Visit a parse tree produced by Parser#expression.
    def visitExpression(self, ctx: Parser.ExpressionContext):
        operators = []
        values = []
        # On sépare les valeurs et les 
        for exp in ctx.children:
            match exp:
                case Parser.OperatorContext():
                    operators.append(exp.getChild(0).getSymbol())
                case TerminalNode():  # C'est un identifiant
                    varname = str(exp.getText())
                    val = self.call_stack[-1][1].get_check(varname)
                    values.append(val)
                case _:
                    values.append(self.visit(exp))

        aggregate = values[0]

        # Une petite erreur bien explicite pour dire qu'il faut n opérateurs et n+1 opérandes
        if len(operators) != len(values) - 1:
            en_trop = values[len(operators): -1] if len(operators) < len(values) - 1 else operators[
                                                                                          len(values) - 1: -1]
            errors.error(
                f"Il n'y pas assez d'opérateurs ou d'opérandes pour effectuer le calcul : il y a en trop {en_trop}",
                self.outstream
            )

        # Pour le moment on se moque de l'ordre des opérations, on traite tous les opérateurs dans l'ordre
        for i, op in enumerate(operators):
            val = values[i + 1]
            match op.type:
                case APAGNANGAGEParser.PLUS:
                    aggregate += val
                case APAGNANGAGEParser.MINUS:
                    aggregate -= val
                case APAGNANGAGEParser.MULTIPLY:
                    aggregate *= val
                case APAGNANGAGEParser.DIVIDE:
                    aggregate /= val
                case APAGNANGAGEParser.EQUALS:
                    aggregate = str(aggregate) == str(val)  # equals à la javascript
                case _:
                    errors.error(f"Opérateur {op.text} non supporté", self.outstream)

        return aggregate

    # Visit a parse tree produced by Parser#function_call.
    def visitFunction_call(self, ctx: Parser.Function_callContext):
        name = str(ctx.ID())
        if name not in self.functions:
            errors.error(f"fonction {name} inconnue", self.outstream)
        self.current = name
        vars = VariableScope(self.call_stack[-1][1], self.outstream)  # On duplique
        self.call_stack.append((name, vars))
        for statement in self.functions[name]:
            ret = self.visitStatement(statement)
            match ret:
                case Return(value):
                    self.call_stack.pop()
                    return value
                case Break():
                    errors.error("Break en dehors d'une boucle", self.outstream)
                case _:
                    continue

        self.call_stack.pop()
        return

    def format_string(self, string: str):
        return re.sub(
            r":((?:AP|AGN|AN)+)",
            lambda match: str(self.call_stack[-1][1].get_check(match[1])),
            string
        )

    def visitPrint(self, ctx: Parser.PrintContext):
        exp = ctx.expression()
        assign_string = ctx.assign_string()
        if exp is not None:
            content = self.visitExpression(exp)
        elif assign_string is not None:
            content = self.visitAssign_string(assign_string)
        else:  # STRING_LINE
            content = self.format_string(
                re.match(r"^TU\s*FAIS\s*UN\s?(.*)$", ctx.STRING_LINE().getText())[1])
        self.outstream.write(content)
        return content

    def visitInput_assign_string(self, ctx: Parser.Input_assign_stringContext):
        name = str(ctx.ID())
        content = ctx.STRING_INPUT()
        content: str = self.format_string(re.match(r"^EH\s*!(.*?)\s?DANS$", str(content))[1])
        res = input(content)
        self.outstream.write(f"{content}{res}")
        self.call_stack[-1][1].set(name, res)

    def visitLoop_counter(self, ctx: Parser.Loop_counterContext):
        id = ctx.ID()
        if id is not None:
            id = id.getText()
            count = self.call_stack[-1][1].get_check(id)
            if not isinstance(count, int):
                errors.error(
                    "Le max du compteur doit être de type int (on et pas dans python avec dé sale itérateur)",
                    self.outstream)
            return count
        count = len(ctx.LOOP_COUNTER())
        if count == 0:
            return None
        return count

    # Visit a parse tree produced by Parser#loop.
    def visitLoop(self, ctx: Parser.LoopContext):
        idx_name = ctx.ID()
        count = self.visitLoop_counter(ctx.loop_counter())
        for i in range(count) if count is not None else itertools.count():
            if idx_name is not None:
                name = idx_name.getText()
                self.call_stack[-1][1].set(name, i)
            ret = self.visitBlock(ctx.block())
            match ret:
                case Break():
                    break
                case Return(val):
                    return Return(val)

    # Visit a parse tree produced by Parser#if.
    def visitIf(self, ctx: Parser.IfContext):
        logic = self.visitExpression(ctx.expression())
        if logic:
            return self.visitBlock(ctx.block())

    # Visit a parse tree produced by Parser#block.
    def visitBlock(self, ctx: Parser.BlockContext):
        for c in ctx.statement():
            ret = self.visitStatement(c)
            match ret:
                case Return(val):
                    return Return(val)
                case Break():
                    return Break()

    # Visit a parse tree produced by Parser#function_def.
    def visitFunction_def(self, ctx: Parser.Function_defContext):
        # On ne visite pas le corps de la fonction
        # On se contente de stocker les statements dans 
        # functions sous le nom de la fonction
        name = str(ctx.ID())
        block = ctx.statement()
        self.functions[name] = block

    # Visit a parse tree produced by Parser#return.
    def visitReturn(self, ctx: Parser.ReturnContext):
        return Return(self.visitExpression(ctx.expression()))

    def visitList_def(self, ctx: Parser.List_defContext):
        self.call_stack[-1][1].set(ctx.ID().getText(), [])

    def visitList_append(self, ctx: Parser.List_appendContext):
        if ctx.assign_string():
            content, list_name = self.visitAssign_string(ctx.assign_string(), False)
        else:
            list_name = ctx.ID().getText()
            content = None
        list_ = self.call_stack[-1][1].get_check(list_name)
        if not isinstance(list_, list):
            errors.error(f"{list_name} n'est pas une liste, on ne peut rien y ajouter",
                         self.outstream)
        if ctx.expression():
            content = self.visitExpression(ctx.expression())
        # else: content already assigned
        list_.append(content)

    def visitList_pop_or_get(self, ctx: Parser.List_pop_or_getContext):
        list_name = ctx.ID(0).getText()
        list_ = self.call_stack[-1][1].get_check(list_name)
        if not isinstance(list_, list):
            errors.error(f"{list_name} n'est pas une liste, on ne peut rien y ajouter",
                         self.outstream)
        expression = ctx.expression()
        index = self.visitExpression(expression) if expression else -1
        if ctx.LIST():
            val = list_[index]
        else:
            val = list_.pop(index)
        id1 = ctx.ID(1)
        if id1 is not None:
            self.call_stack[-1][1].set(id1.getText(), val)
        return val
