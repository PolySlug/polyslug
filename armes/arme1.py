import Arme
import Projectile1

class Arme1(Arme) :

	def __init__(self):
		self.sprite = Sprite('...') #/!\ check le nom du sprite
	
	def tirer(self, position, vecteur) :
		nombre = 3 # Nombre de projectiles envoyes a la suite 
		return (nombre,position, vecteur)