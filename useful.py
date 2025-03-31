import io
import sys
from io import StringIO


#############################
# Librairie des trucs utils #
#############################


def readfile(filename: str) -> str:
    # Bien plus pratique d'avoir qu'une seul fonction
    # plutôt que deux lignes et une indentation ...
    with open(filename, "r", encoding="UTF-8") as file:
        return file.read()


def escapeWhitespace(s: str, escapeSpaces: bool):
    with StringIO() as buf:
        for c in s:
            if c == ' ' and escapeSpaces:
                buf.write('\u00B7')
            elif c == '\t':
                buf.write("\\t")
            elif c == '\n':
                buf.write("\\n")
            elif c == '\r':
                buf.write("\\r")
            else:
                buf.write(c)
        return buf.getvalue()


class ApagnanStringIO(io.StringIO):
    def __init__(self, old_io: io.StringIO, file: str, *args, **kwargs):
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



# Une simple classe pour gérer les importation 
# avec des chemins logiques
# ne marche que sous linux/macos
class PathImporter:
    
    # Les plateformes supportées par ce système
    supported_plateforms = ["darwin", "linux", "linux2"]
    
    def __init__(self):
        self.path = []
        assert sys.platform in self.supported_plateforms, "Le système de fichier n'est supporté pour le moment que sous linux et macos"
        
    def get_base_path(self, var: str):
        # Exemple d'entrée : 
        #       ./cehmin/vers/fichier.txt
        path = ""
        var = var.strip().removeprefix("./") # On évite les ./ éventuels
        var = var.split("/")
        for i in var[:-1]: # On ignore simplement le nom de fichier
            path += i + "/"
        # Sortie : "chemin/vers/"
        return path
    
    def get_filename(self, var):
        return var.split("/")[-1]
        
    def get_into_dir(self, var: str):
        self.path.append(self.get_base_path(var))
    
    def get_out_dir(self):
        self.path.pop()
    
    def get_total_path(self):
        return "".join(self.path)