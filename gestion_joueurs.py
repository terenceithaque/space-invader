# Gérer les différents joueurs du jeu
"gestion_joueurs.py permet de gérer les différents joueurs du jeu de manière indépendante"
import os # On importe les fonctionnalités du système d'exploitation afin de pouvoir accéder à différentes fonctionnalités pour le dossier "joueurs"
import platform
from tkinter import messagebox

def joueurs_existants():
    "Trouver un joueur un existant. Pour cela, on se base sur une liste de dossier présents dans le dossier joueur, chacun d'entre eux représentant un profil de joueur indépendant des autres"
    return os.listdir("joueurs") # On retourne tous les dossiers présents dans le dossier "joueurs", en considérant que chacun de ces dossiers représente un joueur


def supprimer_caracteres_interdits(pseudo, replace_car="_"):
    "Retirer les caractères interdits d'un pseudo selon le système d'exploitation et retourner le pseudo sans ces caractères"
    if platform.system() == "Windows": # Si le système d'exploitation est Windows
        caracteres_interdits = ["<", ">", ":", '"', "/", "'\'","|", "?", "*"] # Liste des caractères interdits dans un nom de fichier ou de dossier pour Windows

    elif platform.system() == "Darwin": # Si le système d'exploitation est macOS
        caracteres_interdits = [":", "/", "\\"] # Liste des caractères interdits dans un nom de fichier ou de dossier pour macOS

    elif platform.system() == "Linux": # Si le système d'exploitation est basé sur Linux
        caracteres_interdits = ["/"] # Liste des caractères interdits dans un nom de fichier ou de dossier pour les systèmes Linux

    if any(car in pseudo for car in caracteres_interdits): # Si un ou plusieurs caractères interdits sont détectés dans le pseudo
        # Informer le joueur que son pseudo contient des caractères interdits
        messagebox.showinfo("Caractères interdits détectés", f"Le pseudo que vous avez saisi contient des caractères interdits. Durant la partie, ces caractères seront remplacés par un {replace_car}.")


    for car in caracteres_interdits: # Pour chaque caractère interdit selon le système d'exploitation
        if car in pseudo: # Si le caractère interdit est présent dans le pseudo
            pseudo = pseudo.replace(car, replace_car) # Remplacer le caractère interdit par le caractère de remplacement indiqué

    return pseudo # Retourner le pseudo sans les caractères interdits               

def creer_dossier(pseudo_du_joueur):
    "Créer un dossier pour un nouveau joueur. Ce dossier sera intitulé selon son pseudo"
    pseudo_du_joueur = supprimer_caracteres_interdits(pseudo=pseudo_du_joueur, replace_car="_") # Supprimer les caractères interdits contenus dans le pseudo et les remplacer par un autre caractère
    chemin_dossier = os.path.join("joueurs", pseudo_du_joueur) # Le chemin du nouveau dossier est composé du nom du dossier parent et du pseudo du joueur
    if not os.path.exists(chemin_dossier):
        os.mkdir(chemin_dossier)


def supprimer_dossier(pseudo_du_joueur):
    "Supprimer un dossier spécifique dans le dossier 'joueurs'"
    if pseudo_du_joueur in joueurs_existants():
        chemin_dossier = os.path.join(f"joueurs/{pseudo_du_joueur}")
        if os.listdir("joueurs") != []:
            for file in os.listdir(chemin_dossier):
                os.remove(os.path.join(f"{chemin_dossier}/{file}"))
            os.rmdir(f"joueurs/{pseudo_du_joueur}")
            print(f"Supprimé {pseudo_du_joueur}")                