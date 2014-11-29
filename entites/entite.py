#-*- coding: utf-8 -*-

import pygame

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
    rect = pygame.Rect(0, 0, 10, 10)

    '''
    @constructor

    @param {Tupple} position    Position de l'entitée
    '''
    def __init__(self, position) :
        pygame.sprite.Sprite.__init__(self)

        #Prise en compte de la position
        x, y = position
        self.rect[0] = x
        self.rect[0] = y

    def update(self) :
        pass

    '''
    blessure

    Fonction par défaut. Modifiée dans certains cas
    @param {Int}    vie     La quantité de vie à enlever
    '''
    def blessure(self, vie):
        self.vie -= vie
        return self.vie

