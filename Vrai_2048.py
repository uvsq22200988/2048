#projet 2048

import tkinter as tk
import random as rd

H_1= 800
L_1= 1000
H_2= 700
L_2= 700

racine= tk.Tk()
canvas=tk.Canvas(racine,background="couleur",height= H_1, width= L_1)
racine.title("2048")


#faire une matrice 4*4
matrice= [[0]*4 for e in range (5)]

def start_2048():
    #créer le carré de jeu
    canvas.create_rectangle((H_2, L_2), get_color="grey")



#créer un un quadrillage pour séparer les différentes cases du jeu
for e in range (1,5):
    canvas.create_line()
    canvas.create_line()
