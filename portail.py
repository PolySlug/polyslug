#-*- coding: utf-8 -*-

import pygame
from lib.sprites import Sprites

class Portail(pygame.sprite.Sprite) :

    def __init__(self, position, suivant, nom) :

        if nom == "jouer" :
            self.image  = pygame.image.load('img/portail_jouer.png')
        elif nom == "score" :
            self.image  = pygame.image.load('img/portail_score.png')
        elif nom == "credit" :
            self.image  = pygame.image.load('img/portail_credit.png')
        elif nom == "exit" :
            self.image  = pygame.image.load('img/signExit.png')
        elif nom == "flecheDroite":
            self.image  = pygame.image.load('img/signRight.png')
        else:
            self.image  = pygame.image.load('img/signLeft.png')

        pygame.sprite.Sprite.__init__(self)

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

        self.suivant = suivant
