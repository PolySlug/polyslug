#-*- coding: utf-8 -*-

from entitee import Entitee

class Murs(Entite):

    sprites = Sprites('img/tiles_spritesheet.png')
    self.image = self.sprites.sprite((216, 0), (72,72))

    '''
    blessure

    Un mur ne peut pas mourir
    '''
    def blessure(self) :
        return 1
