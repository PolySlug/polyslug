import Arme
import Projectile2

class Arme2(Arme) :

	def __init__(self):

		self.sprite = Sprite('...') #/!\ check le nom du sprite

		#self.imageDefaut = self.sprites.sprite((0,0), ())

	def tirer(self, position, vecteur) :
		
		return Projectile2(position, vecteur)
