#-*- coding: utf-8 -*-

import pygame
from projectile import Projectile

#projectile allant en ligne droite

class ProjectileDroit(Projectile):

    dommage = 3
    multi   = 3

    def __init__(self, position, vecteur):
        super(ProjectileDroit, self).__init__(position, vecteur)
        self.posx, self.posy = (float(position[0]), float(position[1]))

    def update(self, *args) :

        self.posx += self.vitesse[0] * self.multi
        self.posy += self.vitesse[1] * self.multi

        self.rect.x = int(self.posx)
        self.rect.y = int(self.posy)
