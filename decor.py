# Décor d'arrière-plan du jeu
"decor.py contient une classe Decor, qui appelle un fichier image depuis le dossier assets/images afin d'insérer son contenu comme décor pour le jeu."
import pygame
import path

class Decor:
    "Décor du jeu"
    def __init__(self, screen):
        self.screen = screen
        self.width = 900 
        self.height = 900
        self.image = pygame.image.load(path.Path("assets/images/galaxy.jpg")) # Image pour le décor
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 10

    def draw(self):
        "Dessiner le décor à l'écran"
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
