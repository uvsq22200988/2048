#projet 2048

import tkinter as tk
import random as rd

H_1= 800
L_1= 1000
H_2= 700
L_2= 700
#création de la fenêtre
racine= tk.Tk()
canvas=tk.Canvas(racine,background="grey",height= H_1, width= L_1)
racine.title("2048")
#lancement de la boucle principale
racine.mainloop()
#Création widget start (pour commencer le jeu) afin d'emmener le joueur sur la page de jeu
boutton_start= tk.Button(racine, text= "JOUER", "RENTRER UN PARAMETRE ")
boutton_start.pack()
#création du menu comprenant les infos suivantes : score, meilleure score, nouvelle partie

#faire une matrice 4*4
matrice= [[0]*4 for e in range (5)]



#definir les actions
actions = ["up", "down","left","right","restart","exit"]


#definir le jeu
def jeu():
   if actions == "restart":
       return "Init"
   if actions == "exit":
       return " exit"
       if le joueur a gagné:
           return "Win"
       if le joueur a perdu:
           return "Gameover"


#definir les mouvements
def move(ligne):
   ###avec la fonction serre on va presser les tuiles
   def serre(ligne):
       ###pour les tuiles avec un nombre
       new_row = [ i for i in ligne if i != 0]
       ###pour les tuiles sans valeur
       new_row += [ 0 for i in range(len(ligne) - len(new_row))]
       return new_row
   ###avec la fonction fusion on va fusionner les tuiles adjacents ayant les memes nombres
   def fusion(ligne):
       pair = False
       new_row = []
       for i in range(len(ligne)):
           if pair:
               ###ici on definit l'action: 2 tuiles qui fusionnent = multiplie leur valeur par 2
               new_row.append(2 * ligne[i])
           else:
               ###si on fusionne 2 tuiles sur une ligne, alors on doit mettre une tuile vide(0) dans la ligne
               if i + 1 < len(ligne) and ligne[i] == ligne[i + 1]:
                   pair = True
                   new_row.append(0)
               ###si les 2 tuiles ne peuvent pas fusionner alors on doit ajouter ces elements a la nouvelle liste
               else:
                    new_row.append(ligne{i})
       ###on s'assure ue les fusion ne deforme pas la matrice
       assert len(new_row) == len(ligne)
       return new_row
   
