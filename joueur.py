# Script du joueur
import pygame

class Joueur(pygame.sprite.Sprite):
    "Joueur"
    def __init__(self):
        super().__init__() # On hérite des attributs de la classe Sprite de pygame.sprite