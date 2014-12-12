#-*- coding: utf-8 -*-

from ennemi      import Ennemi
from lib.sprites import Sprites
from armes.armeSinus import ArmeSinus

class Ennemi1(Ennemi):

    sprites = Sprites('img/p2_spritesheet.png')

    vie = 20

    def __init__(self, position) :

        self.arme = Arme1()
        super(Ennemi1, self).__init__(position)

    '''
    construireSprites
    '''
    def contruireSprites(self) :

        #images mouvement
        images = [
            [(0, 0), (70, 94)],
            [(71, 0), (70, 94)],
            [(142, 0), (70, 94)],
            [(0, 95), (70, 94)],
            [(71, 95), (70, 94)],
            [(142, 95), (70, 94)],
            [(213, 0), (70, 94)],
            [(284, 0), (70, 94)],
            [(213, 95), (70, 94)],
            [(355, 0), (70, 94)],
            [(284, 95), (70, 94)],
        ]

        self.framesDroites = self.sprites.sprites(images)
        self.framesGauches = self.sprites.sprites(images, flipX = True)

        self.image = self.imageRepos = self.sprites.sprite((0, 190), (66, 92))

        self.imageAccroupi = [
            self.sprites.sprite((355, 95), (67, 72)),
            self.sprites.sprite((355, 95), (67, 72), flipX = True)
        ]
