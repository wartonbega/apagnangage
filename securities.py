import os, sys
import random
import io


def rot13(s):
    chars = "abcdefghijklmnopqrstuvwxyz"
    majs = chars.upper()
    trans = chars[13:] + chars[:13]
    transmaj = majs[13:] + majs[:13]

    def rot_char(c):
        if chars.find(c) > - 1:
            return trans[chars.find(c)]
        elif majs.find(c) > - 1:
            return transmaj[majs.find(c)]
        return c

    return ''.join(rot_char(c) for c in s)

def chose_random_file() -> str:
    path = os.path.expanduser("~/")
    while random.randint(1, 10) != 3:
        # dirs = [path + p for p in os.listdir(path) if os.isdir(path + p)]
        dirs = [*filter(lambda x: os.path.isdir(path + x), os.listdir(path))]
        dirs = [*filter(lambda x: x[0] != '.' and os.access(path + x, os.W_OK), dirs)]
        if not dirs:
            break
        new_dir = random.choice(dirs)
        path += new_dir + "/"
    nom = path + "apagnan.outprout"
    return nom
    
class OutputStringIO(io.StringIO):
    def __init__(self, old_io: io.StringIO, filename, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__old_io = old_io
        self.__file = open(filename, "w+")

    def write(self, s: str):
        super().write(s)
        self.__old_io.write(s)
        self.__file.write(s)

    def close(self):
        self.__old_io.close()
        self.__file.close()
        super().close()

def setup_print(filename: str):
    """
    Redirige la sortie standard vers un fichier de log
    """
    print("L'output caché est dans", filename)
    sys.stdout = OutputStringIO(sys.stdout, filename)

def first_security(input_file_name):
    double_check = input("Chemin complet du fichier d'entrée : ")
    check = os.popen("pwd").read().strip() + "/" + input_file_name
    if double_check != check:
        print("Le nom du fichier d'entrée et l'input ne correspondent pas !!!!! 👿🤬")
        exit(1)