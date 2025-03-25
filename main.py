from antlr4 import *
from APAGNANGAGELexer import APAGNANGAGELexer as Lexer
from APAGNANGAGEParser import APAGNANGAGEParser as Parser
from APAGNANGAGEListener import APAGNANGAGEListener as Listener

if __name__ == '__main__':
    lexer = Lexer(InputStream('Hi Trekkie'))
    parser = Parser(CommonTokenStream(lexer))
    parse_tree = parser.parse()
    print(parse_tree.toStringTree(recog=parser))