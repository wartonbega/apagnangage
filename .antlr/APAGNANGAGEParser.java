// Generated from /Users/antonappel/Desktop/Code/apagnangage/APAGNANGAGE.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class APAGNANGAGEParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ID=1, INT=2, PRINT=3, ASSIGN=4, FUNCTION_CALL=5, BLOCK_START=6, BLOCK_END=7, 
		EQUALS=8, PLUS=9, MINUS=10, MULTIPLY=11, DIVIDE=12, LOOP=13, LOOP_COUNTER=14, 
		BREAK=15, IF=16, STRING_ASSIGN=17, STRING_LINE=18, COMMENT=19, WS_=20;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_assignment = 2, RULE_expression = 3, 
		RULE_function_call = 4, RULE_print = 5, RULE_print_assign_string = 6, 
		RULE_loop = 7, RULE_logic = 8, RULE_if = 9, RULE_block = 10, RULE_increment = 11;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "assignment", "expression", "function_call", 
			"print", "print_assign_string", "loop", "logic", "if", "block", "increment"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, "'POV'", "'QUOI'", "'FEUR'", "'FAIT'", "'BELECK'", 
			null, "'+'", "'-'", "'*'", "'/'", null, "'OUH'", "'FF'", "'GENRE'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "ID", "INT", "PRINT", "ASSIGN", "FUNCTION_CALL", "BLOCK_START", 
			"BLOCK_END", "EQUALS", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "LOOP", 
			"LOOP_COUNTER", "BREAK", "IF", "STRING_ASSIGN", "STRING_LINE", "COMMENT", 
			"WS_"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "APAGNANGAGE.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public APAGNANGAGEParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(APAGNANGAGEParser.EOF, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(27);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 253994L) != 0)) {
				{
				{
				setState(24);
				statement();
				}
				}
				setState(29);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(30);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public Function_callContext function_call() {
			return getRuleContext(Function_callContext.class,0);
		}
		public PrintContext print() {
			return getRuleContext(PrintContext.class,0);
		}
		public Print_assign_stringContext print_assign_string() {
			return getRuleContext(Print_assign_stringContext.class,0);
		}
		public LoopContext loop() {
			return getRuleContext(LoopContext.class,0);
		}
		public IfContext if_() {
			return getRuleContext(IfContext.class,0);
		}
		public TerminalNode BREAK() { return getToken(APAGNANGAGEParser.BREAK, 0); }
		public IncrementContext increment() {
			return getRuleContext(IncrementContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(40);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(32);
				assignment();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(33);
				function_call();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(34);
				print();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(35);
				print_assign_string();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(36);
				loop();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(37);
				if_();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(38);
				match(BREAK);
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(39);
				increment();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(APAGNANGAGEParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(APAGNANGAGEParser.ASSIGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(42);
			match(ID);
			setState(43);
			match(ASSIGN);
			setState(44);
			expression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public List<TerminalNode> PLUS() { return getTokens(APAGNANGAGEParser.PLUS); }
		public TerminalNode PLUS(int i) {
			return getToken(APAGNANGAGEParser.PLUS, i);
		}
		public List<TerminalNode> MINUS() { return getTokens(APAGNANGAGEParser.MINUS); }
		public TerminalNode MINUS(int i) {
			return getToken(APAGNANGAGEParser.MINUS, i);
		}
		public List<TerminalNode> MULTIPLY() { return getTokens(APAGNANGAGEParser.MULTIPLY); }
		public TerminalNode MULTIPLY(int i) {
			return getToken(APAGNANGAGEParser.MULTIPLY, i);
		}
		public List<TerminalNode> DIVIDE() { return getTokens(APAGNANGAGEParser.DIVIDE); }
		public TerminalNode DIVIDE(int i) {
			return getToken(APAGNANGAGEParser.DIVIDE, i);
		}
		public List<TerminalNode> EQUALS() { return getTokens(APAGNANGAGEParser.EQUALS); }
		public TerminalNode EQUALS(int i) {
			return getToken(APAGNANGAGEParser.EQUALS, i);
		}
		public List<Function_callContext> function_call() {
			return getRuleContexts(Function_callContext.class);
		}
		public Function_callContext function_call(int i) {
			return getRuleContext(Function_callContext.class,i);
		}
		public List<TerminalNode> INT() { return getTokens(APAGNANGAGEParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(APAGNANGAGEParser.INT, i);
		}
		public List<TerminalNode> ID() { return getTokens(APAGNANGAGEParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(APAGNANGAGEParser.ID, i);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_expression);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(54); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					setState(54);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case PLUS:
						{
						setState(46);
						match(PLUS);
						}
						break;
					case MINUS:
						{
						setState(47);
						match(MINUS);
						}
						break;
					case MULTIPLY:
						{
						setState(48);
						match(MULTIPLY);
						}
						break;
					case DIVIDE:
						{
						setState(49);
						match(DIVIDE);
						}
						break;
					case EQUALS:
						{
						setState(50);
						match(EQUALS);
						}
						break;
					case FUNCTION_CALL:
						{
						setState(51);
						function_call();
						}
						break;
					case INT:
						{
						setState(52);
						match(INT);
						}
						break;
					case ID:
						{
						setState(53);
						match(ID);
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(56); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Function_callContext extends ParserRuleContext {
		public TerminalNode FUNCTION_CALL() { return getToken(APAGNANGAGEParser.FUNCTION_CALL, 0); }
		public TerminalNode ID() { return getToken(APAGNANGAGEParser.ID, 0); }
		public Function_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_call; }
	}

	public final Function_callContext function_call() throws RecognitionException {
		Function_callContext _localctx = new Function_callContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_function_call);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(58);
			match(FUNCTION_CALL);
			setState(59);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrintContext extends ParserRuleContext {
		public TerminalNode PRINT() { return getToken(APAGNANGAGEParser.PRINT, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode STRING_LINE() { return getToken(APAGNANGAGEParser.STRING_LINE, 0); }
		public PrintContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_print; }
	}

	public final PrintContext print() throws RecognitionException {
		PrintContext _localctx = new PrintContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_print);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(61);
			match(PRINT);
			setState(64);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
			case INT:
			case FUNCTION_CALL:
			case EQUALS:
			case PLUS:
			case MINUS:
			case MULTIPLY:
			case DIVIDE:
				{
				setState(62);
				expression();
				}
				break;
			case STRING_LINE:
				{
				setState(63);
				match(STRING_LINE);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Print_assign_stringContext extends ParserRuleContext {
		public TerminalNode STRING_ASSIGN() { return getToken(APAGNANGAGEParser.STRING_ASSIGN, 0); }
		public TerminalNode ID() { return getToken(APAGNANGAGEParser.ID, 0); }
		public TerminalNode PRINT() { return getToken(APAGNANGAGEParser.PRINT, 0); }
		public Print_assign_stringContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_print_assign_string; }
	}

	public final Print_assign_stringContext print_assign_string() throws RecognitionException {
		Print_assign_stringContext _localctx = new Print_assign_stringContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_print_assign_string);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==PRINT) {
				{
				setState(66);
				match(PRINT);
				}
			}

			setState(69);
			match(STRING_ASSIGN);
			setState(70);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LoopContext extends ParserRuleContext {
		public List<TerminalNode> LOOP() { return getTokens(APAGNANGAGEParser.LOOP); }
		public TerminalNode LOOP(int i) {
			return getToken(APAGNANGAGEParser.LOOP, i);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public List<TerminalNode> ID() { return getTokens(APAGNANGAGEParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(APAGNANGAGEParser.ID, i);
		}
		public List<TerminalNode> LOOP_COUNTER() { return getTokens(APAGNANGAGEParser.LOOP_COUNTER); }
		public TerminalNode LOOP_COUNTER(int i) {
			return getToken(APAGNANGAGEParser.LOOP_COUNTER, i);
		}
		public LoopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_loop; }
	}

	public final LoopContext loop() throws RecognitionException {
		LoopContext _localctx = new LoopContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_loop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(72);
			match(LOOP);
			setState(74);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(73);
				match(ID);
				}
			}

			setState(76);
			match(LOOP);
			setState(84);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				{
				setState(77);
				match(ID);
				}
				break;
			case BLOCK_START:
			case LOOP_COUNTER:
			case BREAK:
				{
				setState(81);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==LOOP_COUNTER) {
					{
					{
					setState(78);
					match(LOOP_COUNTER);
					}
					}
					setState(83);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(86);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LogicContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode EQUALS() { return getToken(APAGNANGAGEParser.EQUALS, 0); }
		public LogicContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logic; }
	}

	public final LogicContext logic() throws RecognitionException {
		LogicContext _localctx = new LogicContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_logic);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(88);
			expression();
			setState(89);
			match(EQUALS);
			setState(90);
			expression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(APAGNANGAGEParser.IF, 0); }
		public LogicContext logic() {
			return getRuleContext(LogicContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public IfContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if; }
	}

	public final IfContext if_() throws RecognitionException {
		IfContext _localctx = new IfContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_if);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(92);
			match(IF);
			setState(93);
			logic();
			setState(94);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockContext extends ParserRuleContext {
		public TerminalNode BLOCK_START() { return getToken(APAGNANGAGEParser.BLOCK_START, 0); }
		public TerminalNode BLOCK_END() { return getToken(APAGNANGAGEParser.BLOCK_END, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public TerminalNode BREAK() { return getToken(APAGNANGAGEParser.BREAK, 0); }
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_block);
		int _la;
		try {
			setState(105);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BLOCK_START:
				enterOuterAlt(_localctx, 1);
				{
				setState(96);
				match(BLOCK_START);
				setState(100);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 253994L) != 0)) {
					{
					{
					setState(97);
					statement();
					}
					}
					setState(102);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(103);
				match(BLOCK_END);
				}
				break;
			case BREAK:
				enterOuterAlt(_localctx, 2);
				{
				setState(104);
				match(BREAK);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IncrementContext extends ParserRuleContext {
		public TerminalNode LOOP_COUNTER() { return getToken(APAGNANGAGEParser.LOOP_COUNTER, 0); }
		public TerminalNode ID() { return getToken(APAGNANGAGEParser.ID, 0); }
		public IncrementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_increment; }
	}

	public final IncrementContext increment() throws RecognitionException {
		IncrementContext _localctx = new IncrementContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_increment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(107);
			match(LOOP_COUNTER);
			setState(108);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u0014o\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0001"+
		"\u0000\u0005\u0000\u001a\b\u0000\n\u0000\f\u0000\u001d\t\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001)\b\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0004\u0003"+
		"7\b\u0003\u000b\u0003\f\u00038\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0003\u0005A\b\u0005\u0001\u0006\u0003"+
		"\u0006D\b\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001"+
		"\u0007\u0003\u0007K\b\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0005"+
		"\u0007P\b\u0007\n\u0007\f\u0007S\t\u0007\u0003\u0007U\b\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\n\u0001\n\u0005\nc\b\n\n\n\f\nf\t\n\u0001\n\u0001\n\u0003\nj"+
		"\b\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0000\u0000\f\u0000"+
		"\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0000\u0000y\u0000"+
		"\u001b\u0001\u0000\u0000\u0000\u0002(\u0001\u0000\u0000\u0000\u0004*\u0001"+
		"\u0000\u0000\u0000\u00066\u0001\u0000\u0000\u0000\b:\u0001\u0000\u0000"+
		"\u0000\n=\u0001\u0000\u0000\u0000\fC\u0001\u0000\u0000\u0000\u000eH\u0001"+
		"\u0000\u0000\u0000\u0010X\u0001\u0000\u0000\u0000\u0012\\\u0001\u0000"+
		"\u0000\u0000\u0014i\u0001\u0000\u0000\u0000\u0016k\u0001\u0000\u0000\u0000"+
		"\u0018\u001a\u0003\u0002\u0001\u0000\u0019\u0018\u0001\u0000\u0000\u0000"+
		"\u001a\u001d\u0001\u0000\u0000\u0000\u001b\u0019\u0001\u0000\u0000\u0000"+
		"\u001b\u001c\u0001\u0000\u0000\u0000\u001c\u001e\u0001\u0000\u0000\u0000"+
		"\u001d\u001b\u0001\u0000\u0000\u0000\u001e\u001f\u0005\u0000\u0000\u0001"+
		"\u001f\u0001\u0001\u0000\u0000\u0000 )\u0003\u0004\u0002\u0000!)\u0003"+
		"\b\u0004\u0000\")\u0003\n\u0005\u0000#)\u0003\f\u0006\u0000$)\u0003\u000e"+
		"\u0007\u0000%)\u0003\u0012\t\u0000&)\u0005\u000f\u0000\u0000\')\u0003"+
		"\u0016\u000b\u0000( \u0001\u0000\u0000\u0000(!\u0001\u0000\u0000\u0000"+
		"(\"\u0001\u0000\u0000\u0000(#\u0001\u0000\u0000\u0000($\u0001\u0000\u0000"+
		"\u0000(%\u0001\u0000\u0000\u0000(&\u0001\u0000\u0000\u0000(\'\u0001\u0000"+
		"\u0000\u0000)\u0003\u0001\u0000\u0000\u0000*+\u0005\u0001\u0000\u0000"+
		"+,\u0005\u0004\u0000\u0000,-\u0003\u0006\u0003\u0000-\u0005\u0001\u0000"+
		"\u0000\u0000.7\u0005\t\u0000\u0000/7\u0005\n\u0000\u000007\u0005\u000b"+
		"\u0000\u000017\u0005\f\u0000\u000027\u0005\b\u0000\u000037\u0003\b\u0004"+
		"\u000047\u0005\u0002\u0000\u000057\u0005\u0001\u0000\u00006.\u0001\u0000"+
		"\u0000\u00006/\u0001\u0000\u0000\u000060\u0001\u0000\u0000\u000061\u0001"+
		"\u0000\u0000\u000062\u0001\u0000\u0000\u000063\u0001\u0000\u0000\u0000"+
		"64\u0001\u0000\u0000\u000065\u0001\u0000\u0000\u000078\u0001\u0000\u0000"+
		"\u000086\u0001\u0000\u0000\u000089\u0001\u0000\u0000\u00009\u0007\u0001"+
		"\u0000\u0000\u0000:;\u0005\u0005\u0000\u0000;<\u0005\u0001\u0000\u0000"+
		"<\t\u0001\u0000\u0000\u0000=@\u0005\u0003\u0000\u0000>A\u0003\u0006\u0003"+
		"\u0000?A\u0005\u0012\u0000\u0000@>\u0001\u0000\u0000\u0000@?\u0001\u0000"+
		"\u0000\u0000A\u000b\u0001\u0000\u0000\u0000BD\u0005\u0003\u0000\u0000"+
		"CB\u0001\u0000\u0000\u0000CD\u0001\u0000\u0000\u0000DE\u0001\u0000\u0000"+
		"\u0000EF\u0005\u0011\u0000\u0000FG\u0005\u0001\u0000\u0000G\r\u0001\u0000"+
		"\u0000\u0000HJ\u0005\r\u0000\u0000IK\u0005\u0001\u0000\u0000JI\u0001\u0000"+
		"\u0000\u0000JK\u0001\u0000\u0000\u0000KL\u0001\u0000\u0000\u0000LT\u0005"+
		"\r\u0000\u0000MU\u0005\u0001\u0000\u0000NP\u0005\u000e\u0000\u0000ON\u0001"+
		"\u0000\u0000\u0000PS\u0001\u0000\u0000\u0000QO\u0001\u0000\u0000\u0000"+
		"QR\u0001\u0000\u0000\u0000RU\u0001\u0000\u0000\u0000SQ\u0001\u0000\u0000"+
		"\u0000TM\u0001\u0000\u0000\u0000TQ\u0001\u0000\u0000\u0000UV\u0001\u0000"+
		"\u0000\u0000VW\u0003\u0014\n\u0000W\u000f\u0001\u0000\u0000\u0000XY\u0003"+
		"\u0006\u0003\u0000YZ\u0005\b\u0000\u0000Z[\u0003\u0006\u0003\u0000[\u0011"+
		"\u0001\u0000\u0000\u0000\\]\u0005\u0010\u0000\u0000]^\u0003\u0010\b\u0000"+
		"^_\u0003\u0014\n\u0000_\u0013\u0001\u0000\u0000\u0000`d\u0005\u0006\u0000"+
		"\u0000ac\u0003\u0002\u0001\u0000ba\u0001\u0000\u0000\u0000cf\u0001\u0000"+
		"\u0000\u0000db\u0001\u0000\u0000\u0000de\u0001\u0000\u0000\u0000eg\u0001"+
		"\u0000\u0000\u0000fd\u0001\u0000\u0000\u0000gj\u0005\u0007\u0000\u0000"+
		"hj\u0005\u000f\u0000\u0000i`\u0001\u0000\u0000\u0000ih\u0001\u0000\u0000"+
		"\u0000j\u0015\u0001\u0000\u0000\u0000kl\u0005\u000e\u0000\u0000lm\u0005"+
		"\u0001\u0000\u0000m\u0017\u0001\u0000\u0000\u0000\u000b\u001b(68@CJQT"+
		"di";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}