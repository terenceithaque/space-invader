# Script de lancement du jeu
import pygame # Importation de pygame
from jeu import * # Importation du script gérant le corps du jeu
pygame.init() # Initialisation de pygame

if __name__ == "__main__": # Si le programme s'exécute
    jeu = Jeu() # On démarre une nouvelle partie
    jeu.executer()
