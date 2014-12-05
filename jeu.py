#-*- coding: utf-8 -*-

import pygame
import platform
from lib.viseur         import Viseur
from lib.ecouteSouris   import ecouteSouris
from bord import Bord


'''
gestionJeu

@param {pygame.Surface} fenetre             La fenetre principale du jeu
@param {Dictionnaire}   niveau
@param {Liste}          niveau.murs                     Une liste d'instances de murs
@param {Liste}          niveau.obstacles                Une liste d'instances d'obstacles
@param {Liste}          niveau.ennemis                  Une liste d'instances d'ennemis
@param {Liste}          niveau.joueur                   Une instance joueur
@param {Int}            niveau.taille                   Longueur du niveau en px


@return {?}                                 Le score de la partie
'''
def gestionJeu(fenetre, niveau):

    f_width, f_height = fenetre.get_width(), fenetre.get_height() #racourcis
    decalageX = 0
    
    #creation des bords
    bords = [Bord((-1,0), (1, f_height)), Bord((f_width, 0), (1, f_height)),\
                 Bord((0,-1), (f_width, 1)), Bord((0, f_height), (f_width, 1))]
        
    joueur = niveau['joueur']

    #Création des groupes de sprites

    groupeMurs                  = creationGroupe(niveau['murs'])
    groupeObstacles             = creationGroupe(niveau['obstacles'])
    groupeEnnemis               = creationGroupe(niveau['ennemis'])
    groupeProjectilesJoueur     = pygame.sprite.Group()
    groupeProjectilesEnnemis    = pygame.sprite.Group()
    groupeBords                 = creationGroupe(bords)

    groupeJeu                   = creationGroupe(niveau['murs'] + niveau['obstacles'] + \

            niveau['ennemis'] + [joueur])

    #Création d'un calque
    calque = pygame.Surface((niveau['taille'], f_height))

    done   = False
    course = 1      #gestion de la vitesse de deplacement (marcher : 1, courir : 3)
    viseur = Viseur()

    #Init du temps
    clock = pygame.time.Clock()

    #On récupère le système (Win/Mac/etc) pour les touches
    systeme = platform.system()

    while not done :

        calque.fill((0, 20, 50)) #un nouveau calque tout beau tout propre

        #Écoute des touches clavier

        for event in pygame.event.get() :

            #Fermeture fenêtre
            if event.type == pygame.QUIT :
                pygame.quit() #TODO : ne pas quitter ici mais dans main

            #Gestion de la vitesse de course
            if event.type == pygame.KEYDOWN and  \
                (event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT) :
                course = 3
            if event.type == pygame.KEYUP and  \
                (event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT) :
                course = 1

            if event.type == pygame.MOUSEBUTTONDOWN :
                position = (joueur.rect.x, joueur.rect.y)
                positionSouris = ecouteSouris()
                vecteur = (positionSouris[0] - position[0], positionSouris[1] - position[1])
                groupeProjectilesEnnemis.add(joueur.arme.tirer(position, vecteur))


            #Écoute déplacement
            if systeme == "Windows" : #pygame sur windows est en Qwerty ...

                #Demande de saut
                if event.type == pygame.KEYDOWN and event.key == pygame.K_w :
                    joueur.sauter()

                #Demande de mouvement
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_a :
                        joueur.deplacementX(-3 * course)
                    if event.key == pygame.K_d :
                        joueur.deplacementX(3 * course)
                #Fin de mouvement
                if event.type == pygame.KEYUP :
                    if event.key == pygame.K_a or event.key == pygame.K_d :
                        joueur.deplacementX(0)

            else :

                #Demande de saut
                if event.type == pygame.KEYDOWN and event.key == pygame.K_z :
                    joueur.sauter()

                #Demande de mouvement
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_q :
                        joueur.deplacementX(-3 * course)
                    if event.key == pygame.K_d :
                        joueur.deplacementX(3 * course)
                #Fin de mouvement
                if event.type == pygame.KEYUP :
                    if event.key == pygame.K_q or event.key == pygame.K_d :
                        joueur.deplacementX(0)


        #On update tout le petit monde

        #On commence par construire un object représentant l'état actuel du jeu
        etat = {
            'murs' :                groupeMurs,
            'obstacles':            groupeObstacles,
            'ennemis':              groupeEnnemis,
            'width':                niveau['taille'],
            'height':               f_height,
            'projectilesEnnemies':  groupeProjectilesEnnemis,
            'projectilesJoueur':    groupeProjectilesJoueur,
            'joueur':               joueur,
            'bords':                bords
            }

        #On update en passant les infos
        groupeJeu.update(etat)
        groupeProjectilesEnnemis.update(etat)
        groupeProjectilesJoueur.update(etat)
        groupeBords.update(decalageX)

        #On dessine dans le calque
        groupeJeu.draw(calque)
        groupeProjectilesEnnemis.draw(calque)
        viseur.draw(calque)

        #On insère le calque dans le fenêtre en fonction de decalageX
        fenetre.fill((0, 0, 0))
        decalageX = -joueur.rect.x + f_width / 2 if joueur.rect.x > f_width / 2 else 0
        fenetre.blit(calque, (decalageX, 0)) #on multiplie par 3, on a pas que ça à faire
        pygame.display.flip()

        clock.tick(60)

    return #TODO

'''
creationGroupe

@param  {Liste}                 items
@return {pygame.sprite.Group}
'''
def creationGroupe(items):
    return pygame.sprite.Group(*items)

'''
testCollision

1 teste des differentes collision entre les projectiles des ennemis vers le joueur et 
    les bords de la fenetre
2 teste des differentes collision entre les projectiles du joueur  vers les obstacles,
    les ennemis et les bords de la fenetre
    
-> destruction des projectiles en collision, soustraction des PV
    
@param {dictionnaire}          etat   toutes les groupes d'instance courantes 
'''

def testCollision(etat):
    #collision des projectiles ennemis vers joueur
    projectilesContactJ = pygame.sprite.spritecollide(etat.joueur, etat.ProjectilesEnnemis, True)
    for projectile in projectilesContactJ :
        etat.joueur.blessure(projectile.dommage)
    
    #collsion des projectiles joueur vers obstacles
    projectilesContactO = pygame.sprite.groupcollide(etat.projectilesJoueur, etat.obstacles, True, False)
    for projectile in projectilesContactO:
        etat.obstacles.blessure(projectile.dommage)
    
    #collision des projectiles joueur vers ennemis
    projectilesContactE = pygame.sprite.groupcollide(etat.projectilesJoueur, etat.ennemis, True, False)
    for projectile in projectilesContactE:
        etat.ennemis.blessure(projectile.dommage)
        
    
    #destruction des projectiles du joueur et des ennemis en contact avec les bords
    pygame.sprite.spritecollide(etat.projectilesJoueur, etat.bords, True)
    pygame.sprite.spritecollide(etat.projectilesEnnemis, etat.bords, True)
    
    return
    
    
