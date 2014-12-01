#-*- coding: utf-8 -*-

import pygame

from entite      import Entite
from lib.sprites import Sprites
#TODO import armes


'''
collisions

@param  {pygame.sprite.Sprite}  item        Typiquement, le joueur
@param  {Dictionnaire}          niveau
@return {Liste}     Liste des sprites de Mur et Obstalce en collision avec l'item
'''
def collisions(item, niveau) :
    collisions = []

    for test in ['murs', 'obstacles'] :
        collisions += pygame.sprite.spritecollide(item, niveau[test], False)

    return collisions


class Joueur(Entite):

    vitesse_x = 0
    vitesse_y = 0

    vie     = 100

    sprites = Sprites('img/p1_walk.png')
    frames  = []

    def __init__(self, position) :

        #Test images mouvement
        images = [
                [(0, 0), (66, 90)],
                [(66, 0), (66, 90)],
                [(132, 0), (67, 90)],
                [(0, 93), (66, 90)],
                [(66, 93), (66, 90)],
                [(132, 93), (72, 90)],
                [(0, 186), (70, 90)]
                ]

        self.framesDroites = self.sprites.sprites(images)
        self.framesGauches = self.sprites.sprites(images, flipX = True)

        self.image = self.framesDroites[0]

        super(Joueur, self).__init__(position)

    def calcul_Y(self, niveau) :

        #Calcul vitesse verticale due à la gravité
        if self.vitesse_y == 0 :
            self.vitesse_y = 1
        else:
            self.vitesse_y += 0.35 #PFD

        #Si on touche le sol
        if self.rect.y + self.rect.height > niveau['height'] :
            self.vitesse_y = 0
            self.rect.y = niveau['height'] - self.rect.height #on force à ne pas dépasser le sol

        self.rect.y += self.vitesse_y

    def calcul_X(self, niveau) :

        #si on touche un bord du niveau
        if (self.rect.x < 0 and self.vitesse_x < 0) \
            or (self.rect.x + self.rect.width > niveau['width'] and self.vitesse_x > 0):
            self.vitesse_x = 0

        self.rect.x += self.vitesse_x

        #si on touche quelque chose en chemin
        for collision in collisions(self, niveau) :
            if self.vitesse_x > 0 :
                self.rect.right = collision.rect.left
            if self.vitesse_x < 0 :
                self.rect.left = collision.rect.right


        #Gestion de l'image
        if self.vitesse_x > 0 : #image si déplacement vers la droite
            self.image = self.framesDroites[(self.rect.x // 30) % len(self.framesDroites)]
        elif self.vitesse_x < 0 : #image si déplacement vers la gauche
            self.image = self.framesGauches[(self.rect.x // 30) % len(self.framesGauches)]
        else : #image si perso à l'arrêt
            self.image = self.framesDroites[0]

    def update(self, niveau, *args) :

        self.calcul_X(niveau)
        self.calcul_Y(niveau)



    def deplacementX(self, vitesse) :
        self.vitesse_x = vitesse

