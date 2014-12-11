#-*- coding: utf-8 -*-

import pygame
from projectile import Projectile
import math

#projectile suivant une courbe sinusoidale

class ProjectileSinus(Projectile):

    dommage = 1
    multi   = 3

    def __init__(self, position, vecteur):
        super(ProjectileSinus, self).__init__(position, vecteur)
        self.posx, self.posy = (float(position[0]), float(position[1]))
        
    def update(self, *args) :
      
        self.posx += self.vitesse[0] * self.multi
        self.posy += self.vitesse[1] * self.multi + 2*math.sin(0.005*pygame.time.get_ticks()) #depend du temps
	
        self.rect.x = int(self.posx)
        self.rect.y = int(self.posy)
