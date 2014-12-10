
import pygame

from arme           import Arme
from lib.sprites    import Sprites
from projectiles.projectileDroitVert import ProjectileDroitVert

class Arme2(Arme) :

    delai = 200

    def __init__(self):

        self.sprites = Sprites('img/raygun.png')
        self.image = self.imageDefaut = self.sprites.sprite((0,12), (56, 56))

        super(Arme2, self).__init__()

    def tirer(self, position, vecteur) :

        if pygame.time.get_ticks() - self.dernierTir > self.delai :

            super(Arme2, self).tirer(position, vecteur)
            return [ProjectileDroitVert(position, vecteur)]

        else :
            return []
