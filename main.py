# Script de lancement du jeu
"Il s'agit du script de démarrage du jeu. Lorsqu'il est exécuté, il importe la classe Jeu depuis jeu.py, l'initalise puis l'exécute afin de démarrer une nouvelle partie."
import pygame # Importation de pygame
from jeu import * # Importation du script gérant le corps du jeu
pygame.init() # Initialisation de pygame
pygame.display.init()

if __name__ == "__main__": # Si le programme s'exécute
    jeu = Jeu() # On démarre une nouvelle partie
    jeu.executer()
