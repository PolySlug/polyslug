#-*- coding: utf-8 -*-

import pygame
import platform

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
    groupeMurs      = creationGroupe(niveau['murs'])
    groupeObstacles = creationGroupe(niveau['obstacles'])
    groupeEnnemis   = creationGroupe(niveau['ennemis'])

    groupeJeu       = creationGroupe(niveau['murs'] + niveau['obstacles'] + \
            niveau['ennemis'] + niveau['joueur'])

    #Création d'un calque
    calque = pygame.Surface((1000, fenetre.get_height()))
    decalageX = 0

    done = False

    #Init du temps
    clock = pygame.time.Clock()

    #On récupère le système (Win/Mac/etc) pour les touches
    systeme = platform.system()

    while not done :

        #Écoute des touches clavier

        for event in pygame.event.get() :

            if systeme == "Windows" : #pygame sur windows est en Qwerty ...
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_a :
                        decalageX -= 1
                    if event.key == pygame.K_d :
                        decalageX += 1

            else :
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_q :
                        decalageX -= 1
                    if event.key == pygame.K_d :
                        decalageX += 1

        #Contrôle
        decalageX = decalageX if decalageX > -1 else 0

        #On update tout le petit monde
        groupeJeu.update()

        #On dessine dans le calque
        groupeJeu.draw(calque)

        #On insère le calque dans le fenêtre en fonction de decalageX
        fenetre.fill((0, 0, 0))
        fenetre.blit(calque, (-decalageX * 3, 0))
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
