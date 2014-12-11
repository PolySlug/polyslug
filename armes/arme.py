#-*- coding: utf-8 -*-

import pygame

from sons       import son
from lib.angle  import angleVecteurs

class Arme(pygame.sprite.Sprite) :

    #imageDefaut : l'image de l'arme sans rotation
    #image
    #rect
    angle = 0
    center = (0, 0)

    dernierTir = 0 #delai entre 2 tires

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        #On récupère le rectangle de l'image
        self.rect = self.image.get_rect()

    '''
    position

    Setter la position de l'arme
    @param {tuple}  pos
    '''
    def position(self, pos) :
        self.center = pos

    '''
    direction

    Setter la direction de tir de l'arme
    @param {tuple}  vect
    '''
    def direction(self, vect) :
        angle = angleVecteurs((0, 1), vect)
        if vect[0] < 0 :
            angle *= -1

        #l'angle par rapport au vecteur (0, 1)
        self.angle = angle

    '''
    update

    Calcule la nouvelle image
    '''
    def update(self, *args) :

        img = self.imageDefaut

        if self.angle < 0 :
            img = pygame.transform.flip(img, True, False)
            self.angle += 90
        else :
            self.angle -= 90

        self.image = pygame.transform.rotate(img, self.angle)

        #on pivote autour de la postion donnée
        self.rect = self.image.get_rect()
        self.rect.center = self.center

    '''
    tirer

    @param  {tuple} positon     Position 0 du tir
    @param  {tuple} vecteur     Direction du tir
    @return {Liste}             Une liste de projectiles
    '''
    def tirer(self, position, vecteur) :

        self.dernierTir = pygame.time.get_ticks() #On enregistre le tir pour respecter le delai entre 2 tirs
        son.sonTir() #c'est bien plus fun

        #chaque arme doit implémenter une façon de renvoyer une liste de projectiles
