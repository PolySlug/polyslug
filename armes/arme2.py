import Arme
import Projectile2

class Arme2(Arme) :

	def __init__(self):
		self.sprite = Sprite('...') #/!\ check le nom du sprite
	
	def tirer(self, position, vecteur) :
		nombre = 1
		return (nombre, position, vecteur)