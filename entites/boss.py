#-*- coding: utf-8 -*-
import pygame

from ennemi      import Ennemi
from lib.sprites import Sprites
from armes.armeboss import ArmeBoss

class Boss(Ennemi):

    sprites = Sprites('img/p2_spritesheet.png')

    arme = ArmeBoss()

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

        #REDIMENSIONNEMENT DES FRAMES DU BOSS
        # Idee : recuperer taille et mult par ce qu'on veut, ici par 2
        j = 0

        self.framesDroitesNonDim = self.sprites.sprites(images)
        self.framesDroites = []
        for i in self.framesDroitesNonDim :
            tailleFD = self.framesDroitesNonDim[j].get_size()
            redim = pygame.transform.scale(self.framesDroitesNonDim[j], (tailleFD[0]*2, tailleFD[1]*2))
            self.framesDroites.append(redim)
            j = j+1

        j = 0

        self.framesGauchesNonDim = self.sprites.sprites(images, flipX = True)
        self.framesGauches = []
        for i in self.framesGauchesNonDim :
            tailleFG = self.framesGauchesNonDim[j].get_size()
            redim = pygame.transform.scale(self.framesGauchesNonDim[j], (tailleFG[0]*2, tailleFG[1]*2))
            self.framesGauches.append(redim)
            j = j+1


        self.imageNonDim = self.imageReposNonDim = self.sprites.sprite((0, 190), (66, 92))
        tailleimage = self.imageNonDim.get_size()
        self.image = self.imageRepos = pygame.transform.scale(self.imageNonDim, (tailleimage[0]*2, tailleimage[1]*2))

        self.imageAccroupiNonDim = [
            self.sprites.sprite((355, 95), (67, 72)),
            self.sprites.sprite((355, 95), (67, 72), flipX = True)
        ]

        j = 0

        self.imageAccroupi= []

        for i in self.imageAccroupiNonDim :
            tailleA = self.imageAccroupiNonDim[j].get_size()
            redim = pygame.transform.scale(self.imageAccroupiNonDim[j], (tailleA[0]*2, tailleA[1]*2))
            self.imageAccroupi.append(redim)
            j = j+1
            
    def positionMain(self) :
      
        position = self.position()


        main = [0, 0]
        main[0], main[1] = position[0], position[1]
        main[1] += 150
        main[0] += 12

        return main

