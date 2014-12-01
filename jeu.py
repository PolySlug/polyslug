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

@return {?}                                 Le score de la partie
'''
def gestionJeu(fenetre, niveau):

    joueur = niveau['joueur']

    #Création des groupes de sprites
    groupeMurs      = creationGroupe(niveau['murs'])
    groupeObstacles = creationGroupe(niveau['obstacles'])
    groupeEnnemis   = creationGroupe(niveau['ennemis'])

    groupeJeu       = creationGroupe(niveau['murs'] + niveau['obstacles'] + \
            niveau['ennemis'] + [joueur])

    #Création d'un calque
    calque = pygame.Surface((1000, fenetre.get_height()))

    done = False

    #Init du temps
    clock = pygame.time.Clock()

    #On récupère le système (Win/Mac/etc) pour les touches
    systeme = platform.system()

    while not done :

        calque.fill((0, 20, 50))

        #Écoute des touches clavier

        for event in pygame.event.get() :

            #Fermeture fenêtre
            if event.type == pygame.QUIT :
                pygame.quit() #TODO : ne pas quitter ici mais dans main

            #Écoute déplacement
            if systeme == "Windows" : #pygame sur windows est en Qwerty ...
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_a :
                        joueur.deplacementX(-3)
                    if event.key == pygame.K_d :
                        joueur.deplacementX(3)
                if event.type == pygame.KEYUP :
                    if event.key == pygame.K_a or event.key == pygame.K_d :
                        joueur.deplacementX(0)

            else :
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_q :
                        joueur.deplacementX(-3)
                    if event.key == pygame.K_d :
                        joueur.deplacementX(3)
                if event.type == pygame.KEYUP :
                    if event.key == pygame.K_q or event.key == pygame.K_d :
                        joueur.deplacementX(0)

        #On update tout le petit monde
        groupeJeu.update()

        #On dessine dans le calque
        groupeJeu.draw(calque)

        #On insère le calque dans le fenêtre en fonction de decalageX
        fenetre.fill((0, 0, 0))
        fenetre.blit(calque, (-joueur.rect.x, 0)) #on multiplie par 3, on a pas que ça à faire
        pygame.display.flip()

        clock.tick(60)

    return #TODO

'''
creationGroupe

@param  {Liste)                 items
@return {pygame.sprite.Group}
'''
def creationGroupe(items):
    return pygame.sprite.Group(*items)
