# Aliens du jeu
"""Les aliens sont les ennemis du joueur. Ils sont représentés par une classe Alien, qui hérite elle-même de pygame.sprite.Sprite. Ces aliens peuvent apparaître à des endroits aléatoires sur l'écran et peuvent tirer des projectiles
afin d'abattre le joueur. Quand le joueur touche un alien, ce dernier est détruit, ce qui lui permet de gagner des points."""
import pygame
import random
from projectiles import *
#pygame.init()

pygame.mixer.pre_init(44100, -16, 2, 2048)
def init_alien_mixer():
    pygame.mixer.init()


class Alien(pygame.sprite.Sprite):
    "Alien qui doit être éliminé par le joueur"
    def __init__(self, screen, group, joueur):
        super().__init__() # On hérite des attributs de la classe Sprite
        self.screen = screen # Surface sur laquelle l'alien sera dessiné
        self.image = pygame.image.load("assets/images/alien.jpg") # Image pour représenter le sprite de l'alien
        self.image = pygame.transform.scale(self.image, (30, 30)) # On modifie la taille de l'image en 30x30

        self.x = random.randint(15, 500) # Position x de départ de l'alien
        self.y = 50 # Position y de départ de l'alien
        for alien in group: # Pour chaque autre alien appartenant au même groupe que l'alien que nous créons
            self.x = alien.x + 40

        if self.x > 500:
            self.x = 500    

            
        self.rect = self.image.get_rect() # Rectangle de l'alien
        self.rect.x = self.x # Position x actuelle de l'alien. Au départ, elle vaut self.x
        self.rect.y = self.y # Position y actuelle de l'alien. Au départ, elle vaut self.y

        self.vitesse = random.uniform(0.80, 1) # Vitesse de déplacement de l'alien

    def move(self):
        "Déplacer l'alien"
        self.rect.y += self.vitesse


    def tirer_projectile(self, group, cible):
        "Permettre à l'alien de tirer des projectiles contre le joueur"
        group.add(Projectile(self.screen, self, cible, direction=-1))
        son_tir = pygame.mixer.Sound("assets/sons/tir_projectile.wav") # Son pour le tir du projectile
        channel = son_tir.play() # Jouer le son

        """if channel.get_busy():
            pygame.time.delay(1)"""


        

    def is_out(self):
        "Vérifier si l'alien sort des bordures de l'écran"
        return self.rect.y > 700        

    def draw(self):
        "Afficher l'alien à l'écran"
        self.screen.blit(self.image, (self.rect.x, self.rect.y))   # Dessiner l'image de l'alien à l'écran