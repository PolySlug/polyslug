
import pygame

from arme           import Arme
from lib.sprites    import Sprites
from projectiles.projectileDroitVert import ProjectileDroitVert

class Arme2(Arme) :

    delai = 200

    def __init__(self):

        self.sprites = Sprites('img/tiles_spritesheet.png')
        self.imageDefaut = self.sprites.sprite((432,0), (72, 72))

    def tirer(self, position, vecteur) :

        if pygame.time.get_ticks() - self.dernierTir > self.delai :

            super(Arme2, self).tirer(position, vecteur)
            return [ProjectileDroitVert(position, vecteur)]

        else :
            return []
