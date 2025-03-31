# Generated from APAGNANGAGE.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .APAGNANGAGEParser import APAGNANGAGEParser
else:
    from APAGNANGAGEParser import APAGNANGAGEParser

# This class defines a complete listener for a parse tree produced by APAGNANGAGEParser.
class APAGNANGAGEListener(ParseTreeListener):

    # Enter a parse tree produced by APAGNANGAGEParser#program.
    def enterProgram(self, ctx:APAGNANGAGEParser.ProgramContext):
        pass

    # Exit a parse tree produced by APAGNANGAGEParser#program.
    def exitProgram(self, ctx:APAGNANGAGEParser.ProgramContext):
        pass


    # Enter a parse tree produced by APAGNANGAGEParser#statement.
    def enterStatement(self, ctx:APAGNANGAGEParser.StatementContext):
        pass

    # Exit a parse tree produced by APAGNANGAGEParser#statement.
    def exitStatement(self, ctx:APAGNANGAGEParser.StatementContext):
        pass


    # Enter a parse tree produced by APAGNANGAGEParser#assignment.
    def enterAssignment(self, ctx:APAGNANGAGEParser.AssignmentContext):
        pass

    # Exit a parse tree produced by APAGNANGAGEParser#assignment.
    def exitAssignment(self, ctx:APAGNANGAGEParser.AssignmentContext):
        pass


    # Enter a parse tree produced by APAGNANGAGEParser#assign_string.
    def enterAssign_string(self, ctx:APAGNANGAGEParser.Assign_stringContext):
        pass

    # Exit a parse tree produced by APAGNANGAGEParser#assign_string.
    def exitAssign_string(self, ctx:APAGNANGAGEParser.Assign_stringContext):
        pass


    # Enter a parse tree produced by APAGNANGAGEParser#expression_int.
    def enterExpression_int(self, ctx:APAGNANGAGEParser.Expression_intContext):
        pass

    # Exit a parse tree produced by APAGNANGAGEParser#expression_int.
    def exitExpression_int(self, ctx:APAGNANGAGEParser.Expression_intContext):
        pass


    # Enter a parse tree produced by APAGNANGAGEParser#operator.
    def enterOperator(self, ctx:APAGNANGAGEParser.OperatorContext):
        pass

    # Exit a parse tree produced by APAGNANGAGEParser#operator.
    def exitOperator(self, ctx:APAGNANGAGEParser.OperatorContext):
        pass


    # Enter a parse tree produced by APAGNANGAGEParser#expression.
    def enterExpression(self, ctx:APAGNANGAGEParser.ExpressionContext):
        pass

    # Exit a parse tree produced by APAGNANGAGEParser#expression.
    def exitExpression(self, ctx:APAGNANGAGEParser.ExpressionContext):
        pass


    # Enter a parse tree produced by APAGNANGAGEParser#function_call.
    def enterFunction_call(self, ctx:APAGNANGAGEParser.Function_callContext):
        pass

    # Exit a parse tree produced by APAGNANGAGEParser#function_call.
    def exitFunction_call(self, ctx:APAGNANGAGEParser.Function_callContext):
        pass


    # Enter a parse tree produced by APAGNANGAGEParser#print.
    def enterPrint(self, ctx:APAGNANGAGEParser.PrintContext):
        pass

    # Exit a parse tree produced by APAGNANGAGEParser#print.
    def exitPrint(self, ctx:APAGNANGAGEParser.PrintContext):
        pass


    # Enter a parse tree produced by APAGNANGAGEParser#input_assign_string.
    def enterInput_assign_string(self, ctx:APAGNANGAGEParser.Input_assign_stringContext):
        pass

    # Exit a parse tree produced by APAGNANGAGEParser#input_assign_string.
    def exitInput_assign_string(self, ctx:APAGNANGAGEParser.Input_assign_stringContext):
        pass


    # Enter a parse tree produced by APAGNANGAGEParser#loop_counter.
    def enterLoop_counter(self, ctx:APAGNANGAGEParser.Loop_counterContext):
        pass

    # Exit a parse tree produced by APAGNANGAGEParser#loop_counter.
    def exitLoop_counter(self, ctx:APAGNANGAGEParser.Loop_counterContext):
        pass


    # Enter a parse tree produced by APAGNANGAGEParser#loop.
    def enterLoop(self, ctx:APAGNANGAGEParser.LoopContext):
        pass

    # Exit a parse tree produced by APAGNANGAGEParser#loop.
    def exitLoop(self, ctx:APAGNANGAGEParser.LoopContext):
        pass


    # Enter a parse tree produced by APAGNANGAGEParser#if.
    def enterIf(self, ctx:APAGNANGAGEParser.IfContext):
        pass

    # Exit a parse tree produced by APAGNANGAGEParser#if.
    def exitIf(self, ctx:APAGNANGAGEParser.IfContext):
        pass


    # Enter a parse tree produced by APAGNANGAGEParser#block.
    def enterBlock(self, ctx:APAGNANGAGEParser.BlockContext):
        pass

    # Exit a parse tree produced by APAGNANGAGEParser#block.
    def exitBlock(self, ctx:APAGNANGAGEParser.BlockContext):
        pass


    # Enter a parse tree produced by APAGNANGAGEParser#increment.
    def enterIncrement(self, ctx:APAGNANGAGEParser.IncrementContext):
        pass

    # Exit a parse tree produced by APAGNANGAGEParser#increment.
    def exitIncrement(self, ctx:APAGNANGAGEParser.IncrementContext):
        pass


    # Enter a parse tree produced by APAGNANGAGEParser#function_def.
    def enterFunction_def(self, ctx:APAGNANGAGEParser.Function_defContext):
        pass

    # Exit a parse tree produced by APAGNANGAGEParser#function_def.
    def exitFunction_def(self, ctx:APAGNANGAGEParser.Function_defContext):
        pass


    # Enter a parse tree produced by APAGNANGAGEParser#return.
    def enterReturn(self, ctx:APAGNANGAGEParser.ReturnContext):
        pass

    # Exit a parse tree produced by APAGNANGAGEParser#return.
    def exitReturn(self, ctx:APAGNANGAGEParser.ReturnContext):
        pass


    # Enter a parse tree produced by APAGNANGAGEParser#list_def.
    def enterList_def(self, ctx:APAGNANGAGEParser.List_defContext):
        pass

    # Exit a parse tree produced by APAGNANGAGEParser#list_def.
    def exitList_def(self, ctx:APAGNANGAGEParser.List_defContext):
        pass


    # Enter a parse tree produced by APAGNANGAGEParser#list_append.
    def enterList_append(self, ctx:APAGNANGAGEParser.List_appendContext):
        pass

    # Exit a parse tree produced by APAGNANGAGEParser#list_append.
    def exitList_append(self, ctx:APAGNANGAGEParser.List_appendContext):
        pass


    # Enter a parse tree produced by APAGNANGAGEParser#list_pop_or_get.
    def enterList_pop_or_get(self, ctx:APAGNANGAGEParser.List_pop_or_getContext):
        pass

    # Exit a parse tree produced by APAGNANGAGEParser#list_pop_or_get.
    def exitList_pop_or_get(self, ctx:APAGNANGAGEParser.List_pop_or_getContext):
        pass


    # Enter a parse tree produced by APAGNANGAGEParser#import_statement.
    def enterImport_statement(self, ctx:APAGNANGAGEParser.Import_statementContext):
        pass

    # Exit a parse tree produced by APAGNANGAGEParser#import_statement.
    def exitImport_statement(self, ctx:APAGNANGAGEParser.Import_statementContext):
        pass



del APAGNANGAGEParser