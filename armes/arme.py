#-*- coding: utf-8 -*-

import pygame

class Arme(pygame.sprite.Sprite) :

    #imageDefaut : l'image de l'arme sans rotation
    #image
    #rect

    dernierTir = 0 #delai entre 2 tires

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        #On récupère le rectangle de l'image
        self.rect = self.image.get_rect()

    #Update de la position
    def update(self, position, angle) :
        self.rect.x, self.rect.y = position
        self.image = pygame.transform.rotate(self.imageDefaut, angle)

    def tirer(self, position, vecteur) :
        self.dernierTir = pygame.time.get_ticks()

        #chaque arme doit implémenter une façon de renvoyer une liste de projectiles
