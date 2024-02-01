# Aliens du jeu
import pygame
import random

class Alien(pygame.sprite.Sprite):
    "Alien qui doit être éliminé par le joueur"
    def __init__(self, screen, group):
        super().__init__() # On hérite des attributs de la classe Sprite
        self.screen = screen # Surface sur laquelle l'alien sera dessiné
        self.image = pygame.image.load("assets/images/alien.jpg") # Image pour représenter le sprite de l'alien
        self.image = pygame.transform.scale(self.image, (30, 30)) # On modifie la taille de l'image en 30x30

        self.x = random.randint(15, 500) # Position x de départ de l'alien
        self.y = 50 # Position y de départ de l'alien
        for alien in group: # Pour chaque autre alien appartenant au même groupe que l'alien que nous créons
            self.x = alien.x + 40

        self.rect = self.image.get_rect() # Rectangle de l'alien
        self.rect.x = self.x # Position x actuelle de l'alien. Au départ, elle vaut self.x
        self.rect.y = self.y # Position y actuelle de l'alien. Au départ, elle vaut self.y

        self.vitesse = random.uniform(0.60, 1) # Vitesse de déplacement de l'alien

    def move(self):
        "Déplacer l'alien"
        self.rect.y += self.vitesse

    def is_out(self):
        "Vérifier si l'alien sort des bordures de l'écran"
        return self.rect.y > 700        

    def draw(self):
        "Afficher l'alien à l'écran"
        self.screen.blit(self.image, (self.rect.x, self.rect.y))   # Dessiner l'image de l'alien à l'écran