from Personnage import *
from Epee import *

p1=Personnage("Conan",78)
p2=Personnage("Lannister",45)
epee1=Epee("Excalibur", 7)
epee2=Epee("Durandal", 4)

liste_epee=[]
liste_epee.append(epee1)
liste_epee.append(epee2)
for j in liste_epee:
    print(j)

liste_perso=[]

liste_perso.append(p1)
liste_perso.append(p2)
for i in liste_perso:
    print(i)
