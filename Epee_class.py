# Créé par Eleve, le 26/09/2024 en Python 3.7
class Epee:
    __nom=""
    __niveauAttaque=0

    def __init__(self,nom,niveauAttaque):
        print ("initialisation des 2 paramètres")
        self.__nom=nom
        self.__niveauAttaque=niveauAttaque

    def getNom(self):
        return self.__nom

    def getNiveauAttaque(self):
        return self.__niveauAttaque

    def __str__(self):
        total=self.__nom+"  "+str(self.__niveauAttaque)
        return total
