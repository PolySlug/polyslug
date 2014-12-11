 
import pygame

from arme           import Arme
from lib.sprites    import Sprites
from projectiles.projectileSinusVert import ProjectileSinusVert

class ArmeSinus(Arme) :

    delai = 250

    def __init__(self):

        self.sprites = Sprites('img/tiles_spritesheet.png')
        self.imageDefaut = self.sprites.sprite((432,0), (72, 72))

    def tirer(self, position, vecteur) :

        if pygame.time.get_ticks() - self.dernierTir > self.delai :

            super(ArmeSinus, self).tirer(position, vecteur)
            return [ProjectileSinusVert(position, vecteur)]

        else :
            return []
