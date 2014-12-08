#-*- coding: utf-8 -*-

import pygame
import platform
import time
import datetime

from lib.viseur         import Viseur
from lib.ecouteSouris   import ecouteSouris
from bord               import Bord
from entites.joueur     import Joueur

pygame.font.init()
font = pygame.font.Font(None, 28)


'''
gestionJeu

@param {pygame.Surface} fenetre                         La fenetre principale du jeu
@param {Dictionnaire}   niveau
@param {Liste}          niveau.murs                     Une liste d'instances de murs
@param {Liste}          niveau.obstacles                Une liste d'instances d'obstacles
@param {Liste}          niveau.ennemis                  Une liste d'instances d'ennemis
@param {Liste}          niveau.checkpoints              Une liste d'instances de checkpoints
@param {tuple}          niveau.joueur                   La position initiale du joueur
@param {Int}            niveau.taille                   Longueur du niveau en px

@return {?}                                             Le score de la partie
'''
def gestionJeu(fenetre, niveau):

    f_width, f_height = fenetre.get_width(), fenetre.get_height() #racourcis dimension fenêtre

    #creation des bords
    bords = creationBords(f_width, f_height)

    #le joueur
    joueur = Joueur(niveau['joueur'])

    #Création des groupes de sprites

    groupeMurs                  = creationGroupe(niveau['murs'])
    groupeObstacles             = creationGroupe(niveau['obstacles'])
    groupeEnnemis               = creationGroupe(niveau['ennemis'])
    groupeCheckpoints           = creationGroupe(niveau['checkpoints'])
    groupeProjectilesJoueur     = pygame.sprite.Group() #les projectiles envoyés par le joueur
    groupeProjectilesEnnemis    = pygame.sprite.Group() #les projectiles envoyés par les ennemis
    groupeBords                 = creationGroupe(bords) #les bords de l'écran

    groupeJeu                   = creationGroupe(niveau['murs'] + niveau['obstacles'] + \
                                    niveau['ennemis'] + niveau['checkpoints'] + [joueur])

    #Création d'un calque dans lequel on va dessiner tout le niveau
    calque = pygame.Surface((niveau['taille'], f_height))

    done              = False
    decalageX         = 0
    dernierCheckPoint = niveau['joueur']  #la position du dernier checkpoint validé
    tempsStart        = time.time() #timestamp

    viseur = Viseur()

    #Init du temps
    clock = pygame.time.Clock()

    #On récupère le système (Win/Mac/etc) pour les touches
    systeme = platform.system()


    #Boucle principale
    while not done :

        #Le scroll horizontal du niveau
        decalageX = -joueur.rect.x + f_width / 2 if joueur.rect.x > f_width / 2 else 0

        #un nouveau calque tout beau tout propre
        calque.fill((0, 20, 50))

        #Si le joueur est mort, on le ressuscite au dernier checkpoint validé
        if joueur.vie <= 0 :
            joueur = Joueur(dernierCheckPoint)
            groupeJeu.add(joueur)


        #Écoute des touches clavier

        for event in pygame.event.get() :

            #Fermeture fenêtre
            if event.type == pygame.QUIT :
                pygame.quit() #TODO : ne pas quitter ici mais dans main

            #Gestion de la vitesse de course
            if event.type == pygame.KEYDOWN and  \
                (event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT) :
                joueur.vitesseCourse(courir = True)
            if event.type == pygame.KEYUP and  \
                (event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT) :
                joueur.vitesseCourse(courir = False)

            #Le joueur se baisse
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s :
                joueur.seBaisser(accroupi = True)
            if event.type == pygame.KEYUP and event.key == pygame.K_s :
                joueur.seBaisser(accroupi = False)

            #Le joueur change d'arme
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r :
                joueur.changerArme()

            #Le joueur tire
            if event.type == pygame.MOUSEBUTTONDOWN :
                #Calcul de la direction du tir
                positionJoueur = (joueur.rect.x, joueur.rect.y)
                positionSouris = ecouteSouris()
                vecteur = (positionSouris[0] - decalageX - positionJoueur[0], \
                        positionSouris[1] - positionJoueur[1])
                #Feu !
                projectiles = joueur.tirer(vecteur)
                for projectile in projectiles :
                    groupeProjectilesJoueur.add(projectile)


            #Écoute déplacement
            if systeme == "Windows" : #pygame sur windows est en Qwerty ...

                #Demande de saut
                if event.type == pygame.KEYDOWN and event.key == pygame.K_w :
                    joueur.sauter()

                #Demande de mouvement
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_a :
                        joueur.deplacementX(-1)
                    if event.key == pygame.K_d :
                        joueur.deplacementX(1)
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
                        joueur.deplacementX(-1)
                    if event.key == pygame.K_d :
                        joueur.deplacementX(1)
                #Fin de mouvement
                if event.type == pygame.KEYUP :
                    if event.key == pygame.K_q or event.key == pygame.K_d :
                        joueur.deplacementX(0)


        #On update tout le petit monde

        #On commence par construire un object représentant l'état actuel du jeu
        etat = {
            #Entités
            'murs' :                groupeMurs,
            'obstacles':            groupeObstacles,
            'ennemis':              groupeEnnemis,
            'checkpoints':          groupeCheckpoints,
            'joueur':               joueur,

            #Projectiles
            'projectilesEnnemis':   groupeProjectilesEnnemis,
            'projectilesJoueur':    groupeProjectilesJoueur,

            #taille niveau
            'width':                niveau['taille'],
            'height':               f_height,

            #taille fenêtre
            'f_width':              f_width,
            'f_height':             f_height, #idem height niveau

            #Bords de la fenêtre
            'bords':                bords
            }

        #On update en passant les infos
        groupeJeu.update(etat)
        groupeProjectilesEnnemis.update(etat)
        groupeProjectilesJoueur.update(etat)

        #On décale les bords comme il faut bien
        groupeBords.update(decalageX)

        #Test des collisions
        testCollision(etat)
        check = testCheckpoints(etat)
        if check :
            dernierCheckPoint = check

        #On dessine dans le calque
        groupeJeu.draw(calque)
        groupeProjectilesEnnemis.draw(calque)
        groupeProjectilesJoueur.draw(calque)

        viseur.draw(calque,decalageX)
        groupeBords.draw(calque) #il semblerait qu'on ait besoin de les dessiner pour le calcul des collisions

        afficherTemps(calque, time.time() - tempsStart, (f_width - decalageX - 70, 10))
        afficherVie(calque, joueur.vie, -decalageX)

        #On insère le calque dans le fenêtre en fonction de decalageX
        fenetre.fill((0, 0, 0))
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
creationBords

@param  {int}   f_width
@param  {int}   f_height
@return {Liste}     Liste de bords en fonctin de la dimension de la fenêtre
'''
def creationBords(f_width, f_height) :
    return [
            Bord((-f_width / 2, -f_height / 2), (1, f_height * 2)),
            Bord((f_width * 3/2, -f_height / 2), (1, f_height * 2)),
            Bord((-f_width / 2, -f_height / 2), (f_width * 2, 1)),
            Bord((-f_width / 2, f_height * 3/2), (f_width * 2, 1))
        ]

'''
testCollision

1 test des differentes collision entre les projectiles des ennemis vers le joueur et
    les bords de la fenetre
2 test des differentes collision entre les projectiles du joueur  vers les obstacles,
    les ennemis et les bords de la fenetre

-> destruction des projectiles en collision, soustraction des PV

@param {dictionnaire}          etat   toutes les groupes d'instance courantes
'''
def testCollision(etat):

    #collision des projectiles ennemis vers joueur
    projectilesContactJ = pygame.sprite.spritecollide(etat['joueur'], etat['projectilesEnnemis'], True)
    for projectile in projectilesContactJ :
        etat['joueur'].blessure(projectile.dommage) #on prend en compte les dommages

    #collsion des projectiles joueur vers obstacles
    projectilesContactO = pygame.sprite.groupcollide(etat['projectilesJoueur'], etat['obstacles'], True, False)
    for projectile in projectilesContactO: #On récupère les obstacles touchés et soustraction PV
        obstaclesTouches = projectilesContactO[projectile]
        for obstacle in obstaclesTouches :
            obstacle.blessure(projectile.dommage)

    #collision des projectiles joueur vers ennemis
    projectilesContactE = pygame.sprite.groupcollide(etat['projectilesJoueur'], etat['ennemis'], True, False)
    for projectile in projectilesContactE: #récup des ennemis touchés et soustraction PV
        ennemisTouches = projectilesContactE[projectile]
        for ennemi in ennemisTouches :
            ennemi.blessure(projectile.dommage)

    #destruction des projectiles du joueur et des ennemis en contact avec les bords
    #le jeu est trop facile sinon
    pygame.sprite.groupcollide(etat['projectilesJoueur'], etat['bords'], True, False)
    pygame.sprite.groupcollide(etat['projectilesEnnemis'], etat['bords'], True, False)

    return

'''
testCheckpoints

Test si le joueur est sur un checkpoint

@return {tuple | None}  Position du checkpoint ou None
'''
def testCheckpoints(etat) :
    check = pygame.sprite.spritecollide(etat['joueur'], etat['checkpoints'], False)
    if len(check) > 0 :
        for point in check :
            point.check = True
            return point.position()
    else :
        return None

'''
afficherTemps

Affiche le temps passé en paramètre sous format minute:seconde
@param {pygame.Surface} calque
@param {milli}          milli       temps à afficher en millisecondes
@param {tuple}          position    position du texte sur calque
'''
def afficherTemps(calque, milli, position) :

    #on covertit le timestamp
    st = datetime.datetime.fromtimestamp(milli).strftime('%M:%S')

    label = font.render(st, 1, (255, 255, 255))
    calque.blit(label, position)


'''
afficherVie

Affiche la vie du joueur en haut à gauche de l'écran

@param  {pygame.Surface}    surface     La surface sur laquelle on blit
@param  {int}               vie         La vie du joueur (max = `max`)
@param  {int}               decalageX   Scroll du niveau en px
@param  {int}               max
'''
def afficherVie(calque, vie, decalageX, max = 100) :

    pygame.draw.rect(calque, (255, 0, 0), (10 + decalageX, 10, 1.5 * max, 8), 1)
    pygame.draw.rect(calque, (255, 0, 0), (10 + decalageX, 10, 1.5 * vie, 8))

