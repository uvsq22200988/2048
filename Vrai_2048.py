#projet 2048

import tkinter as tk
import random as rd

# Création de la matrice 4x4 vide
matrice=[[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]]

# Création de la fênetre 
racine= tk.Tk()
FONT=('Ubuntu', 75, 'bold')
canvas= tk.Canvas(racine,background='white',height = 800, width = 800)
canvas.grid(column=1, row= 1)
racine.title("2048")

# Création de la fonction permettant de lancer le jeux 
def start_2048():
    for i in range(4):
        for j in range(4):
            a, b=200*j, 200*i
            A, B, C=(a, b), (a+200, b+200), (a+100, b+100)
        canvas.create_rectangle(A, B, fill='darkgrey')
        canvas.create_text(C, text=matrice[i][j], fill ='white', font=FONT)

#Création widget start (pour commencer le jeu) afin d'emmener le joueur sur la page de jeu
boutton_start= tk.Button(racine, text= "JOUER", bg= "orange",font= "200",command= start_2048)
boutton_start.grid(column= 1, row= 1)



    


#création de l'espace de jeu


#création du menu comprenant les infos suivantes : score, meilleure score, nouvelle partie
def menu():
    score= tk.Menu(canvas, bg= "yellow",fg= "black", font= "300", command= boutton_start)
    score.grid(column= 1, row= 1, padx= 600)

#création du menu comprenant les infos suivantes : score, meilleure score, nouvelle partie


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
   racine.mainloop()
       
       
       
       
       
       
       
       
       
# GENERER UN NOMBRE ALEATOIRE  
       
import random
# Générer un nombre aléatoire en 0 et 10 nous permettant de savoir si nous faisons apparaitre un 2 ou un 4 
chiffre_aleatoire = random.randint (0,10)
#Le chiffre 2 a 90% de chance d'être obtenu alors que le 4 seulement 10% 
if chiffre_aleatoire <= 9 :
    print(2)
else : 
    print(4)
    

# Création d'une liste qui parcourt la matrice permettant de trouver les positions des zéros de cette matrice
positions_des_zeros = [(i, j) for i, row in enumerate(matrice) for j, element in enumerate(row) if element == 0]

print(positions_des_zeros)


def ajouter_chiifre_aleatoire (matrice, positions_des_zeros, print):
    # On choisit une position au hasard dans la liste positions_des_zeros
    position = random.choice(positions_des_zeros)
    
    # On ajoute le chiffre à la position choisie dans la matrice
    matrice[position[0]][position[1]] = print
    
    # On retourne la matrice modifiée
    return matrice
 
