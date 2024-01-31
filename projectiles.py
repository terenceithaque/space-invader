# Script pour gérer les projectiles que le joueur peut tirer sur les aliens
import pygame

class Projectile(pygame.sprite.Sprite):
    "Projectile"
    def __init__(self, screen,envoyeur, direction=1):
        super().__init__()
        self.screen = screen # Surface sur laquelle le projectile sera dessiné
        self.direction = direction # Direction dans laquelle le projectile se dirigera (1 pour avancer, -1 pour reculer)
        self.image = pygame.image.load("assets/images/fireball.jpg") # Image pour le sprite du projectile

        self.image = pygame.transform.scale(self.image, (10,10)) # On modifie les dimensions de l'image en 10x10

        self.rect = self.image.get_rect() # Rectangle du projectile

        self.x = envoyeur.rect.x # La position x initiale du projectile vaut celle de son envoyeur
        self.y = envoyeur.rect.y # La position y initiale du projectile vaut celle de son envoyeur

        self.rect.x = self.x # Position x actuelle du projectile
        self.rect.y = self.y # Position y actuelle du projectile

    def move(self):
        "Déplacer le projectile sur l'écran"
        if self.direction == 1:
            self.rect.y -= 1

        if self.direction == -1:
            self.rect.y += 1 

    def draw(self):
        "Afficher le projectile à l'écran"
        self.screen.blit(self.image, (self.rect.x, self.rect.y))               