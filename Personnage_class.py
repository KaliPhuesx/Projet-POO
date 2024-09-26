class Personnage:
    __name = ""
    __hp = 0
    
    def __init__(self, name, hp):
        self.__name = name
        self.__hp = hp 
        
    def getName(self):
        return self.__name
    def getHp(self):
        return self.__hp
    
    def __str__(self):
        return (" Name : " +self.__name+" and have : "+self.__hp+ "HP")
