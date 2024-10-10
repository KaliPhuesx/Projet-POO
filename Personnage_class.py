from Epee_class import *

class Personnage:
    __nom=""
    __hp=0
    __armeEnMain=None


    def __init__(self,nom,hp):
        self.__nom=nom
        self.__hp=hp
        self.__listePossessionArmes=[]

    def getnom(self):
        return self.__nom
    def gethp(self):
        return self.__hp

    def sethp(self,hp):
        self.__hp=hp

    def __str__(self):
        if self.__armeEnMain==None:
            return ("Le personnage s'appelle "+self.__nom+", il a "+str(self.__hp)+" points de vie")
        else:
            return ("Le personnage s'appelle "+self.__nom+", il a "+str(self.__hp)+" points de vie, et porte actuellement sur lui : "+str(self.__armeEnMain))

    def choisirArmeEnMain(self,NomEpee):
        for epee in self.__listePossessionArmes:
            if NomEpee==epee.getNom():
                print("arme trouvée")
                self.__armeEnMain=epee

    def getarmeenmain(self):
        return self.__armeEnMain

    def attaque(self,guerrier):
        DEGAT=self.getarmeenmain().getNiveauAttaque()
        if self.getnom()=="Lannister" and self.getarmeenmain().getNom()=="Durandal":
            DEGAT=self.getarmeenmain().getNiveauAttaque()*2
        if self.getnom()=="Conan" and self.getarmeenmain().getNom()=="Excalibur":
            DEGAT=self.getarmeenmain().getNiveauAttaque()*2
        degatTotal=guerrier.gethp()-DEGAT
        guerrier.sethp(degatTotal)
        return


    def AjoutARMEinventaire(self,epee):
        if len(self.__listePossessionArmes)<5:
            self.__listePossessionArmes.append(epee)

