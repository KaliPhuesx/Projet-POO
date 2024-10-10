from Personnage_class import *
from Epee_class import *
from tkinter import * 

def histoire():
    file = open("histoire.txt", "r",encoding="utf-8")
    liste = file.readlines()
    file.close()
    print(liste[0])
    liste.pop(0)

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

listePossessionArmes=[]
p1.AjoutARMEinventaire(listePossessionArmes,epee1.getNom())
if epee2 != None:
    p1.AjoutARMEinventaire(listePossessionArmes,epee2.getNom())
print("le guerrier possède : "+str(listePossessionArmes))

nomA=input("choisi l'arme que tu possèdes : ")
for EPEE in listePossessionArmes:
    if nomA==EPEE:
        p1.choisirArmeEnMain(EPEE)
print(p1)

window = Tk()
window.geometry("1280x720")

window.mainloop()
