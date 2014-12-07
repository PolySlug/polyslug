#-*- coding: utf-8 -*-

from entites.mur           import Mur
from entites.obstacleTest  import ObstacleTest
from entites.ennemi1       import Ennemi1
from entites.ennemi2       import Ennemi2
from entites.joueur        import Joueur

'''
Touts les éléments du niveau
'''

murs = [Mur((0, 400)), Mur((71, 400)), Mur((400, 550))]

obstacles = [ObstacleTest((0,0)), ObstacleTest((100, 0))]

ennemis = [Ennemi1((1000, 200)), Ennemi2((1200, 200))]

joueur = Joueur((0, 200))


'''
niveau

La structure d'un niveau

@type {Dictionnaire}
'''
niveau = {
    'murs':      murs,
    'obstacles': obstacles,
    'ennemis':   ennemis,
    'joueur':    joueur,
    'taille':    2000   #longueur du niveau en px
}
