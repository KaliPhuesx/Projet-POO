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

p1.AjoutARMEinventaire(epee1)
p1.AjoutARMEinventaire(epee2)

nomA=input("choisi l'arme que tu possèdes : ")
p1.choisirArmeEnMain(nomA)
print(p1)

p1.attaque(p2)
print(p2)

window = Tk()
window.geometry("1280x720")

window.mainloop()
