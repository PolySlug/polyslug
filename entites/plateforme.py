#-*- coding: utf-8 -*-

from entite      import Entite
from lib.sprites import Sprites

class Plateforme (Entite):

    sprites = Sprites('img/bridge.png')
    image   = sprites.sprite((0, 52), (72,20))
    plateforme = True

    '''
    blessure

    Un mur ne peut pas mourir
    '''
    def blessure(self) :
        return 1
