
# Parser pour les options de bash (-o -i --HEEEEEELP ...)
import argparse

# Lexer et parser APAGNAN
from antlr4 import *
from APAGNANGAGELexer import APAGNANGAGELexer as ALexer
from APAGNANGAGEParser import APAGNANGAGEParser as AParser
from APAGNANGAGEListener import APAGNANGAGEListener as AListener


# Des trucs utiles
import useful as uf


if __name__ == '__main__':
    #################################################
    # Parsing des arguments de la ligne de commande #
    #################################################
    argument_parser = argparse.ArgumentParser(
        prog="Interpréteur de l'APAGNANGAGE",
        description="Interpète l'APAGNANGAGE",
        epilog="POV TU FAIT UN APAGNAN DANS L'INTERPRÉTEUR DE L'APAGNANGAGE (APAGNAAAAAAAAAAA)",
    )
    argument_parser.add_argument("filename")
    args = argument_parser.parse_args()
    input_file_name = args.filename
    
    input_stream = uf.readfile(input_file_name)
    

    #################################################
    # Parsing du/des fichiers d'entrée              #
    #################################################
    lexer = ALexer(InputStream(input_stream))
    parser = AParser(CommonTokenStream(lexer))
    parse_tree = parser.program()
    print(parse_tree.toStringTree(recog=parser))