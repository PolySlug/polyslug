#-*- coding: utf-8 -*-
import pygame

'''
Sprites

Découpe d'images
'''
class Sprites(object):

    '''
    @constructor
    @param {String} file    La path vers l'image
    '''
    def __init__(self, file) :
        self.image = pygame.image.load(file)

    '''
    sprite

    @param {Tupple} ref     Le point haut gauche
    @param {Tupple} taille  width et height de l'image à récupérer
    '''
    def sprite(self, ref, taille) :

        image = pygame.Surface(taille)
        image.blit(self.image, (0,0), (ref[0], ref[1], taille[0], taille[1]))
        image.set_colorkey((0,0,0))

        return image
