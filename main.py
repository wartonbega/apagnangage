
# Parser pour les options de bash (-o -i --HEEEEEELP ...)
import argparse

# Lexer et parser APAGNAN
from antlr4 import *
from APAGNANGAGELexer import APAGNANGAGELexer as Lexer
from APAGNANGAGEParser import APAGNANGAGEParser as Parser
from APAGNANGAGEListener import APAGNANGAGEListener as Listener


# Des trucs utiles
import useful as uf


if __name__ == '__main__':
    #################################################
    # Parsing des arguments de la ligne de commande #
    #################################################
    options_parser = argparse.ArgumentParser(
        prog="Interpréteur de l'APAGNANGAGE",
        description="Interpète l'APAGNANGAGE",
        epilog="POV TU FAIT UN APAGNAN DANS L'INTERPRÉTEUR DE L'APAGNANGAAAAAAAAGE (APAGNAAAAAAAAAAA)",
    )
    options_parser.add_argument("filename")
    args = options_parser.parse_args()
    input_file_name = args.filename
    
    input_stream = uf.readfile(input_file_name)
    

    #################################################
    # Parsing du/des fichiers d'entrée              #
    #################################################
    lexer = Lexer(InputStream(input_stream))
    parser = Parser(CommonTokenStream(lexer))
    parse_tree = parser.parse()
    print(parse_tree.toStringTree(recog=parser))