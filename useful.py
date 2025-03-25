#############################
# Librairie des trucs utils #
#############################


def readfile(filename):
    # Bien plus pratique d'avoir qu'une seul fonction
    # plutôt que deux lignes et une indentation ...
    with open(filename, "r") as file:
        return file.read()
