Empêchez les aliens d'envahir votre planète !

Aux commandes d'un vaisseau, vous devez détruire le plus de vaisseaux ennemis possible afin d'engranger des points. Faites toutefois attention à vos munitions et à vos vies, car elles sont toutes les deux limitées et en manquer à un moment pourrait vous être préjudiciable.

En début de partie, il vous sera demandé de saisir un pseudo afin de retrouver vos scores à la prochaine partie. Si vous décidez d'ignorer cette étape, ils ne seront stockés que temporairement.

Le jeu est découpé en 7 scripts différents, chacun ayant un rôle particulier. Les voici:
    - main.py : démarre une nouvelle partie à la demande
    - jeu.py : contient la logique du jeu (boucle principale, notamment)
    -gestion_joueurs.py : crée des dossiers de joueurs afin de sauvegarder les scores séparément, liste les dossiers existants, et en supprime au besoin

    Enfin, viennent les scripts gérant chaque objet du jeu:
        - joueur.py : crée un nouveau joueur (en définissant les méthodes correspondantes et en chargeant le sprite)
        - alien.py : crée un nouvel ennemi que le joueur doit éliminer afin d'engranger des points
        - projectiles.py : crée un nouveau projectile ayant une direction, un envoyeur et une ciblé déterminés.
        - decor.py : charge un fichier image afin de placer son contenu en tant que décor du jeu

Une grande partie de ce jeu utilise la bibliothèque pygame pour Python. Si vous souhaitez en savoir plus sur cette bibliothèque, rendez vous sur https://www.pygame.org