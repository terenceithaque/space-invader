# Décor d'arrière-plan du jeu
import pygame

class Decor:
    "Décor du jeu"
    def __init__(self, screen):
        self.screen = screen
        self.width = 900 
        self.height = 900
        self.image = pygame.image.load("assets/images/galaxy.jpg") # Image pour le décor
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 10

    def draw(self):
        "Dessiner le décor à l'écran"
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
