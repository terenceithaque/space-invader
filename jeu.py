# Script contenant le corps du jeu
"jeu.py contient toutes les données relatives au démarrage d'une nouvelle partie"
import pygame # Importation du module pygame pour gérer le jeu
pygame.init()
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
        projectiles = pygame.sprite.Group() # Groupe pour les projectiles tirés par le joueur
        for i in range(5): # On ajoute 5 aliens au groupe
            aliens.add(Alien(self.screen, aliens, joueur))
        execution = True # Variable pour tenir compte de l'état de l'exécution du jeu

        projectile_tire = pygame.USEREVENT + 1 # Evènement pour gérer le tir de projectiles par le joueur
        alien_spawn = pygame.USEREVENT+ 2 # Evènement pour gérer l'apparition des aliens
        alien_move = pygame.USEREVENT + 4 # Evènement pour gérer le déplacement des aliens
        alien_shot = pygame.USEREVENT + 5 # Evènement pour gérer les tirs de projectiles par les aliens contre le joueur
        regeneration_vies_joueur = pygame.USEREVENT + 6 # Evènement pour gérer la régénération des points de vie du joueur
        pygame.time.set_timer(projectile_tire, 100)
        pygame.time.set_timer(alien_spawn, 10000)
        pygame.time.set_timer(joueur.recharge, 10000)
        pygame.time.set_timer(alien_move, 100)
        pygame.time.set_timer(alien_shot, 3000)
        pygame.time.set_timer(regeneration_vies_joueur, 15000)
        n_alien_spawn = 1 # Nombre d'aliens à faire apparaître à chaque vague

        while execution: # Tant que le jeu est en cours d'exécution
            
            self.screen.fill((0, 0,0))
            keys = pygame.key.get_pressed() # On obtient toutes les touches pressées par le joueur

            for event in pygame.event.get(): # Pour chaque évènement intercepté durant la boucle de jeu
                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]: # Si le joueur a cliqué sur l'icône de fermeture de la fenêtre ou s'il a appuyé sur la touche échap. du clavier
                    if self.quitter() == "yes": # Si le joueur confirme qu'il veut quitter le jeu
                        execution = False # On met execution sur False, de manière à arrêter la boucle de jeu 


                if event.type == alien_spawn: # Si une apparition d'aliens a lieu
                            for i in range(n_alien_spawn):
                                aliens.add(Alien(self.screen, aliens, joueur)) # On ajoute un nouvel alien au groupe
                            n_alien_spawn += 1         

                if event.type == projectile_tire: # Si le joueur tire un projectile
                        #for alien in aliens:
                            joueur.tirer_projectile(keys, projectiles,cible=aliens)


                if event.type == alien_shot: # Si un alien tire un projectile
                     for alien in aliens:
                          alien.tirer_projectile(projectiles, cible=joueur)            

                if event.type == joueur.recharge and  joueur.doit_recharger: # Si on doit recharger les munitions
                     joueur.recharger_munitions()

                if event.type == alien_move: # Si il y a un évènement "déplacement des aliens"
                     for alien in aliens: # Pour chaque sprite représentant un alien
                          alien.move()   # On déplace le sprite 


                if event.type == regeneration_vies_joueur: # Si il y un évènement "régénération des vies du joueur"
                     joueur.regenerer_vies() # On regénère les points de vie du joueur                  
                        

                                      

            joueur.move(keys) # Permettre au joueur de déplacer son sprite
            decor.draw() # Dessiner le décor à l'écran
            joueur.draw() # Dessiner le sprite du joueur à l'écran 

            for alien in aliens: # Pour chaque alien
                alien.draw() # Dessiner l'alien sur l'écran
                if alien.is_out(): # Si l'alien a dépassé les bordures de l'écran
                    alien.kill() # On détruit le sprite de cet alien
                    
                    
                        

            for projectile in projectiles:
                projectile.move()
                projectile.detruire_cible()
                projectile.draw()

            joueur.afficher_pseudo()
            joueur.afficher_munitions_restantes()

            joueur.afficher_ligne_visee(keys)
            joueur.afficher_vies_restantes()
            joueur.mettre_a_jour_meilleur_score()
            joueur.afficher_score()

            if joueur.vies <= 0:
                joueur.game_over()
                pygame.time.wait(5000)
                execution = False


            joueur.sauvegarder_score() # On sauvegarde le meilleur score du joueur    

            pygame.display.flip() # Mettre à jour l'affichage du jeu            

