from arme import Arme
from projectiles.projectile1 import Projectile1
from lib.sprites             import Sprites

class Arme1(Arme) :

	def __init__(self):

		self.sprites = Sprites('img/tiles_spritesheet.png') #/!\ check le nom du sprite
		self.imageDefaut = self.sprites.sprite((432,0), (72, 72))


	def tirer(self, position, vecteur) :

		return Projectile1(position, vecteur)
