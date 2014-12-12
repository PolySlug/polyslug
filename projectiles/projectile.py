#-*- coding:utf-8-*-

#test de projectiles
import pygame
import math

class Projectile(pygame.sprite.Sprite):

    sprite = None

    vitesse = (0, 0)
    dommage = 10

    '''
    __init__

    Initialise les position, vitesse et sprite du projectile

    @param {tuple} position & vecteur
    '''
    def __init__(self, position, vecteur):

        pygame.sprite.Sprite.__init__(self)

        #On récupère le rectangle de l'image
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = position[0], position[1]

        vx, vy = vecteur

        #On normalise `vecteur` en en vecteur unitaire pour avoir self.vitesse
        norme = math.sqrt(vx*vx + vy*vy)

        if norme == 0 :
            self.vitesse = [2, 2]
        else :
            self.vitesse = [float(vx) / norme, float(vy) / norme]

    '''
    update

    Update la position du projectile grace au tuple vitesse
    Propre à chaque Projectile (différentes trajectoires différentes)
    '''
    def update(self, *args):
        pass

