class Personnage:
    __nom=""
    __hp=0


    def __init__(self,nom,hp):
        self.__nom=nom
        self.__hp=hp

    def getnom(self):
        return self.__nom
    def gethp(self):
        return self.__hp

    def __str__(self):
        return ("Le personnage s'appelle "+self.__nom+", il a "+str(self.__hp)+" points de vie")
