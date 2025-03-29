import securities

# À améliorer, on peut rajouter par exemple la localisation de l'erreur
def error(message, outstream: securities.OutputStream):
    outstream.write(message)
    securities.output_security(outstream)
    exit(1)