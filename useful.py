import io
import sys
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

class ApagnanStringIO(io.StringIO):
    def __init__(self, old_io: io.StringIO, file:str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__old_io = old_io
        self.__file = open(file, "w+")

    def write(self, s: str):
        super().write(s)
        self.__old_io.write(s)
        self.__file.write(s)

    def close(self):
        self.__old_io.close()
        self.__file.close()
        super().close()



def setup_print(logfile: str):
    """
    Redirige la sortie standard vers un fichier de log
    :param logfile: Le nom du fichier de log
    """
    sys.stdout = ApagnanStringIO(sys.stdout, logfile)