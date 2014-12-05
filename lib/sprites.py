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

    '''
    sprites

    Pratique pour découper rapidement une sprite en une liste d'images

    @param {Liste}      sprites     Une liste de listes d'aguments compatibles self.sprite
                                    [[(xO, y0), (width, height)], ... ]
    @param {Boolean}    flipX       Miroir vertical ? Defaut : False
    @param {Boolean}    flipY       Miroir horizontal ? Defaut : False

    @return {Liste}                 Une liste de Surface obtenue par self.sprite
    '''
    def sprites(self, sprites, flipX = False, flipY = False) :
        images = []

        for sprite in sprites :
            img = self.sprite(sprite[0], sprite[1])
            if flipX :
                img = pygame.transform.flip(img, True, False)
            if flipY :
                img = pygame.transform.flip(img, False, True)
            images.append(img)

        return images

