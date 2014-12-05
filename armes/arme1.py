import Arme
import Projectile1

class Arme1(Arme) :

	def __init__(self):

		self.sprites = Sprite('.....png') #/!\ check le nom du sprite

		#self.imageDefaut = self.sprites.sprite((0,0), ())
	

	def tirer(self, position, vecteur) :
		
		return Projectile1(position, vecteur)