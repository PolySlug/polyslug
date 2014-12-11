#-*- coding: utf-8 -*-

from entite      import Entite
from lib.sprites import Sprites

class Mur(Entite):

    plateforme = False

    '''
    __init__

    Découpe de l'image
    '''
    def __init__(self, position, image, rect) :
        self.sprites = Sprites(image)
        self.image   = self.sprites.sprite(rect = rect)

        super(Mur, self).__init__(position)

    '''
    blessure

    Un mur ne peut pas mourir
    '''
    def blessure(self) :
        return 1
