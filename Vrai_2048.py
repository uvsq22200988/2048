#projet 2048

#Permet la création de l'interface graphique
import tkinter as tk
#Permet de générer des nombres aléatoires
import random

# Création de la fenêtre du jeux 
racine = tk.Tk()
rectangles = []
# Création d'une matrice 4x4 remplie de zéros
grille = [[0] * 4 for i in range(4)]
# Variable score initialisée à 0. Score au début du jeux qui va augmenter au fur et à mesure du jeux  
score = 0

# Création d'une fonction qui met à jour l'affichage du score
def maj_score():
    global score
    score_affichage.config(text=f"Score = {score}")

# Création d'une fonction qui lance le jeux
def debut_2048():
    global rectangles, grille
    
    
    # La variable 'i' représente l'indice de la ligne variant de 0 à 3
    for i in range(4):
        rectangles_ligne = []
        # La variable 'col' représente l'indice de la colonne varaint de 0 à 3
        for col in range(4):
            # Dimensions de l'objet rectangle
            rectangle = tk.Button(racine, text="", width=20, height=10, font=("helvatica",17))
            rectangle.grid(row=i, column=col)
            rectangles_ligne.append(rectangle)
        rectangles.append(rectangles_ligne)
        
    score_affichage.grid(row=6, column=1, columnspan=2)
    
    bouton_left.grid(row=2, column=5)
    bouton_right.grid(row=2, column=7)
    bouton_down.grid(row=2, column=9)
    bouton_up.grid(row=2, column=11)
    
    button_rejouer = tk.Button(racine, text="Nouvelle partie", command=recommencer_partie)
    button_rejouer.grid(row=1, column=5)
    bouton_quitter = tk.Button(racine, text="Quitter", command=quitter_partie)
    bouton_quitter.grid(row=1, column=7)
    
    aléatoire_départ()
    maj_score()
       
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


# Création d'une fonction qui permet de générer une nouvelle partie de jeux 
def recommencer_partie():
    global grille, score
    # Permet de remettre la grille à zéro
    grille = [[0] * 4 for i in range(4)]
    # Permet de réinitialiser le score
    score = 0
    # Permet de mettre à jour l'affichage de la grille et du score
    update_grid()
    maj_score()
    # Permet d'ajouter deux chiffres au hasard
    aléatoire_départ()
        
# Création d'une fonction qui permet de quitter la partie et d'afficher le score obtenu au cours de la partie        
def quitter_partie():
    global score
    racine.destroy()
    print(f"La partie est maintenant terminée, le score est de {score}")        
        
#Ajout des differents boutons dans la fenêtre
bouton_left = tk.Button(racine, text="Left", command =move_left)
bouton_right = tk.Button(racine, text="Right", command =move_right)
bouton_down = tk.Button(racine, text="Down", command =move_down)
bouton_up = tk.Button(racine, text="Up", command =move_up)

racine.mainloop()
 
