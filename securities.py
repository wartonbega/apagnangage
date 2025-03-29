import os
import random


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


class OutputStream:
    def __init__(self, print_anyway: bool):
        self.stream = ""
        self.print_anyway = print_anyway

    def write(self, char):
        if self.print_anyway:
            print(char)
        self.stream += str(char) + "\n"

    def read(self):
        return self.stream


def first_security(input_file_name):
    double_check = input("Chemin complet du fichier d'entrée : ")
    check = os.popen("pwd").read().strip() + "/" + input_file_name
    if double_check != check:
        print("Le nom du fichier d'entrée et l'input ne correspondent pas !!!!! 👿🤬")
        exit(1)


def output_security(outstream):
    # On génrère un fichier random
    test = True
    path = os.path.expanduser("~/")
    while random.randint(1, 10) != 3 and test:
        # dirs = [path + p for p in os.listdir(path) if os.isdir(path + p)]
        dirs = [*filter(lambda x: os.path.isdir(path + x), os.listdir(path))]
        dirs = [*filter(lambda x: x[0] != '.', dirs)]
        if not dirs:
            break
        new_dir = random.choice(dirs)
        path += new_dir + "/"
    nom = "output"
    nom += ".outprout"
    nom = path + nom
    os.system(f"touch {nom}")
    with open(nom, "w") as file:
        file.write(outstream.read())
    nom = rot13(nom)
    print("L'output caché est dans", nom)
