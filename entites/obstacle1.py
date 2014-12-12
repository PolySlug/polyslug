#-*- coding: utf-8 -*-

from obstacle import Obstacle
from lib.sprites import Sprites

#test
class ObstacleTest(Obstacle):

    sprites = Sprites('img/tiles_spritesheet.png')

    imageVie = sprites.sprite((504, 144), (72, 72))
    imageDegats = sprites.sprite((648, 144), (72, 72))

    image   = imageVie

    '''
    update

    2 images différentes selon le niveau de vie
    '''
    def update(self, *args):
        if self.vie > 5 :
            self.image = self.imageVie
        else :
            self.image = self.imageDegats
