from antlr4.ParserRuleContext import ParserRuleContext

import securities

# À améliorer, on peut rajouter par exemple la localisation de l'erreur
def error(message, outstream: securities.OutputStream, ctx: ParserRuleContext | None = None):
    if ctx is not None:
        message = f"Erreur à la ligne {ctx.start.line}:{ctx.start.column} : {message}\n"
    outstream.write(message)
    if not outstream.print_anyway:
        securities.output_security(outstream)
    exit(1)