"path.py permet de gérer les chemins de fichiers quand le jeu est compilé ou en script"

import sys # Importer sys
import os # Importer os

def Path(filepath:str):
    "Convertit un chemin de fichier pour sys (compilé) ou os (script)"
    if getattr(sys, "frozen", False): # Si on est dans un paquet d'application compilé
        filepath = os.path.join(sys._MEIPASS, filepath) # Chemin de fichier converti pour le programme compilé

    else: # Si on lance le jeu en version script
        filepath = os.path.abspath(filepath)


    return filepath        

    
