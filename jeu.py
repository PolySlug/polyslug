#-*- coding: utf-8 -*-

import pygame
import platform
import time
import datetime

from lib.viseur         import Viseur
from lib.ecouteSouris   import ecouteSouris
from bord               import Bord
from entites.joueur     import Joueur
from sons import son


#Init de la font pygame
pygame.font.init()
font = pygame.font.Font(None, 28) #defaut


'''
gestionJeu

@param {pygame.Surface} fenetre                         La fenetre principale du jeu
@param {Dictionnaire}   niveau
@param {Liste}          niveau.murs                     Une liste d'instances de murs
@param {Liste}          niveau.obstacles                Une liste d'instances d'obstacles
@param {Liste}          niveau.ennemis                  Une liste d'instances d'ennemis
@param {Ennemi}         niveau.boss                     Le boss (une instance d'ennemi).
                                                        Quand il meurt la partie est finie
@param {Liste}          niveau.checkpoints              Une liste d'instances de checkpoints
@param {tuple}          niveau.joueur                   La position initiale du joueur
@param {Int}            niveau.taille                   Longueur du niveau en px

@return {int}                                           Le score de la partie (timestamp)
'''
def gestionJeu(fenetre, niveau, tempsStart = 0): #TODO : update doc

    f_width, f_height = fenetre.get_width(), fenetre.get_height() #racourcis dimension fenêtre

    #le fond
    fond = pygame.image.load('img/' + niveau['nom'] + '.png')

    #creation des bords
    bords = creationBords(f_width, niveau['height'])

    #le joueur
    joueur = Joueur(niveau['joueur'][0])

    boss = None
    if len(niveau['boss']) > 0 :
        boss = niveau['boss']

    niveau['ennemi'] = niveau['ennemis'] + niveau['boss']

    #Création des groupes de sprites
    groupeMurs                  = creationGroupe(niveau['murs'])
    groupePlateformes           = creationGroupe(niveau['plateformes'])
    groupeObstacles             = creationGroupe(niveau['obstacles'])
    groupeEnnemis               = creationGroupe(niveau['ennemis'])
    groupeCheckpoints           = creationGroupe(niveau['checkpoints'])
    groupePortails              = creationGroupe(niveau['portails'])
    groupeProjectilesJoueur     = pygame.sprite.Group() #les projectiles envoyés par le joueur
    groupeProjectilesEnnemis    = pygame.sprite.Group() #les projectiles envoyés par les ennemis
    groupeArmes                 = creationGroupeArmes(niveau, joueur) #toutes les armes
    groupeBords                 = creationGroupe(bords) #les bords de l'écran

    groupeJeu                   = creationGroupe(niveau['obstacles'] + niveau['ennemis'] \
                                    + niveau['checkpoints']\
                                    + [joueur])

    #Création d'un calque dans lequel on va dessiner tout le niveau
    calquePropre = pygame.Surface((niveau['width'], niveau['height']))
    calquePropre.blit(fond, (0,0))

    groupeMurs.draw(calquePropre)
    groupePlateformes.draw(calquePropre)
    groupePortails.draw(calquePropre)


    done              = False
    decalageX         = 0
    decalageY         = 0
    dernierCheckPoint = niveau['joueur'][0]  #la position du dernier checkpoint validé

    tempsStart += time.time()

    viseur = Viseur()

    #Init du temps
    clock = pygame.time.Clock()

    #On récupère le système (Win/Mac/etc) pour les touches
    systeme = platform.system()


    #Boucle principale
    while not done :

        #un nouveau calque tout beau tout propre
        calque = calquePropre.copy()

        #Le scroll horizontal du niveau
        decalageX = -joueur.rect.x + f_width / 2 if joueur.rect.x > f_width / 2 else 0

        #Scroll vertical
        decalageY = -1 * (niveau.get('height') - f_height)

        if joueur.rect.y < -decalageY + f_height / 2 :
            decalageY = f_height / 2 - joueur.rect.y

        decalageY = 0 if decalageY > 0 else decalageY

        #Si le joueur est mort, on le ressuscite au dernier checkpoint validé
        if joueur.vie <= 0 :
            joueur = Joueur(dernierCheckPoint)
            groupeJeu.add(joueur)
            groupeArmes.add(joueur.arme)

        #Si le boss est mort, c'est fini
        if boss and boss.vie <= 0 :
            son.sonVictoire()
            done = True

        #Calcul de la direction du tir
        positionSouris = ecouteSouris()
        positionmain = joueur.positionMain()
        vecteur = (positionSouris[0] - decalageX - positionmain[0]-15, \
                positionSouris[1] - decalageY - positionmain[1]+10)
        #-15 et +10 viennent du fait que l'on a décalé les projectiles
        #(de +15 et -10) à leur création pour qu'ils sortent de l'arme

        joueur.bougerArme(vecteur)

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
                groupeArmes.add(joueur.changerArme())

            #Le joueur tire
            if event.type == pygame.MOUSEBUTTONDOWN :
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
            'plateformes':          groupePlateformes,
            'obstacles':            groupeObstacles,
            'ennemis':              groupeEnnemis,
            'checkpoints':          groupeCheckpoints,
            'portails':             groupePortails,
            'joueur':               joueur,

            #Projectiles
            'projectilesEnnemis':   groupeProjectilesEnnemis,
            'projectilesJoueur':    groupeProjectilesJoueur,

            #armes
            'armes' :               groupeArmes,

            #taille niveau
            'width':                niveau.get('width'),
            'height':               niveau.get('height'),

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
        groupeArmes.update(etat)

        #On décale les bords comme il faut bien
        groupeBords.update(decalageX)

        #Test des collisions
        testCollision(etat)

        #les checkpoints
        check = testCheckpoints(etat)
        if check :
                #ne changer le checkpoint sauvegardé que si le nouveau est plus avancé
            if dernierCheckPoint[0] < check[0] :
                dernierCheckPoint = check

        #les portails
        suivant = testPortails(etat)
        if suivant :
            done = True

        #On dessine dans le calque
        groupeJeu.draw(calque)
        groupeProjectilesEnnemis.draw(calque)
        groupeProjectilesJoueur.draw(calque)
        groupeArmes.draw(calque)

        viseur.draw(calque, decalageX, decalageY)
        groupeBords.draw(calque) #il semblerait qu'on ait besoin de les dessiner pour le calcul des collisions

        afficherTemps(calque, time.time() - tempsStart, (f_width - decalageX - 70, 10 - decalageY))
        afficherVie(calque, joueur.vie, -decalageX, -decalageY)

        #On insère le calque dans le fenêtre en fonction de decalageX
        fenetre.fill((0, 0, 0))
        fenetre.blit(calque, (decalageX, decalageY)) #on multiplie par 3, on a pas que ça à faire

        pygame.display.flip()

        clock.tick(60)

    return (time.time() - tempsStart, suivant)

'''
creationGroupe

@param  {Liste}                 items
@return {pygame.sprite.Group}
'''
def creationGroupe(items):
    return pygame.sprite.Group(*items)


'''
creationGroupeArmes

Crée un groupe de sprite pygame contenant toutes les armes du jeu
Elles doivent être indépendante car dessinées par dessus les personnages
et n'ayant pas le même mouvement

@param  {dic}                 niveau      La config du niveau
@param  {Joueur}              joueur
@return {pygame.sprite.Group}
'''
def creationGroupeArmes(niveau, joueur) :
    groupe = pygame.sprite.Group()

    ent = niveau['ennemis'] + [joueur]
    if len(niveau['boss']) > 0 :
        ent += niveau['boss']

    for item in ent :
        groupe.add(item.arme)

    return groupe

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
    projectilesContactJ = pygame.sprite.spritecollide(etat.get('joueur'), etat.get('projectilesEnnemis'), True)
    for projectile in projectilesContactJ :
        etat.get('joueur').blessure(projectile.dommage) #on prend en compte les dommages

    #collsion des projectiles joueur vers obstacles
    projectilesContactO = pygame.sprite.groupcollide(etat.get('projectilesJoueur'), etat.get('obstacles'), True, False)
    for projectile in projectilesContactO: #On récupère les obstacles touchés et soustraction PV
        obstaclesTouches = projectilesContactO.get(projectile)
        for obstacle in obstaclesTouches :
            obstacle.blessure(projectile.dommage)

    #collision des projectiles joueur vers ennemis
    projectilesContactE = pygame.sprite.groupcollide(etat.get('projectilesJoueur'), etat.get('ennemis'), True, False)
    for projectile in projectilesContactE: #récup des ennemis touchés et soustraction PV
        ennemisTouches = projectilesContactE.get(projectile)
        for ennemi in ennemisTouches :
            ennemi.blessure(projectile.dommage)

    #destruction des projectiles du joueur et des ennemis en contact avec les bords
    #le jeu est trop facile sinon
    pygame.sprite.groupcollide(etat.get('projectilesJoueur'), etat.get('bords'), True, False)
    pygame.sprite.groupcollide(etat.get('projectilesEnnemis'), etat.get('bords'), True, False)

    #destruction des projectiles du joueur et des ennemis en contact avec les murs
    pygame.sprite.groupcollide(etat.get('projectilesJoueur'), etat.get('murs'), True, False)
    pygame.sprite.groupcollide(etat.get('projectilesEnnemis'), etat.get('murs'), True, False)

    return

'''
testCheckpoints

Test si le joueur est sur un checkpoint

@return {tuple | None}  Position du checkpoint ou None
'''
def testCheckpoints(etat) :
    check = pygame.sprite.spritecollide(etat.get('joueur'), etat.get('checkpoints'), False)
    if len(check) > 0 :
        for point in check :
            point.check = True
            return point.position()
    else :
        return None

'''
testPortails

Test si le joueur est sur un portail

@return {tuple | None}  Position du portail ou None
'''
def testPortails(etat) :
    contact = pygame.sprite.spritecollide(etat.get('joueur'), etat.get('portails'), False)
    if len(contact) > 0 :
        for point in contact:
            return point.suivant
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
def afficherVie(calque, vie, decalageX, decalageY, max = 100) :

    pygame.draw.rect(calque, (255, 0, 0), (10 + decalageX, 10 + decalageY, 1.5 * max, 8), 1)
    pygame.draw.rect(calque, (255, 0, 0), (10 + decalageX, 10 + decalageY, 1.5 * vie, 8))

