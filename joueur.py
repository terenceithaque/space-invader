# Script du joueur
import pygame

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

    def draw(self):
        "Dessiner le sprite du joueur à l'écran"
        self.screen.blit(self.image, (self.rect.x, self.rect.y))  # Dessiner l'image du joueur sur les positions x et y actuelles de celui-ci
        