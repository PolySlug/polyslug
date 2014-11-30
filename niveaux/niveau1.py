#-*- coding: utf-8 -*-

from entites.murs          import Murs
from entites.obstacleTest  import ObstacleTest
from entites.ennemi        import Ennemi
from entites.joueur        import Joueur

'''
Touts les éléments du niveau
'''

murs = [Murs((200, 50))]

obstacles = [ObstacleTest((0,0)), ObstacleTest((100, 0))]

ennemis = []

joueur = []


'''
niveau

La structure d'un niveau

@type {Dictionnaire}
'''
niveau = {
    'murs':      murs,
    'obstacles': obstacles,
    'ennemis':   ennemis,
    'joueur':    joueur
}
