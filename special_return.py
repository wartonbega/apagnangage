
###############################################################
# Ensemble des valeurs de retour spéciaux pour les statements #
# comme return ou break ou etc...                             #
###############################################################

class SpecialReturn:
    ...
    
class Return(SpecialReturn):
    __match_args__ = ("value",)
    def __init__(self, value):
        self.value = value

class Break(SpecialReturn):
    ...