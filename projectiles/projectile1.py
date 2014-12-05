<<<<<<< HEAD
import pygame
from projectile import Projectile
 
=======
#-*- coding: utf-8 -*-

import pygame
from projectile import Projectile

>>>>>>> origin/master
#projectile allant en ligne droite

class Projectile1(Projectile):

<<<<<<< HEAD
	self.vitesse = (0, 0)
	self.dommage = 3
	self.image = pygame.Surface((10, 10))
	pygame.draw.circle(self.image, (255,0,0), (5, 5), 5)

	def __init__(self, position, vecteur):
		super(Projectile, self).__init__()


	def update(self, *args) :
		self.rect.x, self.rect.y += self.vitesse
=======
	vitesse = (0, 0)
	dommage = 3
	image = pygame.Surface((10, 10))
	pygame.draw.circle(image, (255,0,0), (5, 5), 5)

	def __init__(self, position, vecteur):
		Projectile.__init__(self, position, vecteur)


	def update(self, *args) :
		self.rect.x += self.vitesse[0]
		self.rect.y += self.vitesse[1]
>>>>>>> origin/master
