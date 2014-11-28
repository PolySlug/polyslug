
from entitee import Entite
#from sprites import Sprites

class Obstacle(Entite) :

    self.vie = 10
    #self.sprites = Sprites

    def draw(self, calque) :
        calque.blit(self.sprite.sprite((0,0), (10,10)) , self.position)
