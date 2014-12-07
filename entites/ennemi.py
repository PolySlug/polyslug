#-*- coding: utf-8 -*-

import math

from personnage import Personnage

class Ennemi(Personnage):

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

        enVue = self.ia_joueurEnVue(joueur, niveau['f_width'])

        if enVue :
            projectile = self.arme.tirer(self.position(), self.ia_directionJoueur(joueur))
            if projectile :
                projectilesEnnemis.add(projectile)


    def update(self, niveau, *args) :

        self.ia(niveau)

        self.calcul_Y(niveau)
        self.calcul_X(niveau)
