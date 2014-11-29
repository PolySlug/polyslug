#test de projectiles
import pygame.display

class Projectile(pygame.sprite.Sprite):

	self.rect =  (0, 0)
        self.image = None
	self.sprite = None
	self.dommage = 0

	'''
	__init__

	Initialise les position, vitesse et sprite du projectile

	@param {tuple} position & vecteur
	'''
	def __init__(self, position, vecteur):
		
		self.position = (x, y)
		self.image = pygame.draw.circle(fen, (120,120,0), x, y, 5)
		self.vitesse = (a, b)

	'''
	Update la position du projectile grace au tuple vitesse
	'''
	def update(self):
		self.rect = (a+x, y+b)		
		# a la fin de update, changer self.image à partir de self.sprite
		# et si besoin, changer self.rect
