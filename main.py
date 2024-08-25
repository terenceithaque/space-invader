# Script de lancement du jeu
"Il s'agit du script de démarrage du jeu. Lorsqu'il est exécuté, il importe la classe Jeu depuis jeu.py, l'initalise puis l'exécute afin de démarrer une nouvelle partie."
import pygame # Importation de pygame
from jeu import * # Importation du script gérant le corps du jeu
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init() # Initialisation de pygame
pygame.display.init()
from tkinter import messagebox

if __name__ == "__main__": # Si le programme s'exécute
    jeu = Jeu() # On démarre une nouvelle partie
    jeu.executer()
    pygame.quit()
    

    del jeu # Supprimer la partie précédente de la mémoire
    #pygame.time.wait(5000) # Attendre pendant 5 secondes
    while True:
        rejouer = messagebox.askyesno("Rejouer ?", "Voulez-vous rejouer ?") # Demander au joueur s'il souhaite rejouer
        if rejouer: # Si le joueur veut rejouer
            pygame.init() # Initialiser pygame à nouveau
            pygame.font.init()
            jeu = Jeu()
            jeu.executer() # Exécuter le jeu à nouveau
            pygame.quit() # Quand le jeu est terminé, quitter pygame
            del jeu

        else: # Sinon
            break # Quitter le jeu  
