#-*- coding: utf-8 -*-

import pygame
from lib.sprites import Sprites

class Checkpoint(pygame.sprite.Sprite) :

    check    = False
    couleur  = "red" #red | green | blue
    compteur = 0

    sprite = Sprites("img/items_spritesheet.png")

    image = None
    imagesCheck = []
    imageNonCheck = None

    def __init__(self, couleur, position) :

        pygame.sprite.Sprite.__init__(self)

        self.couleur = couleur

        #découpe du sprite en fonction de la couleur demandée

        if couleur == "blue" :
            self.imagesCheck = self.sprite.sprites([((275, 72), (70, 70)), ((275, 0), (70, 70))])
            self.image = self.imageNonCheck = self.sprite.sprite((216, 504), (70, 70))

        elif couleur == "green" :
            self.imagesCheck = self.sprite.sprites([((216, 432), (70, 70)), ((216, 360), (70, 70))])
            self.image = self.imageNonCheck = self.sprite.sprite((216, 288), (70, 70))

        elif couleur == "yellow" :
            self.imagesCheck = self.sprite.sprites([((203, 0), (70, 70)), ((202, 144), (70, 70))])
            self.image = self.imageNonCheck = self.sprite.sprite((144, 434), (70, 70))

        else : #red
            self.couleur = "red"
            self.imagesCheck = self.sprite.sprites([((274, 144), (70, 70)), ((216, 216), (70, 70))])
            self.image = self.imageNonCheck = self.sprite.sprite((203, 72), (70, 70))

        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = position


    def position(self) :
        return (self.rect.x, self.rect.y)

    def update(self, *args) :

        if self.check :

            self.image = self.imagesCheck[1 if self.compteur % 60 > 29 else 0]
            self.compteur += 1

        else :
            self.image = self.imageNonCheck
