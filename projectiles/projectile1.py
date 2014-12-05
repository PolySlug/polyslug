import pygame
from projectile import Projectile
 
#projectile allant en ligne droite

class Projectile1(Projectile):

	self.vitesse = (0, 0)
	self.dommage = 3
	self.image = pygame.Surface((10, 10))
	pygame.draw.circle(self.image, (255,0,0), (5, 5), 5)

	def __init__(self, position, vecteur):
		super(Projectile, self).__init__()


	def update(self, *args) :
		self.rect.x, self.rect.y += self.vitesse