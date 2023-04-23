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
            # Dimensions des boutons, ils font tous une largeur de 20 et une hauteur de 10
            rectangle = tk.Button(racine, text="", width=20, height=10, font=("helvatica",17))
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
    #Générer un chiffre aléatoire entre 0 et 10 inclus 
    chiffre_aleatoire = random.randint(0, 10)
    #Si le nombre aléatoirement généré est inferieur ou égal à 9, le chiffre 2 est retourné 
    if chiffre_aleatoire <= 9:
        return 2
    #Dans le cas contraire, c'est le chiffre 4 qui est retourné
    else:
        return 4
    
#Création d'un widget qui affiche le score en tant réel du joueur    
score_affichage = tk.Label(racine, text=f"Score = {score}")


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

    
#Création du bouton Jouer qui, lorsqu'il est cliqué, exécute la fonction "start_2048"
button_play = tk.Button(racine, text="Jouer", command=start_2048)
button_play.grid(row=0, column=0)    
        

#Permet de lancer la boucle principale d'événements de la fenêtre graphique
racine.mainloop()
 
