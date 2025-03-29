
# Parser pour les options de bash (-o -i --HEEEEEELP ...)
import os
import argparse

# Lexer et parser APAGNAN
from antlr4 import *
from APAGNANGAGELexer import APAGNANGAGELexer as Lexer
from APAGNANGAGEParser import APAGNANGAGEParser as Parser

import visitor

# Des trucs utiles
import useful as uf

import securities

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
    argument_parser.add_argument("--enlève_toute_les_sécuritées", const=True, nargs="?")
    #parser.add_argument("-t", "--tree", const=True, nargs="?", help="Affiche l'arbre de syntaxe abstrait")
    args = argument_parser.parse_args()
    input_file_name = args.filename
    no_security = False
    if args.enlève_toute_les_sécuritées:
        no_security = True
    
    input_stream = uf.readfile(input_file_name)
    
    if not no_security:
        securities.first_security(input_file_name)

    output_stream = securities.OutputStream(no_security)

    #################################################
    # Parsing du/des fichiers d'entrée              #
    #################################################
    lexer = Lexer(InputStream(input_stream))
    parser = Parser(CommonTokenStream(lexer))
    parse_tree = parser.program()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
    else:
        try:
            vinterp = visitor.Visitor(output_stream)
            vinterp.visit(parse_tree)
        except Exception as e:
            print("Il y a manifestement un bug dans l'apagnangage. Ça doit être de ta faute. \n Quoi ??? Tu a cassé l'apagnangge. RAAAAAAAAAAAAh👹🤬🤯😵")
            print(e)

    if not no_security:
        securities.output_security(output_stream)