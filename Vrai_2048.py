#projet 2048

#Permet la création de l'interface graphique
import tkinter as tk
#Permet de générer des nombres aléatoires
import random

racine = tk.Tk()
rectangles = []
grille = [[0] * 4 for i in range(4)]
# Variable score initialisée à 0. Score au début du jeux qui va augmenter au fur et à mesure du jeux  
score = 0

def update_score():
    global score
    score_affichage.config(text=f"Score = {score}")

def start_2048():
    global rectangles, grille
    
    for i in range(4):
        rectangles_ligne = []
        for col in range(4):
            rectangle = tk.Button(racine, text="", width=20, height=10)
            rectangle.grid(row=i, column=col)
            rectangles_ligne.append(rectangle)
        rectangles.append(rectangles_ligne)
        
    score_affichage.grid(row=6, column=1, columnspan=2)
    
    bouton_left.grid(row=1, column=5)
    bouton_right.grid(row=1, column=7)
    bouton_down.grid(row=1, column=9)
    bouton_up.grid(row=1, column=11)

    aléatoire_départ()
    update_score()
       
def verifie_gagne_ou_pas():
    global grille 
    if 2048 in grille :
        print("Gagné")
        
def aléatoire_départ():
    global grille, score
    indices = random.sample(range(16), 2)
    for i in indices:
        row = i // 4
        col = i % 4
        random_number = debut_chiffre()
        grille[row][col] = random_number
        score += random_number
        rectangles[row][col].config(text=str(grille[row][col]))
        
def debut_chiffre():
    chiffre_aleatoire = random.randint(0, 10)
    if chiffre_aleatoire <= 9:
        return 2
    else:
        return 4
    
score_affichage = tk.Label(racine, text=f"Score = {score}")

button_play = tk.Button(racine, text="Jouer", command=start_2048)
button_play.grid(row=0, column=0)



#Ajout des differents boutons dans la fenêtre
bouton_left = tk.Button(racine, text="Left", command =move_left)
bouton_right = tk.Button(racine, text="Right", command =move_right)
bouton_down = tk.Button(racine, text="Down", command =move_down)
bouton_up = tk.Button(racine, text="Up", command =move_up)

racine.mainloop()
 
