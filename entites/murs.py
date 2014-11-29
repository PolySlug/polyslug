#-*- coding: utf-8 -*-

from entite      import Entite
from lib.sprites import Sprites

class Murs(Entite):

    sprites = Sprites('img/tiles_spritesheet.png')
    image   = sprites.sprite((216, 0), (72,72))

    '''
    blessure

    Un mur ne peut pas mourir
    '''
    def blessure(self) :
        return 1
