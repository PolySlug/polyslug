#-*- coding: utf-8 -*-

import math

from personnage import Personnage

class Ennemi(Personnage):

    multiCourse = 3/2     #va 2 fois moins vite que le joueur

    def __init__(self, position) :

        #Sauvegarde de la position initiale
        self.pivot = position

        super(Ennemi, self).__init__(position)

    '''
    ia_directionJoueur

    @param  {Personnage} joueur
    @return {tuple}             Le vecteur distance ennemi/joueur
    '''
    def ia_directionJoueur(self, joueur) :
        x, y   = self.position()
        jx, jy = joueur.position()

        return (jx-x, jy-y)

    '''
    ia_distanceJoueur

    @param  {Personnage}    joueur
    @return {int}                   La distance ennemi/joueur en px
    '''
    def ia_distanceJoueur(self, joueur):
        vect = self.ia_directionJoueur(joueur)

        return math.sqrt( vect[0] * vect[0] + vect[1] * vect[1] )

    '''
    ia_joueurEnVue

    @param  {Personnage}    joueur
    @param  {int}           vision  Champ de vision de l'ennemi = distance max de px
    @return {Bool}                  True si le joueur est dans le champ de vision de l'ennemi
    '''
    def ia_joueurEnVue(self, joueur, vision) :
        return self.ia_distanceJoueur(joueur) < vision

    '''
    ia

    La partie autonome de l'ennemi.
    Tente de tuer le joueur si il est dans le champ de vision
    Sinon, reste à sa place

    @param  {dic}   niveau  l'état du niveau
    '''
    def ia(self, niveau) :

        joueur              = niveau['joueur']
        projectilesEnnemis  = niveau['projectilesEnnemis']

        enVue = self.ia_joueurEnVue(joueur, niveau['f_width'] * 0.8)

        if enVue :
            directionJoueur = self.ia_directionJoueur(joueur)

            #tirer
            projectile = self.arme.tirer(self.position(), directionJoueur)
            if projectile :
                projectilesEnnemis.add(projectile)

            #se rapprocher du joueur
            self.deplacementX(-1 if directionJoueur[0] < 0 else 1)

        else : #retour à la position pivot

            position = self.position()
            if not position == self.pivot :
                self.deplacementX(-1 if self.pivot[0] - position[0] < 0 else 1)


    def update(self, niveau, *args) :

        self.ia(niveau)

        self.calcul_Y(niveau)
        self.calcul_X(niveau)
