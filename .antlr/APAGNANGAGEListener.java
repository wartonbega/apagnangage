// Generated from /Users/antonappel/Desktop/Code/apagnangage/APAGNANGAGE.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link APAGNANGAGEParser}.
 */
public interface APAGNANGAGEListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link APAGNANGAGEParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(APAGNANGAGEParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link APAGNANGAGEParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(APAGNANGAGEParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link APAGNANGAGEParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(APAGNANGAGEParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link APAGNANGAGEParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(APAGNANGAGEParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link APAGNANGAGEParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(APAGNANGAGEParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link APAGNANGAGEParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(APAGNANGAGEParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link APAGNANGAGEParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(APAGNANGAGEParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link APAGNANGAGEParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(APAGNANGAGEParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link APAGNANGAGEParser#math}.
	 * @param ctx the parse tree
	 */
	void enterMath(APAGNANGAGEParser.MathContext ctx);
	/**
	 * Exit a parse tree produced by {@link APAGNANGAGEParser#math}.
	 * @param ctx the parse tree
	 */
	void exitMath(APAGNANGAGEParser.MathContext ctx);
	/**
	 * Enter a parse tree produced by {@link APAGNANGAGEParser#function_call}.
	 * @param ctx the parse tree
	 */
	void enterFunction_call(APAGNANGAGEParser.Function_callContext ctx);
	/**
	 * Exit a parse tree produced by {@link APAGNANGAGEParser#function_call}.
	 * @param ctx the parse tree
	 */
	void exitFunction_call(APAGNANGAGEParser.Function_callContext ctx);
	/**
	 * Enter a parse tree produced by {@link APAGNANGAGEParser#print}.
	 * @param ctx the parse tree
	 */
	void enterPrint(APAGNANGAGEParser.PrintContext ctx);
	/**
	 * Exit a parse tree produced by {@link APAGNANGAGEParser#print}.
	 * @param ctx the parse tree
	 */
	void exitPrint(APAGNANGAGEParser.PrintContext ctx);
	/**
	 * Enter a parse tree produced by {@link APAGNANGAGEParser#print_assign_string}.
	 * @param ctx the parse tree
	 */
	void enterPrint_assign_string(APAGNANGAGEParser.Print_assign_stringContext ctx);
	/**
	 * Exit a parse tree produced by {@link APAGNANGAGEParser#print_assign_string}.
	 * @param ctx the parse tree
	 */
	void exitPrint_assign_string(APAGNANGAGEParser.Print_assign_stringContext ctx);
	/**
	 * Enter a parse tree produced by {@link APAGNANGAGEParser#loop}.
	 * @param ctx the parse tree
	 */
	void enterLoop(APAGNANGAGEParser.LoopContext ctx);
	/**
	 * Exit a parse tree produced by {@link APAGNANGAGEParser#loop}.
	 * @param ctx the parse tree
	 */
	void exitLoop(APAGNANGAGEParser.LoopContext ctx);
	/**
	 * Enter a parse tree produced by {@link APAGNANGAGEParser#logic}.
	 * @param ctx the parse tree
	 */
	void enterLogic(APAGNANGAGEParser.LogicContext ctx);
	/**
	 * Exit a parse tree produced by {@link APAGNANGAGEParser#logic}.
	 * @param ctx the parse tree
	 */
	void exitLogic(APAGNANGAGEParser.LogicContext ctx);
	/**
	 * Enter a parse tree produced by {@link APAGNANGAGEParser#if}.
	 * @param ctx the parse tree
	 */
	void enterIf(APAGNANGAGEParser.IfContext ctx);
	/**
	 * Exit a parse tree produced by {@link APAGNANGAGEParser#if}.
	 * @param ctx the parse tree
	 */
	void exitIf(APAGNANGAGEParser.IfContext ctx);
	/**
	 * Enter a parse tree produced by {@link APAGNANGAGEParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(APAGNANGAGEParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link APAGNANGAGEParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(APAGNANGAGEParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link APAGNANGAGEParser#increment}.
	 * @param ctx the parse tree
	 */
	void enterIncrement(APAGNANGAGEParser.IncrementContext ctx);
	/**
	 * Exit a parse tree produced by {@link APAGNANGAGEParser#increment}.
	 * @param ctx the parse tree
	 */
	void exitIncrement(APAGNANGAGEParser.IncrementContext ctx);
}