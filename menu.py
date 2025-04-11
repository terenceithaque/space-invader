"""Menu du jeu"""
import pygame
import pygame_menu
pygame.init()
from decor import *
from jeu import *
from joueur import *


window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
decor = Decor(window)

def creer():
    "Crée le menu de jeu"
    menu = pygame_menu.Menu("Bienvenue !", 800, 600)

    menu.add.button(title="Jouer", action=Jeu().executer)



display = True

while display:
    pygame.display.flip()
