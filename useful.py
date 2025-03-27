
from antlr4 import *
from APAGNANGAGELexer import APAGNANGAGELexer as Lexer
from APAGNANGAGEParser import APAGNANGAGEParser as Parser
from APAGNANGAGEListener import APAGNANGAGEListener as AListener
from antlr4.tree import Trees

from io import StringIO

#############################
# Librairie des trucs utils #
#############################


def readfile(filename: str) -> str:
    # Bien plus pratique d'avoir qu'une seul fonction
    # plutôt que deux lignes et une indentation ...
    with open(filename, "r") as file:
        return file.read()
    
    
def escapeWhitespace(s:str, escapeSpaces:bool):
    with StringIO() as buf:
        for c in s:
            if c==' ' and escapeSpaces:
                buf.write('\u00B7')
            elif c=='\t':
                buf.write("\\t")
            elif c=='\n':
                buf.write("\\n")
            elif c=='\r':
                buf.write("\\r")
            else:
                buf.write(c)
        return buf.getvalue()
