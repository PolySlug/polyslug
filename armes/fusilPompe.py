#-*- coding: utf-8 -*-

import pygame
import math

from arme           import Arme
from lib.sprites    import Sprites
from projectiles.projectileDroitRouge import ProjectileDroitRouge


'''
rotation

@param  {tuple}  tup    Le vecteur à faire tourner
@param  {number} angle  L'angle en degrés
@return {tuple}         Rotation d'un angle `angle` de `tup`
'''
def rotation(tup, angle) :
    x, y = tup
    angle = math.radians(angle)
    return (
        x * math.cos(angle) - y * math.sin(angle),
        x * math.sin(angle) + y * math.cos(angle)
    )

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
        result.append(rotation(tup, angle))

    return result


'''
FusilPompe

Une arme pas très puissante
Mais qui tire 3 projectiles dispersé
'''
class FusilPompe(Arme) :

    delai = 700

    def __init__(self):

        self.sprites = Sprites('img/raygunPurple.png')
        self.image = self.imageDefaut = self.sprites.sprite((0,12), (56, 56))

        super(FusilPompe, self).__init__()

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
