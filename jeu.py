#-*- coding: utf-8 -*-

import pygame

'''
gestionJeu

@param {pygame.Surface} fenetre             La fenetre principale du jeu
@param {Dictionnaire}   niveau
@param {Liste}          niveau.murs         Une liste d'instances de murs
@param {Liste}          niveau.obstacles    Une liste d'instances d'obstacles
@param {Liste}          niveau.ennemis      Une liste d'instances d'ennemis
@param {Liste}          niveau.joueur       Une instance joueur
'''
def gestionJeu(fenetre, niveau):

    #Création des groupes de sprites
    groupeMurs      = creationGroupe(murs)
    groupeObstacles = creationGroupe(obstacles)
    groupeEnnemis   = creationGroupe(ennemis)

    groupeJeu       = creationGroupe(murs + obstacles + ennemis + joueur)

    #Création d'un calque
    calque = pygame.Surface((1000, fenetre.get_height()))

    done = False

    #Init du temps
    clock = pygame.time.Clock()

    while not done :

        groupeJeu.update()
        groupeJeu.draw(calque)

        fenetre.fill((0, 0, 0))
        fenetre.blit(calque, (0,0))
        pygame.display.flip()

        clock.tick(60)

    return

'''
creationGroupe

@param  {Liste)                 items
@return {pygame.sprite.Group}
'''
def creationGroupe(items):
    return pygame.sprite.Group(*items)
