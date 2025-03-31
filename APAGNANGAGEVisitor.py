# Generated from APAGNANGAGE.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .APAGNANGAGEParser import APAGNANGAGEParser
else:
    from APAGNANGAGEParser import APAGNANGAGEParser

# This class defines a complete generic visitor for a parse tree produced by APAGNANGAGEParser.

class APAGNANGAGEVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by APAGNANGAGEParser#program.
    def visitProgram(self, ctx:APAGNANGAGEParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by APAGNANGAGEParser#statement.
    def visitStatement(self, ctx:APAGNANGAGEParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by APAGNANGAGEParser#assignment.
    def visitAssignment(self, ctx:APAGNANGAGEParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by APAGNANGAGEParser#assign_string.
    def visitAssign_string(self, ctx:APAGNANGAGEParser.Assign_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by APAGNANGAGEParser#expression_int.
    def visitExpression_int(self, ctx:APAGNANGAGEParser.Expression_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by APAGNANGAGEParser#operator.
    def visitOperator(self, ctx:APAGNANGAGEParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by APAGNANGAGEParser#expression.
    def visitExpression(self, ctx:APAGNANGAGEParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by APAGNANGAGEParser#function_call.
    def visitFunction_call(self, ctx:APAGNANGAGEParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by APAGNANGAGEParser#print.
    def visitPrint(self, ctx:APAGNANGAGEParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by APAGNANGAGEParser#input_assign_string.
    def visitInput_assign_string(self, ctx:APAGNANGAGEParser.Input_assign_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by APAGNANGAGEParser#loop_counter.
    def visitLoop_counter(self, ctx:APAGNANGAGEParser.Loop_counterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by APAGNANGAGEParser#loop.
    def visitLoop(self, ctx:APAGNANGAGEParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by APAGNANGAGEParser#if.
    def visitIf(self, ctx:APAGNANGAGEParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by APAGNANGAGEParser#block.
    def visitBlock(self, ctx:APAGNANGAGEParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by APAGNANGAGEParser#increment.
    def visitIncrement(self, ctx:APAGNANGAGEParser.IncrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by APAGNANGAGEParser#function_def.
    def visitFunction_def(self, ctx:APAGNANGAGEParser.Function_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by APAGNANGAGEParser#return.
    def visitReturn(self, ctx:APAGNANGAGEParser.ReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by APAGNANGAGEParser#list_def.
    def visitList_def(self, ctx:APAGNANGAGEParser.List_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by APAGNANGAGEParser#list_append.
    def visitList_append(self, ctx:APAGNANGAGEParser.List_appendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by APAGNANGAGEParser#list_pop_or_get.
    def visitList_pop_or_get(self, ctx:APAGNANGAGEParser.List_pop_or_getContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by APAGNANGAGEParser#import_statement.
    def visitImport_statement(self, ctx:APAGNANGAGEParser.Import_statementContext):
        return self.visitChildren(ctx)



del APAGNANGAGEParser