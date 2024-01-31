# Script contenant le corps du jeu
import pygame # Importation du module pygame pour gérer le jeu
from tkinter import messagebox
from joueur import * # On importe le script joueur pour pouvoir gérer le sprite du joueur
from alien import * # On importe le script alien pour pouvoir gérer les ennemis que le joueur doit éliminer
from decor import *


class Jeu:
    "Corps du jeu"
    def __init__(self):
        self.screen_width_height = (800, 600) # Tuple pour contenir les valeurs de la taille de l'écran, en largeur et en hauteur
        self.screen = pygame.display.set_mode((self.screen_width_height)) # On crée une nouvelle fenêtre de jeu à l'aide des valeurs contenues dans le tuple
        pygame.display.set_caption("Space Invaders") # Titre de la fenêtre de jeu
        icone = pygame.image.load("assets/images/alien.jpg") # Icône de la fenêtre du jeu
        pygame.display.set_icon(icone)

    def quitter(self):
        "Demander au joueur s'il souhaite quitter le jeu"
        quit = messagebox.askquestion("Voulez-vous quitter le jeu ?", "Cliquez sur 'Oui' pour confirmer la fin de partie.") # Demander au joueur s'il souhaite quitter le jeu
        return quit


    def executer(self):
        "Exécuter la boucle de jeu"

        decor = Decor(self.screen) # Ajouter un décor au jeu
        joueur = Joueur(self.screen) # On crée un nouveau joueur
        aliens = pygame.sprite.Group() # Groupe pour gérer tous les aliens présents à l'écran
        for i in range(5): # On ajoute 5 aliens au groupe
            aliens.add(Alien(self.screen))
        execution = True # Variable pour tenir compte de l'état de l'exécution du jeu

        while execution: # Tant que le jeu est en cours d'exécution
            self.screen.fill((0, 0,0))
            keys = pygame.key.get_pressed() # On obtient toutes les touches pressées par le joueur

            for event in pygame.event.get(): # Pour chaque évènement intercepté durant la boucle de jeu
                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]: # Si le joueur a cliqué sur l'icône de fermeture de la fenêtre ou s'il a appuyé sur la touche échap. du clavier
                    if self.quitter() == "yes": # Si le joueur confirme qu'il veut quitter le jeu
                        execution = False # On met execution sur False, de manière à arrêter la boucle de jeu    

            joueur.move(keys) # Permettre au joueur de déplacer son sprite
            decor.draw() # Dessiner le décor à l'écran
            joueur.draw() # Dessiner le sprite du joueur à l'écran
            for alien in aliens: # Pour chaque alien
                alien.move() # Déplacer l'alien sur l'écran
                alien.draw() # Dessiner l'alien sur l'écran
                if alien.is_out(): # Si l'alien a dépassé les bordures de l'écran
                    alien.kill() # On détruit le sprite de cet alien
                    aliens.add(Alien(self.screen)) # On ajoute un nouvel alien au groupe

            

            pygame.display.flip() # Mettre à jour l'affichage du jeu            

