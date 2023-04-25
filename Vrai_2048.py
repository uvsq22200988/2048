#projet 2048

#Permet la création de l'interface graphique
import tkinter as tk
#Permet de générer des nombres aléatoires
import random
#Permet d'importer la classe messagebox du module tkinter
from tkinter import messagebox

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
        # La variable 'col' représente l'indice de la colonne variant de 0 à 3
        for col in range(4):
            # Dimensions des boutons, ils font tous une largeur de 10 et une hauteur de 5
            rectangle = tk.Button(racine, text="", width=10, height=5, font=("helvatica",17))
            # Le bouton est ensuite positionné dans la grille en utilisant les coordonnées de la ligne et de la colonne actuelles
            rectangle.grid(row=i, column=col)
            # Les boutons sont stockés dans la liste appellée 'rectangles'
            rectangles_ligne.append(rectangle)
        rectangles.append(rectangles_ligne)
        
    #Permet de placer le widget "score_affichage" dans la fenêtre graphique avec les coordonnées renseignés
    #Columnspan permet d'étendre ce widget sur deux colonnes afin de le centrer dans la fenêtre 
    score_affichage.grid(row=6, column=1, columnspan=2)
    
    #Création des 4 boutons qui permettent le déplacement des tuiles 
    bouton_left.grid(row=2, column=5)
    bouton_right.grid(row=2, column=7)
    bouton_down.grid(row=2, column=9)
    bouton_up.grid(row=2, column=11)
    
    #Création du bouton permettant de générer une nouvelle partie du jeux 2048
    button_rejouer = tk.Button(racine, text="Nouvelle partie", command=recommencer_partie)
    button_rejouer.grid(row=1, column=5)
    
    #Création du bouton permettant de quitter/finir la partie en cours. Cela affiche un message avec le score de la partie finie 
    bouton_quitter = tk.Button(racine, text="Quitter", command=quitter_partie)
    bouton_quitter.grid(row=1, column=7)
    
    #Création du bouton permettant de sauvegarder la partie en cours dans un fichier
    button_sauvegarde = tk.Button(racine, text="Sauvegarder", command=sauvegarder_partie)
    button_sauvegarde.grid(row=1, column=9)
    
    #Création du bouton permettant de continuer une partie qui a été sauvegarder dans un fichier
    button_continuer = tk.Button(racine, text="Continuer", command=continuer_partie)
    button_continuer.grid(row=1, column=11)
    
    aléatoire_départ()
    maj_score()

        
#Création d'une fonction permettant de remplir de façon aléatoires deux tuiles de la grille avec 2 chiffres définit avec la fonction debut_chiffre        
def aléatoire_départ():
    global grille, score
    #Définir aléatoirement dans la grille 2 tuiles pour y placer les 2 chiffres définit avec la fonction debut_chiffre
    indices = random.sample(range(16), 2)
    for i in indices:
        #Valeur correspondant à l'indice de la ligne où l'on va placer le prmeier chiffre aléatoire
        row = i // 4
        #Valeur correspondant à l'indice de la colonne où l'on va placer le second chiffre aléatoire
        col = i % 4
        #Détermination de nombre aléatoires grâce à la fonction debut_chiffre
        random_number = debut_chiffre()
        #Permet d'ajouter le nombre aléatoire généré par la fonction debut_chiffre() dans la grille aux indices ci-dessus
        grille[row][col] = random_number
        #Permet de mettre à jour le score suite à l'ajout du nombre aléatoire dans la grille
        score += random_number
        rectangles[row][col].config(text=str(grille[row][col]))

        
#Création d'une fonction permettant de générer un nombre aléatoire, soit 2 ou 4
#Sachant que le chiffre 2 a 9 fois plus de chance d'apparaitre que le chiffre 4
def debut_chiffre():
    #Générer un chiffre aléatoire entre 0 et 9 inclus 
    chiffre_aleatoire = random.randint(0, 9)
    #Si le nombre aléatoirement généré est inferieur ou égal à 8, le chiffre 2 est retourné 
    if chiffre_aleatoire <= 8:
        return 2
    #Dans le cas contraire, c'est le chiffre 4 qui est retourné
    else:
        return 4
    
#Création d'un widget qui affiche le score en tant réel du joueur    
score_affichage = tk.Label(racine, text=f"Score = {score}")

#Création d'une fonction qui permet de faire bouger les tuiles vers le haut
def move_up():
    global grille, score
    moved = False
    #Parcourt chaque colonne de la grille
    for col in range(4):
        #Pour chaque colonne, parcourt aussi chaque ligne de la deuxième à la dernière
        for row in range(1, 4):
            if grille[row][col] != 0:
                r = row
                while r > 0 and grille[r-1][col] == 0:
                    grille[r-1][col] = grille[r][col]
                    grille[r][col] = 0
                    r -= 1
                    moved = True
                if r > 0 and grille[r-1][col] == grille[r][col]:
                    grille[r-1][col] *= 2
                    score += grille[r-1][col]
                    grille[r][col] = 0
                    moved = True
    #Si au moins une case a fusionné, les fonctions suivantes sont appellées                
    if moved:
        aléatoire_chiffre()
        maj_score()
        update_grid()
        verifier_fin_de_jeu_ou_pas(grille)
        verifie_gagne_ou_pas()

def aléatoire_chiffre():
    global grille
    #Permet de trouver tous les emplacements vides dans la grille, c'est-à-dire les tuiles où il y a un 0
    empty_cells = []
    for row in range(4):
        for col in range(4):
            if grille[row][col] == 0:
                empty_cells.append((row, col))
    if empty_cells:
        #Permet de choisir un emplacement vide aléatoire et mettre un chiffre 2 ou 4
        row, col = random.choice(empty_cells)
        grille[row][col] = debut_chiffre()
              
def update_grid():
    #Permet de mettre à jour l'affichage de la grille avec les nouvelles valeurs de la grille
    for i in range(4):
        for col in range(4):
            if grille[i][col] == 0:
                rectangles[i][col].config(text="")
                rectangles[i][col].config(bg="grey")
            else:
                rectangles[i][col].config(text=str(grille[i][col]))
                if grille[i][col] == 2:
                    rectangles[i][col].config(bg="bisque")
                elif grille[i][col] == 4:
                    rectangles[i][col].config(bg="wheat")
                elif grille[i][col] == 8:
                    rectangles[i][col].config(bg="sandybrown")
                elif grille[i][col] == 16:
                    rectangles[i][col].config(bg="salmon")
                elif grille[i][col] == 32:
                    rectangles[i][col].config(bg="coral")
                elif grille[i][col] == 64:
                    rectangles[i][col].config(bg="orangered")
                elif grille[i][col] == 128:
                    rectangles[i][col].config(bg="gold")
                elif grille[i][col] == 256:
                    rectangles[i][col].config(bg="yellow")
                elif grille[i][col] == 512:
                    rectangles[i][col].config(bg="khaki")
                elif grille[i][col] == 1024:
                    rectangles[i][col].config(bg="yellow")
                elif grille[i][col] == 2048:
                    rectangles[i][col].config(bg="gold")
                else:
                    rectangles[i][col].config(bg="white")
                    
#Création d'une fonction qui permet de faire bouger les tuiles vers le bas       
def move_down():
    global grille, score
    moved = False
    for col in range(4):
        for row in range(2, -1, -1):
            if grille[row][col] != 0:
                r = row
                while r < 3 and grille[r+1][col] == 0:
                    grille[r+1][col] = grille[r][col]
                    grille[r][col] = 0
                    r += 1
                    moved = True
                if r < 3 and grille[r+1][col] == grille[r][col]:
                    grille[r+1][col] *= 2
                    score += grille[r+1][col]
                    grille[r][col] = 0
                    moved = True
    if moved:
        aléatoire_chiffre()
        maj_score()
        update_grid()
        verifier_fin_de_jeu_ou_pas(grille)
        verifie_gagne_ou_pas()

            
#Création d'une fonction qui permet de faire bouger les tuiles vers la gauche         
def move_left():
    global grille, score
    moved = False
    for row in range(4):
        for col in range(1, 4):
            if grille[row][col] != 0:
                c = col
                while c > 0 and grille[row][c-1] == 0:
                    grille[row][c-1] = grille[row][c]
                    grille[row][c] = 0
                    c -= 1
                    moved = True
                if c > 0 and grille[row][c-1] == grille[row][c]:
                    grille[row][c-1] *= 2
                    score += grille[row][c-1]
                    grille[row][c] = 0
                    moved = True
    if moved:
        aléatoire_chiffre()
        maj_score()
        update_grid()
        verifier_fin_de_jeu_ou_pas(grille)
        verifie_gagne_ou_pas()


#Création d'une fonction qui permet de faire bouger les tuiles vers le bas       
def move_down():
    global grille, score
    moved = False
    for col in range(4):
        for row in range(2, -1, -1):
            if grille[row][col] != 0:
                r = row
                while r < 3 and grille[r+1][col] == 0:
                    grille[r+1][col] = grille[r][col]
                    grille[r][col] = 0
                    r += 1
                    moved = True
                if r < 3 and grille[r+1][col] == grille[r][col]:
                    grille[r+1][col] *= 2
                    score += grille[r+1][col]
                    grille[r][col] = 0
                    moved = True
    if moved:
        aléatoire_chiffre()
        maj_score()
        update_grid()
        verifier_fin_de_jeu_ou_pas(grille)
        verifie_gagne_ou_pas()

            
#Création d'une fonction qui permet de faire bouger les tuiles vers la gauche         
def move_left():
    global grille, score
    moved = False
    for row in range(4):
        for col in range(1, 4):
            if grille[row][col] != 0:
                c = col
                while c > 0 and grille[row][c-1] == 0:
                    grille[row][c-1] = grille[row][c]
                    grille[row][c] = 0
                    c -= 1
                    moved = True
                if c > 0 and grille[row][c-1] == grille[row][c]:
                    grille[row][c-1] *= 2
                    score += grille[row][c-1]
                    grille[row][c] = 0
                    moved = True
    if moved:
        aléatoire_chiffre()
        maj_score()
        update_grid()
        verifier_fin_de_jeu_ou_pas(grille)
        verifie_gagne_ou_pas()

        
#Création d'une fonction qui permet de faire bouger les tuiles vers la droite
def move_right():
    global grille, score
    moved = False
    for row in range(4):
        for col in range(2, -1, -1):
            if grille[row][col] != 0:
                c = col
                while c < 3 and grille[row][c+1] == 0:
                    grille[row][c+1] = grille[row][c]
                    grille[row][c] = 0
                    c += 1
                    moved = True
                if c < 3 and grille[row][c+1] == grille[row][c]:
                    grille[row][c+1] *= 2
                    score += grille[row][c+1]
                    grille[row][c] = 0
                    moved = True
    if moved:
        aléatoire_chiffre()
        maj_score()
        update_grid()
        verifier_fin_de_jeu_ou_pas(grille)
        verifie_gagne_ou_pas()


#Création d'une fonction qui vérifie si le joueur peut encore faire bouger les tuiles 
def verifier_fin_de_jeu_ou_pas(grille):
    # Vérifie s'il est possible de déplacer une case horizontalement ou verticalement
    for row in range(4):
        for col in range(4):
            # Vérifie s'il reste des cases vides dans la grille
            if grille[row][col] == 0:
                return False
            # Vérifie s'il est possible de fusionner deux cases adjacentes horizontalement ou verticalement
            elif (col < 3 and grille[row][col] == grille[row][col+1]) or (row < 3 and grille[row][col] == grille[row+1][col]) or (col > 0 and grille[row][col] == grille[row][col-1]) or (row > 0 and grille[row][col] == grille[row-1][col]):
                return False 
    
    
    # Sinon, il reste des cases vides, on peut encore ajouter un chiffre
    messagebox.showinfo("Game Over", "Vous avez perdu, en effet, vous ne pouvez plus bouger les tuiles,  vous êtes invités à appuyer sur le bouton nouvelle partie")    

               
 
#Création d'une fonction qui vérifie si le joueur a reussi à obtenir une tuile avec le nombre 2048 dedans
#Si c'est le cas, un message disant que le joueur a gagné s'affiche
def verifie_gagne_ou_pas():
    global grille 
    if 2048 in grille :
        print("Gagné")

        
#Création d'une fonction qui permet de générer une nouvelle partie de jeux 
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
        
#Création d'une fonction qui permet de quitter la partie et d'afficher le score obtenu au cours de la partie        
def quitter_partie():
    global score
    #Permet de fermer la fenêtre du jeu
    racine.destroy()
    #Affichage d'une phrase indiquant le score obtenu à la suite de cette partie 
    print(f"Vous avez quitté la partie, votre score est actuellement de {score}")
    
#Création d'une fonction qui permet de sauvegarder la partie en cours dans un fichier 
def sauvegarder_partie():
    global grille
    #Permet de créer un objet fichier nommé fic qui permet d'ouvrir le fichier "fichier.txt" 
    fic = open("fichier.txt","w")
    #La boucle for permet de parcourir chaque élément de la grille
    #La valeur de chaque élément est écrite dans le fichier de sauvegarde crée 
    for i in range (4):
        for col in range(4):
            #La fonction str est utilisée pour convertir les valeurs en chaînes de caractères
            #En effet, la méthode write() ne peut écrire que des chaînes de caractères.
            fic.write(str(grille[i][col]))
            print("La partie a été sauvegardée, vous pouvez la continuer à tout moment")
    #Permet de fermer le fichier        
    fic.close()
    
#Création d'une fonction qui permet de continuer une partie qui a été sauvegardée à l'aide de la fonction sauvegarder_partie     
def continuer_partie():
    global grille
    #Permet d'ouvre le fichier qui a été sauvegardé 
    with open("fichier.txt", "r") as f:
        #Permet de lire les valeurs sauvegardées dans le fichier
        grille_data = f.read()
        #Permet de replacer dans la grille de jeu les valeurs du fichier
        for i in range(4):
            for col in range(4):
                grille[i][col] = int(grille_data[i*4+col])
    update_grid()  
    
    
#Création du bouton Jouer qui, lorsqu'il est cliqué, exécute la fonction "debut_2048"
button_play = tk.Button(racine, text="Jouer", fg = 'white', bg = 'orange', font=200, command=debut_2048)
button_play.grid(row=0, column=0)    


#Ajout des differents boutons dans la fenêtre
bouton_left = tk.Button(racine, text="Left", command =move_left)
bouton_right = tk.Button(racine, text="Right", command =move_right)
bouton_down = tk.Button(racine, text="Down", command =move_down)
bouton_up = tk.Button(racine, text="Up", command =move_up)

#Permet de lancer la boucle principale d'événements de la fenêtre graphique
racine.bind('<Up>', lambda event: move_up())
racine.bind('<Down>', lambda event: move_down())
racine.bind('<Left>', lambda event: move_left())
racine.bind('<Right>', lambda event: move_right())
racine.mainloop()
