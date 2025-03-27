import re
from antlr4 import *
from APAGNANGAGEParser import APAGNANGAGEParser as Parser
from APAGNANGAGEVisitor import APAGNANGAGEVisitor

import errors

def convert_int(int_repr: str) -> int:
    sp = re.split("(AP|AGN|AN)", int_repr)
    i = 0
    for k, slice in enumerate(sp):
        i += len(slice) * 10**(len(sp) - k - 1)
    return i


class VariableScope:
    def __init__(self, **kwargs):
        self.vars = {**kwargs}
        
    def varExist(self, varname):
        return varname in self.vars
    
    def get(self, varname):
        return self.vars[varname]
    
    def get_check(self, varname):
        # vérifie si la variable existe et la renvoie, sinon lance une erreur
        if varname not in self.vars:
            errors.error(f"la variable {varname} n'existe pas")
        return self.get(varname)
    
    def set(self, varname, value):
        self.vars[varname] = value

class Visitor(APAGNANGAGEVisitor):
    def __init__(self):
        super().__init__()
        self.scopes = {
            "main" : VariableScope(),
            "pignouf" : VariableScope(A = 1)}
        self.current = "main"
    
    # Visit a parse tree produced by Parser#program.
    def visitProgram(self, ctx:Parser.ProgramContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Parser#statement.
    def visitStatement(self, ctx:Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#assignment.
    def visitAssignment(self, ctx:Parser.AssignmentContext):
        varname = str(ctx.ID())
        value = self.visitExpression(ctx.expression())
        self.scopes[self.current].set(varname, value)

    # Visit a parse tree produced by Parser#expression.
    def visitExpression(self, ctx:Parser.ExpressionContext):
        operators = []
        values = []
        # On sépare les valeurs et les 
        for exp in ctx.children:
            match exp:
                case Parser.OperatorContext():
                    operators.append(exp.getText())
                case Parser.Function_callContext():
                    values.append(exp.getText())
                case Parser.Expression_intContext():
                    values.append(convert_int(exp.getText()))
                case _: # C'est un identifiant
                    varname = str(exp.getText())
                    val = self.scopes[self.current].get_check(varname)
                    values.append(val)
                    
        aggregate = values[0]
        
        # Une petite erreur bien explicite pour dire qu'il faut n opérateurs et n+1 opérandes
        if len(operators) != len(values) - 1:
            en_trop = values[len(operators) : -1] if len(operators) < len(values) - 1 else operators[len(values) - 1: -1]
            errors.error(f"Il n'y pas assez d'opérateurs ou d'opérandes pour effectuer le calcul : il y a en trop {en_trop}")
        
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
            elif re.match(r"c\w*'\w*est", op): # WTF NILS !!!!!!!!!!!!!!!!!
                aggregate = aggregate == val
        return aggregate


    # Visit a parse tree produced by Parser#function_call.
    def visitFunction_call(self, ctx:Parser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#print.
    def visitPrint(self, ctx:Parser.PrintContext):
        exp = self.visitExpression(ctx.expression())
        print(exp)

    # Visit a parse tree produced by Parser#print_assign_string.
    def visitPrint_assign_string(self, ctx:Parser.Print_assign_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#loop.
    def visitLoop(self, ctx:Parser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#logic.
    def visitLogic(self, ctx:Parser.LogicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#if.
    def visitIf(self, ctx:Parser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#block.
    def visitBlock(self, ctx:Parser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#increment.
    def visitIncrement(self, ctx:Parser.IncrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#function_def.
    def visitFunction_def(self, ctx:Parser.Function_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#return.
    def visitReturn(self, ctx:Parser.ReturnContext):
        return self.visitChildren(ctx)