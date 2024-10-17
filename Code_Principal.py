from Personnage_class import *
from Epee_class import *
from tkinter import *
from tkinter import messagebox

persoChoisi=None
compteur=0

def histoire():
    global persoChoisi, compteur, window,LABEL,LabelPerso
    file = open("histoire.txt", "r",encoding="utf-8")
    liste = file.readlines()
    file.close()
    LABEL=Label(window, text=liste[compteur])
    LABEL.pack()
    liste.pop(compteur)
    if persoChoisi==None:
        LabelPerso=Label(window, text="Pas de Personnage")
        LabelPerso.pack()
    if persoChoisi!=None:
        LabelPerso=Label(window, text=persoChoisi)
        LabelPerso.pack()
    if compteur==0:
        BOUTON.destroy()
    if compteur==3:
        LabelListeArmesPerso=Label(window,text=persoChoisi.getlistepossessionarmes())
        LabelListeArmesPerso.pack()
    valider()
    return

def valider():
    global compteur
    compteur+=1
    return

def REPONSE():
    global persoChoisi, liste_perso, Saisie, LabelPerso, LABEL,compteur, Excalibur, window, mechant, FenetreValider
    SAISIE=Saisie.get()
    if compteur==1:
        for perso in liste_perso:
            if SAISIE==perso.getnom():
                persoChoisi=perso
        if persoChoisi==None:
            messagebox.showinfo(title="EXTRA", message="Tu n'es pas le héros de cette histoire.")
            window.destroy()
            FenetreValider.destroy()
            return
    if compteur==2:
        if SAISIE=="A":
            persoChoisi.AjoutARMEinventaire(excalibur)
            messagebox.showinfo(title="EXTRA", message="Vous obtenez Excalibur ! Vous êtes un véritable héro désormais !")
        if SAISIE=="B":
            messagebox.showinfo(title="EXTRA", message="Vous Laissez l'épée, Vous vous sentez fier d'être pacifique ! :) +5 HP")
            HP=persoChoisi.gethp()+5
            persoChoisi.sethp(HP)
        if SAISIE=="C":
            messagebox.showinfo(title="EXTRA", message="Vous cachez l'épée, vous vous sentez intelligent. Mais au plus profond de vous, vous savez que vous ne la retrouverez jamais...")
    if compteur==3:
        if SAISIE=="A":
            messagebox.showinfo(title="EXTRA", message="On ne parle pas avec un méchant. Il vous tue : Fin de l'histoire.")
            window.destroy()
            FenetreValider.destroy()
            return
        if SAISIE=="C":
            messagebox.showinfo(title="EXTRA", message="Vous êtes un lâche! Vous ne méritez pas de continuer cette histoire!")
            window.destroy()
            FenetreValider.destroy()
            return
    if compteur==4:
        for epee in persoChoisi.getlistepossessionarmes():
            if SAISIE==epee.getNom():
                persoChoisi.choisirArmeEnMain(epee.getNom())
                persoChoisi.attaque(mechant)
                if mechant.gethp()<=0:
                    messagebox.showinfo(title="EXTRA", message="Le méchant est mort, vous avez vaincu!")
                    window.destroy()
                    FenetreValider.destroy()
                    return
                else:
                    messagebox.showinfo(title="EXTRA", message="Le méchant est toujours vivant avec "+str(mechant.gethp())+" points de vie : Vous allez prendre cher ...")
                    window.destroy()
                    FenetreValider.destroy()
                    return
    LABEL.destroy()
    LabelPerso.destroy()
    histoire()
    return

dague = Epee("Dague",1)
aiguille = Epee("Aiguille",3)
canif = Epee("Canif",2)
excalibur = Epee("Excalibur",20)
durandal = Epee("Durandal",15)

liste_epee=[]
liste_epee.append(dague)
liste_epee.append(aiguille)
liste_epee.append(canif)
liste_epee.append(excalibur)
liste_epee.append(durandal)
for j in liste_epee:
    print(j)


ouioui = Personnage("Oui-Oui",20)
ouioui.AjoutARMEinventaire(dague)
lannister = Personnage("Lannister",30)
lannister.AjoutARMEinventaire(excalibur)
conan = Personnage("Conan",25)
conan.AjoutARMEinventaire(canif)
mechant = Personnage("méchant",28)
mechant.AjoutARMEinventaire(aiguille)

liste_perso=[]

liste_perso.append(ouioui)
liste_perso.append(lannister)
liste_perso.append(conan)
liste_perso.append(mechant)
for i in liste_perso:
    print(i)


"""p1.AjoutARMEinventaire(epee1)
p1.AjoutARMEinventaire(epee2)

nomA=input("choisi l'arme que tu possèdes : ")
p1.choisirArmeEnMain(nomA)
print(p1)

p1.attaque(p2)
print(p2)"""


window = Tk()
FenetreValider=Tk()
window.geometry("700x200")
FenetreValider.geometry("200x200")
BOUTON=Button(window, text="Commencer la partie", command=histoire)
BOUTON.pack()
label1=Label(FenetreValider,text="saisir votre choix : ")
label1.pack()
Saisie=Entry(FenetreValider)
Saisie.pack()
Bouton1 = Button(FenetreValider, text="Valider", command=REPONSE)
Bouton1.pack()
window.mainloop()
FenetreValider.mainloop()
