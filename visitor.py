import re
from antlr4 import *
from antlr4.tree.Tree import TerminalNodeImpl

from APAGNANGAGEParser import APAGNANGAGEParser as Parser, APAGNANGAGEParser
from APAGNANGAGEVisitor import APAGNANGAGEVisitor

import errors
from special_return import *


def convert_int(int_repr: str) -> int:
    sp = re.split("(P|GN|N)", int_repr)[::2]
    n = 0
    for k, slice in enumerate(reversed(sp)):
        n += len(slice) * (10 ** k)
    return n


class VariableScope:
    def __init__(self, parent, **kwargs):
        self.vars = {**kwargs}
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
        errors.error(f"La variable {varname} n'existe pas")

    def set(self, varname, value):
        self.vars[varname] = value


class Visitor(APAGNANGAGEVisitor):
    def __init__(self):
        super().__init__()

        # Le principe est le suivant, chaque corps de fonction
        # est stockée dans functions (associé au nom de la fonction)

        # À chaque fois qu'il y a un nouvel appel (de fonction, et tout)
        # on le rajoute sur la pile d'appel, ainsi que l'instance de la table de variable associée

        main_var_scope = VariableScope(None)
        self.current = "main"
        self.call_stack = [("main", main_var_scope)]
        self.functions: dict[str, Parser.StatementContext] = {}

    # Visit a parse tree produced by Parser#program.
    def visitProgram(self, ctx: Parser.ProgramContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Parser#statement.
    def visitStatement(self, ctx: Parser.StatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Parser#assignment.
    def visitAssignment(self, ctx: Parser.AssignmentContext):
        varname = str(ctx.ID())
        value = self.visitExpression(ctx.expression())
        self.call_stack[-1][1].set(varname, value)

    # Visit a parse tree produced by Parser#expression.
    def visitExpression(self, ctx: Parser.ExpressionContext):
        operators = []
        values = []
        # On sépare les valeurs et les 
        for exp in ctx.children:
            match exp:
                case Parser.OperatorContext():
                    operators.append(exp.getText())
                case Parser.Function_callContext():
                    values.append(self.visitFunction_call(exp))
                case Parser.Expression_intContext():
                    values.append(convert_int(exp.getText()))
                case _:  # C'est un identifiant
                    varname = str(exp.getText())
                    val = self.call_stack[-1][1].get_check(varname)
                    values.append(val)

        aggregate = values[0]

        # Une petite erreur bien explicite pour dire qu'il faut n opérateurs et n+1 opérandes
        if len(operators) != len(values) - 1:
            en_trop = values[len(operators): -1] if len(operators) < len(values) - 1 else operators[
                                                                                          len(values) - 1: -1]
            errors.error(
                f"Il n'y pas assez d'opérateurs ou d'opérandes pour effectuer le calcul : il y a en trop {en_trop}")

        # Pour le moment on se moque de l'ordre des opérations, on traites tous les opérateurs dans l'ordre
        for i in range(len(operators)):
            op = operators[i]
            val = values[i + 1]
            if op == '+':
                aggregate += val
            elif op == '-':
                aggregate -= val
            elif op == '*':
                aggregate *= val
            elif op == '/':
                aggregate /= val
            elif re.match(r"C\s*'\s*EST", op):  # WTF NILS !!!!!!!!!!!!!!!!!
                aggregate = aggregate == val
        return aggregate

    # Visit a parse tree produced by Parser#function_call.
    def visitFunction_call(self, ctx: Parser.Function_callContext):
        name = str(ctx.ID())
        if name not in self.functions:
            errors.error(f"fonction {name} inconnue")
        self.current = name
        vars = VariableScope(self.call_stack[-1][1])  # On duplique
        self.call_stack.append((name, vars))
        for statement in self.functions[name]:
            ret = self.visitStatement(statement)
            match ret:
                case Return(value):
                    self.call_stack.pop()
                    return value
                case Break():
                    errors.error("Break en dehors d'une boucle")
                case _:
                    continue

        self.call_stack.pop()
        return

        # Visit a parse tree produced by Parser#print.

    def visitPrint(self, ctx: Parser.PrintContext):
        exp = self.visitExpression(ctx.expression())
        print(exp)

    # Visit a parse tree produced by Parser#print_assign_string.
    def visitPrint_assign_string(self, ctx: Parser.Print_assign_stringContext):
        name = str(ctx.ID())
        content = ctx.STRING_ASSIGN()
        content: str = re.findall(r"TU\s*FAIS\s*UN\s*(.*)", str(content))[0]
        content = content.removesuffix("DANS")
        content = content.strip()
        self.call_stack[-1][1].set(name, content)

    def visitLoop_counter(self, ctx: APAGNANGAGEParser.Loop_counterContext):
        id: TerminalNodeImpl = ctx.ID()
        if id is not None:
            id = id.getText()
            count = self.call_stack[-1][1].get_check(id)
            if not isinstance(count, int):
                errors.error(
                    "Le max du compteur doit être de type int (on et pas dans python avec dé sale itérateur)")
            return count
        return len(ctx.LOOP_COUNTER())

    # Visit a parse tree produced by Parser#loop.
    def visitLoop(self, ctx: Parser.LoopContext):
        idx_name = ctx.ID()
        count = self.visitLoop_counter(ctx.loop_counter())
        if idx_name is not None:
            idx_name = idx_name.getText()
            for i in range(count):
                self.call_stack[-1][1].set(idx_name, i)
                self.visitBlock(ctx.block())
        else:
            for _ in range(count):
                self.visitBlock(ctx.block())

    # Visit a parse tree produced by Parser#logic.
    def visitLogic(self, ctx: Parser.LogicContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Parser#if.
    def visitIf(self, ctx: Parser.IfContext):
        logic = self.visitExpression(ctx.expression())
        if logic:
            return self.visitBlock(ctx.block())

    # Visit a parse tree produced by Parser#block.
    def visitBlock(self, ctx: Parser.BlockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Parser#increment.
    def visitIncrement(self, ctx: Parser.IncrementContext):
        return self.visitChildren(ctx)

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
