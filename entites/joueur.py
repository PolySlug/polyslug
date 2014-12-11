#-*- coding: utf-8 -*-
from personnage          import Personnage
from armes.arme2         import Arme2
from armes.armeSinus     import ArmeSinus
from armes.fusilPompe    import FusilPompe
from sons import son

class Joueur(Personnage):

    armes = [Arme2(), FusilPompe(), ArmeSinus()]
    arme  = 0

    '''
    changerArme
    '''
    def changerArme(self) :

        self.arme += 1

        if self.arme >= len(self.armes) :
            self.arme = 0

    '''
    tirer

    Comme le joueur a plusieur armes,
    on ne peut pas appeler `self.arme.tirer()` comme pour les autres perso

    @param  {tuple} vecteur     Direction du tir
    @return {Liste}             Liste de projectiles renvoyés par l'arme
    '''
    def tirer(self, vecteur) :
        return self.armes[self.arme].tirer(self.position(), vecteur)
    
    def blessure(self, vie):
        son.sonBlessureJoueur()
        super(Joueur, self).blessure(vie)
