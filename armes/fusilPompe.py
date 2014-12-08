#-*- coding: utf-8 -*-

import pygame

from arme           import Arme
from lib.sprites    import Sprites
from projectiles.projectileDroitRouge import ProjectileDroitRouge

'''
calculTirs

Calcul 3 vecteur unitaires à partir de `tup`
Chacun créé en faisant tourner tup d'un certain angle

@param  {tuple}  tup    Le vecteur inital
@return {Liste}         Une liste de tuple
'''
def calculTirs(tup) :

    result = []
    angles = [-20, 0, 20]

    for angle in angles :
        v = pygame.math.Vector2(tup).rotate(angle)
        result.append((v.x, v.y))

    return result


'''
FusilPompe

Une arme pas très puissante
Mais qui tire 3 projectiles dispersé
'''
class FusilPompe(Arme) :

    delai = 700

    def __init__(self):

        self.sprites = Sprites('img/tiles_spritesheet.png')
        self.imageDefaut = self.sprites.sprite((432,0), (72, 72))

    def tirer(self, position, vecteur) :

        tirs = calculTirs(vecteur)

        if pygame.time.get_ticks() - self.dernierTir > self.delai :

            super(FusilPompe, self).tirer(position, vecteur)
            projectiles = []

            for direction in tirs :
                projectiles.append(ProjectileDroitRouge(position, direction))

            return projectiles

        else :
            return []
