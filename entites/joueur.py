#-*- coding: utf-8 -*-

from personnage          import Personnage
from armes.arme2         import Arme2
from armes.armeSinus     import ArmeSinus
from armes.fusilPompe    import FusilPompe
from sons import son

class Joueur(Personnage):

    _armes = [Arme2(), FusilPompe(), ArmeSinus()]
    _arme  = 0
    arme   = _armes[0]

    '''
    changerArme
    '''
    def changerArme(self) :

        self.arme.kill()

        self._arme += 1

        if self._arme >= len(self._armes) :
            self._arme = 0

        self.arme = self._armes[self._arme]
        return self.arme

    '''
    tirer

    Comme le joueur a plusieur armes,
    on ne peut pas appeler `self.arme.tirer()` comme pour les autres perso

    @param  {tuple} vecteur     Direction du tir
    @return {Liste}             Liste de projectiles renvoyés par l'arme
    '''
    def tirer(self, vecteur) :
        return self.arme.tirer(self.positionMain(), vecteur)

    def bougerArme(self, direction) :
        self.arme.direction(direction)


    '''
    blessure

    Aie
    '''
    def blessure(self, vie):
        son.sonBlessureJoueur()
        super(Joueur, self).blessure(vie)
