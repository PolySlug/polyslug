
import pygame

from arme           import Arme
from lib.sprites    import Sprites
from projectiles.projectileSinusVert import ProjectileSinusVert

class ArmeSinus(Arme) :

    delai = 250

    def __init__(self):

        self.sprites = Sprites('img/raygunPurple.png')
        self.image = self.imageDefaut = self.sprites.sprite((0,12), (56, 56))

        super(ArmeSinus, self).__init__()

    def tirer(self, position, vecteur) :

        if pygame.time.get_ticks() - self.dernierTir > self.delai :

            super(ArmeSinus, self).tirer(position, vecteur)
            return [ProjectileSinusVert((position[0]+30*((2*self.angle)/(1+self.angle*self.angle)), position[1]+20+30*((1-self.angle*self.angle)/(1+self.angle*self.angle))), vecteur)] #Le tuple position est modifie afin de parametrer un cercle de rayon r=30px selon l'angle.

        else :
            return []
