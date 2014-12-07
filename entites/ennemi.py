#-*- coding: utf-8 -*-

import math

from personnage import Personnage

class Ennemi(Personnage):

    multiCourse = 3/2     #vitesse de deplacementX (marcher/courir)

    def __init__(self, position) :

        #Sauvegarde de la position initiale
        self.pivot = position

        super(Ennemi, self).__init__(position)

    def ia_directionJoueur(self, joueur) :
        x, y   = self.position()
        jx, jy = joueur.position()

        return (jx-x, jy-y)

    def ia_distanceJoueur(self, joueur):
        vect = self.ia_directionJoueur(joueur)

        return math.sqrt( vect[0] * vect[0] + vect[1] * vect[1] )

    def ia_joueurEnVue(self, joueur, vision) :
        return self.ia_distanceJoueur(joueur) < vision

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
