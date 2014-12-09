#-*- coding: utf-8 -*-

import pygame
from sons import son

'''
Entite

'''
class Entite(pygame.sprite.Sprite) :

    '''
    vie

    La vie de l'entitée
    '''
    vie = 100

    '''
    rect

    Position et surface occupée par l'entitée
    @type {pygame.Rect} Les deux premiers int sont pour la position x, y
                        Les deux derniers sont pour width, height
    '''
    #rect =

    '''
    @constructor

    @param {Tupple} position    Position de l'entitée
    '''
    def __init__(self, position) :
        pygame.sprite.Sprite.__init__(self)

        #On récupère le rectangle de l'image
        self.rect = self.image.get_rect()

        #Prise en compte de la position
        x, y = position
        self.rect.x = x
        self.rect.y = y

    def update(self, *args) :
        pass

    def position(self) :
        return (self.rect.x, self.rect.y)

    '''
    blessure

    Fonction par défaut. Modifiée dans certains cas
    @param {Int}    vie     La quantité de vie à enlever
    '''
    def blessure(self, vie):
        self.vie -= vie
        son.sonBlessureEnnemi()
        if self.vie <= 0 :
            self.kill()     #supprime la sprite de tous les groupes
            son.sonMort()
        return self.vie

