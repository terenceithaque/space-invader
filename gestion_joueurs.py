# Gérer les différents joueurs du jeu
"gestion_joueurs.py permet de gérer les différents joueurs du jeu de manière indépendante"
import os # On importe les fonctionnalités du système d'exploitation afin de pouvoir accéder à différentes fonctionnalités pour le dossier "joueurs"

def joueurs_existants():
    "Trouver un joueur un existant. Pour cela, on se base sur une liste de dossier présents dans le dossier joueur, chacun d'entre eux représentant un profil de joueur indépendant des autres"
    return os.listdir("joueurs") # On retourne tous les dossiers présents dans le dossier "joueurs", en considérant que chacun de ces dossiers représente un joueur

def creer_dossier(pseudo_du_joueur):
    "Créer un dossier pour un nouveau joueur. Ce dossier sera intitulé selon son pseudo"
    chemin_dossier = os.path.join("joueurs", pseudo_du_joueur) # Le chemin du nouveau dossier est composé du nom du dossier parent et du pseudo du joueur
    if not os.path.exists(chemin_dossier):
        os.mkdir(chemin_dossier)


def supprimer_dossier(pseudo_du_joueur):
    "Supprimer un dossier spécifique dans le dossier 'joueurs'"
    chemin_dossier = os.path.join(f"joueurs/{pseudo_du_joueur}")
    if os.listdir("joueurs") != []:
        for file in os.listdir(f"joueurs/{pseudo_du_joueur}"):
            os.remove(os.path.join(f"{chemin_dossier}/{file}"))
        os.rmdir(f"joueurs/{pseudo_du_joueur}")
        print(f"Supprimé {pseudo_du_joueur}")                