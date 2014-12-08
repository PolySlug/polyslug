#-*- coding: utf-8 -*-
import pygame

'''
Bord

Un simple rectangle
Sert à gérer les sorties de fenêtre (killer les projectiles par ex)
'''
class Bord(pygame.sprite.Sprite):

    def __init__(self, position, taille):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface(taille)
        self.image.fill((255, 0, 0))

        self.rect = self.image.get_rect()

        self.position = position
        self.rect.x, self.rect.y = position

    '''
    update

    Le bord doit suivre le scroll du niveau
    '''
    def update(self, decalageX):
        self.rect.x = self.position[0] - decalageX
