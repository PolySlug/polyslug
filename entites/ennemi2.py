#-*- coding: utf-8 -*-

from ennemi      import Ennemi
from lib.sprites import Sprites
from armes.arme1 import Arme1

class Ennemi2(Ennemi):

    sprites = Sprites('img/p3_spritesheet.png')

    arme = Arme1()

    vie = 20

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

        self.image = self.imageRepos = self.sprites.sprite((0, 196), (66, 92))

        self.imageAccroupi = [
            self.sprites.sprite((365, 98), (69, 71)),
            self.sprites.sprite((365, 98), (69, 71), flipX = True)
        ]
