"save.py permet de sauvegarder l'état d'une partie en cours"
import json # Importer le module json pour gérer les données de sauvegarde
import os
from tkinter import messagebox # Importer le module messagebox de tkinter pour créer des boîtes de dialogue
import pygame
import path

pygame.init()


class InvalidPseudoException(Exception):
    "Exception en cas de pseudo du joueur invalide pour la sauvegarde (par exemple, si le pseudo est rien ou 'Joueur anonyme')"
    def __init__(self, message="Votre pseudo est invalide pour sauvegarder. \n Cette erreur peut arriver si vous avez choisi 'Joueur anonyme' comme pseudo"):
        "Constructeur de l'exception"
        self.message = message # Message d'erreur de l'exception
        messagebox.showerror("Pseudo invalide pour sauvegarder", self.message) # Afficher le message d'erreur sous forme de boîte de dialogue

    def __str__(self):
        return self.message



def sauvegarder(joueur):
    "Sauvegarder l'état du jeu en cours"
    pseudo_joueur = joueur.pseudo # Pseudo du joueur   
    joueur_rect_x = joueur.rect.x # Position en x actuelle du joueur
    joueur_rect_y = joueur.rect.y # Position en y actuelle du joueur
    munitions_joueur = joueur.munitions # Munitions restantes au joueur
    vies_max_joueur = joueur.vies_max # Nombre maximum de vies du joueur
    vies_joueur = joueur.vies # Points de vie actuels du joueur
    score_joueur = joueur.score

        
        
        
    dossier_joueur = path.Path(f"joueurs/{pseudo_joueur}") # Dossier du joueur
    save_file = "save.json" # Fichier de sauvegarde
    save_file = path.Path(os.path.abspath(os.path.join(dossier_joueur, save_file)))
    print("Chemin du fichier de sauvegarde :", save_file)
    donnees_a_sauvegarder = {
            "pseudo":pseudo_joueur,
            "rect_x":joueur_rect_x,
            "rect_y":joueur_rect_y,
            "munitions":munitions_joueur,
            "vies_max":vies_max_joueur,
            "vies":vies_joueur,
            "score":score_joueur
        } # Données à sauvegarder dans le fichier JSON de sauvegarde
    
    with open(save_file, "w") as f: # Ouvrir le fichier de sauvegarde en écriture
        json.dump(donnees_a_sauvegarder, f) # Ecrire les données dans le fichier JSON
        f.close() # Fermer le fichier JSON
            




        
        
        


def ask_save(key, joueur): 
        "Demander au joueur s'il souhaite sauvegarder"    

        if key[pygame.K_s]:  # Si le joueur a appuyé sur la touche s du clavier

            if joueur.pseudo == "Joueur anonyme": # Si le pseudo du joueur est 'Joueur anonyme'
                InvalidPseudoException() # Enclencher une erreur de pseudo invalide
                return
            
            try: 
                # Demander au joueur s'il souhaite sauvegarder
                save = messagebox.askquestion("Voulez-vous sauvegarder ?", "Souhaitez-vous sauvegarder la partie ? Vous pourrez ainsi reprendre votre jeu dans le même état plus tard.")

                if save == "yes": # Si le joueur veut sauvegarder
                    sauvegarder(joueur) # Sauvegarder la partie

                else: # Si le joueur ne veut pas sauvegarder
                    return    

            except Exception as e: # En cas d'erreur
                print(f"Une erreur s'est produite. Le message est {str(e)}") 
                return # Arrêter la fonction ici   
            


def sauvegarde_presente(pseudo_joueur):
    "Vérifier si le joueur possède une sauvegarde, et retourne le chemin du fichier de sauvegarde si c'est le cas"
    dossier_joueur = f"joueurs/{pseudo_joueur}"
    if os.path.exists(os.path.abspath(dossier_joueur)): # Si le dossier du joueur existe
        print("Vérification de l'existence d'une sauvegarde...")
        if "save.json" in os.listdir(dossier_joueur): # Si le fichier save.json est présent
            # Fichier de sauvegarde 
            save_file = os.path.join(dossier_joueur, "save.json")
            save_file = os.path.abspath(save_file)
            print("Chemin du fichier de sauvegarder chargé:", save_file)
            return save_file # Retourner le chemin du fichier de sauvegarde
        
       


def load_save(pseudo_joueur):
    "Charger les données d'une sauvegarde"
    dossier_joueur = os.path.abspath(f"joueurs/{pseudo_joueur}") # Dossier du joueur pour lequel on veut charger la sauvegarde
    if os.path.exists(dossier_joueur): # Si le dossier du joueur existe
        if os.path.isfile(os.path.join(dossier_joueur, "save.json")): # Si une sauvegarde est présente
            # Fichier de sauvegarde
            save_file = os.path.abspath(os.path.join(dossier_joueur, "save.json"))

            with open(save_file, "r") as f: # Ouvrir le fichier de sauvegarde en lecture
                donnees = json.load(f) # Charger les données en mémoire
                f.close() # Fermer le fichier de sauvegarde
                return donnees # Retourner les données de sauvegarde
            

    else:
        return None       
            




        
    
