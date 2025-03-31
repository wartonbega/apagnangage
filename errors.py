from antlr4.ParserRuleContext import ParserRuleContext

import securities

# À améliorer, on peut rajouter par exemple la localisation de l'erreur
def error(message, ctx: ParserRuleContext | None = None, filename=""):
    if ctx is not None:
        message = f"Erreur à la ligne {filename}:{ctx.start.line}:{ctx.start.column} : {message}\n"
    print(message)
    exit(1)