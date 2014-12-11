
import pygame

from arme           import Arme
from lib.sprites    import Sprites
from projectiles.projectileDroitRouge import ProjectileDroitRouge

class Arme1(Arme) :

    delai = 1000

    def __init__(self):

        self.sprites = Sprites('img/raygunPurple.png')
        self.image = self.imageDefaut = self.sprites.sprite((0,12), (56, 56))

        super(Arme1, self).__init__()

    def tirer(self, position, vecteur) :

        if pygame.time.get_ticks() - self.dernierTir > self.delai :

            super(Arme1, self).tirer(position, vecteur)
            return [ProjectileDroitRouge(position, vecteur)]

        else :
            return []
