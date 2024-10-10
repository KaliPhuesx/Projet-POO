class Personnage:
    __name = ""
    __hp = 0
    __armeEnMain=None
    
    def __init__(self, name, hp):
        self.__name = name
        self.__hp = hp 
        
    def getName(self):
        return self.__name
    def getHp(self):
        return self.__hp
    
    def __str__(self):
        if self.__armeEnMain==None:
            return ("Le personnage s'appelle "+self.__nom+", il a "+str(self.__hp)+" points de vie")
        else:
            return ("Le personnage s'appelle "+self.__nom+", il a "+str(self.__hp)+" points de vie, et porte actuellement sur lui : "+str(self.__armeEnMain))

    def choisirArmeEnMain(self,EPEE):
        self.__armeEnMain=EPEE

    def getarmeenmain(self):
        return self.__armeEnMain

    def AjoutARMEinventaire(self,liste:list,epee):
        if len(liste)<5:
            liste.append(epee)
        return liste

    
