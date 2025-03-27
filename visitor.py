from antlr4 import *
from APAGNANGAGEParser import APAGNANGAGEParser as Parser
from APAGNANGAGEVisitor import APAGNANGAGEVisitor

def convert_int(int_repr: str) -> int:
    sp = int_repr.split("")


class VariableScope:
    def __init__(self, **kwargs):
        self.vars = {**kwargs}

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
        varname = ctx.ID()
        value = self.visitExpression(ctx.expression())


    # Visit a parse tree produced by Parser#expression.
    def visitExpression(self, ctx:Parser.ExpressionContext):
        operators = []
        values = []
        for exp in ctx.children:
            match exp:
                case Parser.OperatorContext():
                    operators.append(exp.getText())
                case Parser.Function_callContext():
                    values.append(exp.getText())
                case Parser.Expression_intContext():
                    values.append(exp.getText())
        print(operators)
        aggregate = 0
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#function_call.
    def visitFunction_call(self, ctx:Parser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#print.
    def visitPrint(self, ctx:Parser.PrintContext):
        return self.visitChildren(ctx)


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