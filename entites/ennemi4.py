#-*- coding: utf-8 -*-

from ennemi      import Ennemi
from lib.sprites import Sprites
from armes.fusilPompe import FusilPompe

class Ennemi4(Ennemi):

    sprites = Sprites('img/p5_spritesheet.png')

    vie = 20

    def __init__(self, position) :

        self.arme = FusilPompe()
        super(Ennemi4, self).__init__(position)

    '''
    construireSprites
    '''
    def contruireSprites(self) :

        #images mouvement
        images = [
            [(0, 0), (72, 97)],
            [(73, 0), (72, 97)],
            [(146, 0), (72, 97)],
            [(0, 98), (72, 97)],
            [(73, 98), (72, 97)],
            [(146, 98), (72, 97)],
            [(219, 0), (72, 97)],
            [(292, 0), (72, 97)],
            [(219, 98), (72, 97)],
            [(365, 0), (72, 97)],
            [(292, 98), (72, 97)],
        ]

        self.framesDroites = self.sprites.sprites(images)
        self.framesGauches = self.sprites.sprites(images, flipX = True)

        self.image = self.imageRepos = self.sprites.sprite((0, 190), (66, 92))

        self.imageAccroupi = [
            self.sprites.sprite((355, 95), (67, 72)),
            self.sprites.sprite((355, 95), (67, 72), flipX = True)
        ]
