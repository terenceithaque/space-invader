# Script contenant le corps du jeu
"jeu.py contient toutes les données relatives au démarrage d'une nouvelle partie"
import pygame # Importation du module pygame pour gérer le jeu
#pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
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
        init_player_mixer() # Initialiser pygame.mixer pour le joueur
        init_alien_mixer() # Initialiser pygame.mixer pour les aliens
        self.pause = False # Variable pour savoir si le jeu est en pause ou non
        

    def quitter(self):
        "Demander au joueur s'il souhaite quitter le jeu"
        quit = messagebox.askquestion("Voulez-vous quitter le jeu ?", "Cliquez sur 'Oui' pour confirmer la fin de partie.") # Demander au joueur s'il souhaite quitter le jeu
        return quit
    
    def mettre_pause(self):
             "Mettre le jeu en pause"
             
             if not self.pause:
                 self.pause = True # On passe le jeu en pause
                 message_pause = pygame.font.Font(None, 36)
                 message = "Jeu en pause (P pour reprendre)"
                 affichage = message_pause.render(message, True, (255,255,255))
                 self.screen.blit(affichage, (10, 100))
                 pygame.display.flip()

             else:
                 self.pause = False 
                 self.screen.fill((0,0,0))

    



    def executer(self):
        "Exécuter la boucle de jeu"
        
        
                       


        decor = Decor(self.screen) # Ajouter un décor au jeu
        joueur = Joueur(self.screen) # On crée un nouveau joueur
        aliens = pygame.sprite.Group() # Groupe pour gérer tous les aliens présents à l'écran
        projectiles = pygame.sprite.Group() # Groupe pour les projectiles tirés par le joueur
        degats_aliens_supp = 0 # Dégâts supplémentaires infligés par les aliens
        for i in range(5): # On ajoute 5 aliens au groupe
            aliens.add(Alien(self.screen, aliens, joueur, degats_aliens_supp))
        execution = True # Variable pour tenir compte de l'état de l'exécution du jeu
        

        projectile_tire = pygame.USEREVENT + 1 # Evènement pour gérer le tir de projectiles par le joueur
        alien_spawn = pygame.USEREVENT+ 2 # Evènement pour gérer l'apparition des aliens
        alien_move = pygame.USEREVENT + 4 # Evènement pour gérer le déplacement des aliens
        alien_shot = pygame.USEREVENT + 5 # Evènement pour gérer les tirs de projectiles par les aliens contre le joueur
        regeneration_vies_joueur = pygame.USEREVENT + 6 # Evènement pour gérer la régénération des points de vie du joueur
        vie_joueur_faible = pygame.USEREVENT + 7 # Evènement qui se déroule quand la vie du joueur est faible
        pause = pygame.USEREVENT + 8 # Evènement pour la mise en pause du jeu
        pygame.time.set_timer(projectile_tire, 100)
        pygame.time.set_timer(alien_spawn, 10000)
        pygame.time.set_timer(joueur.recharge, 10000)
        pygame.time.set_timer(alien_move, 100)
        pygame.time.set_timer(alien_shot, 3000)
        pygame.time.set_timer(regeneration_vies_joueur, 15000)
        pygame.time.set_timer(pause, 100)
        n_alien_spawn = 1 # Nombre d'aliens à faire apparaître à chaque vague
        alerte_vie_faible =  pygame.mixer.Sound("assets/sons/vie_faible.mp3") # Son à déclencher quand la vie du joueur est faible


        

        
        
        while execution: # Tant que le jeu est en cours d'exécution

            if not self.pause:
                 self.screen.fill((0,0,0))
            
            
            
            if joueur.vies <=20:
                 pygame.event.post(pygame.event.Event(vie_joueur_faible))
            
            
            keys = pygame.key.get_pressed() # On obtient toutes les touches pressées par le joueur

            

              

            for event in pygame.event.get(): # Pour chaque évènement intercepté durant la boucle de jeu
                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]: # Si le joueur a cliqué sur l'icône de fermeture de la fenêtre ou s'il a appuyé sur la touche échap. du clavier
                    if self.quitter() == "yes": # Si le joueur confirme qu'il veut quitter le jeu
                        execution = False # On met execution sur False, de manière à arrêter la boucle de jeu 


                if event.type == alien_spawn: # Si une apparition d'aliens a lieu
                            for i in range(n_alien_spawn):
                                if not self.pause:
                                    aliens.add(Alien(self.screen, aliens, joueur, degats_aliens_supp)) # On ajoute un nouvel alien au groupe

                            n_alien_spawn += 1         

                if event.type == projectile_tire: # Si le joueur tire un projectile
                        #for alien in aliens:
                            if not self.pause:
                                joueur.tirer_projectile(keys, projectiles,cible=aliens)


                if event.type == alien_shot: # Si un alien tire un projectile
                     if not self.pause:
                        for alien in aliens:
                          alien.tirer_projectile(projectiles, cible=joueur)            

                if event.type == joueur.recharge and  joueur.doit_recharger: # Si on doit recharger les munitions
                     if not self.pause:
                        joueur.recharger_munitions()

                if event.type == alien_move: # Si il y a un évènement "déplacement des aliens"
                     if not self.pause:
                        for alien in aliens: # Pour chaque sprite représentant un alien
                          alien.move()   # On déplace le sprite 

                if event.type == vie_joueur_faible and joueur.vies <= 20: # Si le nombre de vies restantes au joueur est faible
                        if not self.pause:
                            print("Vie du joueur inférieure ou égale à 20 PV")
                            joueur.afficher_vie_faible() # Afficher un message de vie faible au joueur
                            channel = alerte_vie_faible.play(-1)

                        else:
                             channel = alerte_vie_faible.stop()

                if event.type == pause and keys[pygame.K_p]: # Si le joueur presse la touche P

                    self.mettre_pause() # On met le jeu en pause
                

                if joueur.vies > 20: # Si le nombre de vies restantes au joueur dépasse 20
                     alerte_vie_faible.stop()  # On arrête l'alerte

                if event.type == regeneration_vies_joueur: # Si il y un évènement "régénération des vies du joueur"
                     if not self.pause:
                        joueur.regenerer_vies() # On regénère les points de vie du joueur                  
                        
                  
                                      
            if not self.pause:
                joueur.move(keys) # Permettre au joueur de déplacer son sprite
                
                

                if joueur.last_kills >= 20: # Si le joueur a tué 20 aliens récemment
                     print("20 aliens tués récemment")
                     degats_aliens_supp += 5
                     for alien in aliens:
                        if alien.attaque == 5:
                            alien.attaque += degats_aliens_supp
                        print("Attaque des aliens :", alien.attaque)
                     joueur.last_kills = 0 # On remet à 0 le nombre de kills récents 
           
           
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

            

              

            if joueur.vies <= 0: # Si le joueur a perdu toutes ses vies
                joueur.game_over() # Afficher le message de fin de partie
                pygame.display.flip() # Mettre à jour l'affichage
                pygame.time.wait(5000) # Attendre 5 secondes
                execution = False # Quitter le jeu


            joueur.sauvegarder_score() # On sauvegarde le meilleur score du joueur    

            if joueur.vies > 0: # S'il reste encore des vies au joueur
                pygame.display.flip() # Mettre à jour l'affichage du jeu            

