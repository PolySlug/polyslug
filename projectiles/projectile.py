#test de projectiles
import pygame

class Projectile(pygame.sprite.Sprite):

	self.rect =  (0, 0)
        self.image = None
	self.sprite = None
	self.dommage = 10

	'''
	__init__

	Initialise les position, vitesse et sprite du projectile

	@param {tuple} position & vecteur
	'''
	def __init__(self, position, vecteur):

 		pygame.sprite.Sprite.__init__(self)

        	#On récupère le rectangle de l'image
	        self.rect = self.image.get_rect()
		
		self.rect.x, self.rect.y = position

		vx, vy = vecteur

		#Calcul norme
		norme = math.sqrt(vx*vx + vy*vy)

		self.vitesse = (vx / norme, vy / norme)

	'''
	Update la position du projectile grace au tuple vitesse
	'''
	def update(self, *args):
		pass
		# a la fin de update, changer self.image à partir de self.sprite
		# et si besoin, changer self.rect
