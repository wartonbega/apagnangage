# Parser pour les options de bash (-o -i --HEEEEEELP ...)
import os
import argparse
import sys
import traceback

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
    argument_parser.add_argument("filename", nargs="?")
    argument_parser.add_argument("--enlève_toutes_les_sécurités", const=True, nargs="?")
    argument_parser.add_argument("--input", "-i", action="store", type=str, help="Spécifie le programme à lancer directement en ligne de commande")
    argument_parser.add_argument("--sortie", "-s", help="Spécifie le fichier de log de sortie (pas random)")
    # parser.add_argument("-t", "--tree", const=True, nargs="?", help="Affiche l'arbre de syntaxe abstrait")
    args = argument_parser.parse_args()
    if args.filename:
        input_file_name = args.filename
        input_stream = uf.readfile(input_file_name)
    elif args.input:
        input_file_name = None
        input_stream = args.input
    else:
        argument_parser.print_help()
        sys.exit()
    log_file = securities.chose_random_file()
    if args.sortie:
        log_file = args.sortie

    no_security = False
    if args.enlève_toutes_les_sécurités:
        no_security = True

    if not no_security:
        if input_file_name is not None:
            securities.first_security(input_file_name)
        securities.setup_print(log_file)

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
            vinterp = visitor.Visitor()
            vinterp.visit(parse_tree)
        except Exception as e:
            print(
                "Il y a manifestement un bug dans l'apagnangage. Ça doit être de ta faute. \n Quoi ??? Tu a cassé l'apagnangge. RAAAAAAAAAAAAh👹🤬🤯😵")
            traceback.print_exc()