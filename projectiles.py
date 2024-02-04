# Script pour gérer les projectiles que le joueur peut tirer sur les aliens
import pygame

class Projectile(pygame.sprite.Sprite):
    "Projectile"
    def __init__(self, screen,envoyeur,cible, direction=1):
        super().__init__()
        self.screen = screen # Surface sur laquelle le projectile sera dessiné
        self.direction = direction # Direction dans laquelle le projectile se dirigera (1 pour avancer, -1 pour reculer)
        self.image = pygame.image.load("assets/images/fireball.jpg") # Image pour le sprite du projectile

        self.image = pygame.transform.scale(self.image, (10,10)) # On modifie les dimensions de l'image en 10x10

        self.rect = self.image.get_rect() # Rectangle du projectile

        self.x = envoyeur.rect.x # La position x initiale du projectile vaut celle de son envoyeur
        self.y = envoyeur.rect.y # La position y initiale du projectile vaut celle de son envoyeur

        self.rect.x = self.x # Position x actuelle du projectile
        self.rect.y = self.y # Position y actuelle du projectile

        self.cible = cible # Cible du projectile
        #self.cible_detruite = False # Variable pour indiquer que la cible est détruite ou non

    def move(self):
        "Déplacer le projectile sur l'écran"
        if self.direction == 1:
            self.rect.y -= 1

        if self.direction == -1:
            self.rect.y += 1

    def detruire_cible(self):
        "Détruire la cible quand le projectile la touche"

        if isinstance(self.cible, pygame.sprite.Group): # Si la cible est un groupe d'ennemis
             for cible in self.cible: # On considère que tout membre du groupe est une cible
                  if self.rect.colliderect(cible.rect): # Si le projectile entre en collision avec la cible
                       print("Le projectile est entré en collision avec la cible")
                       cible.kill()
                       print("Cible détruite")
                       self.kill() # On détruit le projectile une fois qu'il a touché la cible
                  
        else: # Sinon, si la cible est un sprite unique, on considère qu'il s'agit du joueur
            if self.rect.colliderect(self.cible.rect):
                print("Le projectile est en collision avec la cible")
                self.cible.vies -=5 # On réduit le nombre de vies du joueur de 1
                print("Cible détruite !")
                #self.cible_detruite = True
                self.kill()


    def draw(self):
        "Afficher le projectile à l'écran"
        self.screen.blit(self.image, (self.rect.x, self.rect.y))               