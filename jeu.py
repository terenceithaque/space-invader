# Script contenant le corps du jeu
import pygame # Importation du module pygame pour gérer le jeu
from tkinter import messagebox

class Jeu:
    "Corps du jeu"
    def __init__(self):
        self.screen_width_height = (800, 600) # Tuple pour contenir les valeurs de la taille de l'écran, en largeur et en hauteur
        self.screen = pygame.display.set_mode((self.screen_width_height)) # On crée une nouvelle fenêtre de jeu à l'aide des valeurs contenues dans le tuple
        pygame.display.set_caption("Space Invader") # Titre de la fenêtre de jeu

    def quitter(self):
        "Demander au joueur s'il souhaite quitter le jeu"
        quit = messagebox.askquestion("Voulez-vous quitter le jeu ?", "Cliquez sur 'Oui' pour confirmer la fin de partie.") # Demander au joueur s'il souhaite quitter le jeu
        return quit


    def executer(self):
        "Exécuter la boucle de jeu"
        execution = True # Variable pour tenir compte de l'état de l'exécution du jeu

        while execution: # Tant que le jeu est en cours d'exécution
            for event in pygame.event.get(): # Pour chaque évènement intercepté durant la boucle de jeu
                if event.type == pygame.QUIT: # Si le joueur a cliqué sur l'icône de fermeture de la fenêtre
                    if self.quitter() == "yes": # Si le joueur confirme qu'il veut quitter le jeu
                        execution = False # On met execution sur False, de manière à arrêter la boucle de jeu    

