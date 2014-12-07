#-*- coding: utf-8 -*-

import pygame
from projectile import Projectile

#projectile allant en ligne droite

class Projectile1(Projectile):

    vitesse = (0, 0)
    dommage = 3

    image = pygame.Surface((10, 10))
    pygame.draw.circle(image, (255,0,0), (5, 5), 5)

    def __init__(self, position, vecteur):
        Projectile.__init__(self, position, vecteur)
        self.posx, self.posy = (float(position[0]), float(position[1]))

    def update(self, *args) :

        self.posx += self.vitesse[0] * 2
        self.posy += self.vitesse[1] * 2

        self.rect.x = int(self.posx)
        self.rect.y = int(self.posy)
