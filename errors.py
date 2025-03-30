import securities

# À améliorer, on peut rajouter par exemple la localisation de l'erreur
def error(message, outstream: securities.OutputStream):
    outstream.write(message)
    if not outstream.print_anyway:
        securities.output_security(outstream)
    exit(1)