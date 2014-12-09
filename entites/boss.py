#-*- coding: utf-8 -*-
import pygame

from ennemi      import Ennemi
from lib.sprites import Sprites
from armes.arme1 import Arme1

class Boss(Ennemi):

    sprites = Sprites('img/p2_spritesheet.png')

    arme = Arme1()

    vie = 80

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
        #self.sizeFD = self.framesDroitesPetites.get_size() Idee : recuperer taille et mult par ce qu'on veut
        #self.framesDroites = pygame.transform.scale(self.image, (int(self.size[0]*2), int(self.size[1]*2)))  
        self.framesGauches = self.sprites.sprites(images, flipX = True)

        self.image = self.imageRepos = self.sprites.sprite((0, 190), (66, 92))

        self.imageAccroupi = [
            self.sprites.sprite((355, 95), (67, 72)),
            self.sprites.sprite((355, 95), (67, 72), flipX = True)
        ]
