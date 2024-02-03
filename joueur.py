# Script du joueur
import pygame
from projectiles import *

class Joueur(pygame.sprite.Sprite):
    "Joueur"
    def __init__(self, screen):
        super().__init__() # On hérite des attributs de la classe Sprite de pygame.sprite
        self.screen = screen # Surface sur laquelle le joueur sera dessiné
        self.image = pygame.image.load("assets/images/ship.jpg") # Image pour le sprite du joueur
        self.image = pygame.transform.scale(self.image, (30, 30)) # On modifie la taille de l'image en 30x30

        self.x = 370 # Position x de départ du joueur
        self.y = 550 # Position y de départ du joueur
        
            

        self.rect = self.image.get_rect() # Rectangle du joueur

        self.rect.x = self.x # Position x actuelle du joueur. Au début de la partie, elle vaut self.x
        self.rect.y = self.y # Position y actuelle du joueur. Au début de la partie, elle vaut self.y
        

        self.munitions = 10 # Nombre de munitions dont le joueur dispose pour tirer sur les aliens
        self.font_muntions = pygame.font.Font(None, 36) # Police pour afficher le nombre de munitions restantes à l'écran
        self.recharge = pygame.USEREVENT + 3 # Evènement pour gérer la recharge des munitions
        self.doit_recharger = False # Variable pour vérifier si la recharge des munitions doit être faite ou est en cours

    def move(self, key):
        "Déplacer le joueur sur l'écran"
        if key[pygame.K_LEFT]:  # Si le joueur presse la touche "flèche vers la gauche"
            self.rect.x -= 1
            if self.rect.x < 0: # Si le joueur sort de la bordure de la fenêtre
                self.rect.x = 0 # On le replace à l'intérieur de la fenêtre

        if key[pygame.K_RIGHT]: # Si le joueur presse la touche "flèche vers la droite" 
            self.rect.x += 1
            if self.rect.x > 770: # Si le joueur sort de la bordure de la fenêtre
                self.rect.x = 770 # On le replace à l'intérieur de la fenêtre

    def afficher_munitions_restantes(self):
        "Afficher les munitions restantes"
        if self.munitions > 0:
            texte_munitions_restantes = f"Munitions restantes : {self.munitions}"
            munitions_restantes = self.font_muntions.render(texte_munitions_restantes, True, (255, 255, 255))
            self.screen.blit(munitions_restantes, (0,0))

        else:    
            texte_munitions_restantes = f"Vous êtes à court de munitions !"
            munitions_restantes = self.font_muntions.render(texte_munitions_restantes, True, (255, 255, 255))
            self.screen.blit(munitions_restantes, (0,0))


    def recharger_munitions(self):
        "Recharger les munitions du joueur"
        self.munitions = 10
        self.doit_recharger = False # On ne doit plus recharger les munitions      


    def tirer_projectile(self, key, group):
        "Tirer un projectile"
       
        temps_tir = 0 # Temps où le tir de la dernière munition a eu lieu
        if key[pygame.K_SPACE]:  
            if self.munitions > 0: # S'il reste encore des munitions au joueur
                print("Tiré un projectile !")
                group.add(Projectile(self.screen, self, direction = 1))
                self.munitions -= 1 # On réduit le nombre de munitions restantes
                if self.munitions == 0: # S'il ne reste plus de munitions après déduction
                    self.doit_recharger = True # On doit recharger les munitions
                    temps_tir = pygame.time.get_ticks()
                    

            else:
                print("Vous êtes à court de munitions !")

        

                           

    def draw(self):
        "Dessiner le sprite du joueur à l'écran"
        self.screen.blit(self.image, (self.rect.x, self.rect.y))  # Dessiner l'image du joueur sur les positions x et y actuelles de celui-ci
        