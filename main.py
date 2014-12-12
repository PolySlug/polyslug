#-*- coding: utf-8 -*-

import pygame
import datetime
import importlib
from   sys      import argv

from jeu         import gestionJeu
from lib.scores  import Scores

from niveaux.niveau import construireNiveau


'''
lesNiveaux

Le jeu peut gérer plusieurs niveaux.
Un niveau est découpé en sous-niveaux

@example :
    - niveau1
        - niveau1
        - niveau1_1
        - niveau1_2

Les sous-niveaux sont créés avec Tiled et exporté en json qu'on parse
@see http://www.mapeditor.org/

'''
lesNiveaux = ['niveau1', 'scores', 'menu']

#Notre DB de scores (veiller à ce que le fichier existe, même vide)
scores = Scores('scores.json')


pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 28) #defaut


f_width, f_height = 800, 600
img_chargement = pygame.image.load('img/chargement.png')


'''
lancerJeu

Lance un sous-niveau

@param  {Module}    niveau
@param  {String}    nomNiveau   Le nom de niveau pour l'enregistrement du score
@param  {foat}      temps       timestamp. Score du sous-niveau précédent
'''
def lancerJeu(niveau, nomNiveau = None, temps = 0) :

    if not nomNiveau :
        nomNiveau = niveau['nom']

    print("Niveau : " + nomNiveau)

    fenetre = pygame.display.set_mode((f_width, f_height))

    score, suivant = gestionJeu(fenetre, niveau, temps)

    #Si il y a une suite au sous-niveau
    if suivant :

        ecranChargement(fenetre)
        print("Niveau suivant : " + suivant)
        niveau = construireNiveau('niveaux/' + suivant)
        niveau['nom'] = suivant

        lancerJeu(niveau, nomNiveau, -score)

    #Niveau fini
    else :
        enregisterScore(temps + score, nomNiveau)


'''
ecranChargement

@param {pygame.Surface}  fenetre
'''
def ecranChargement(fenetre) :

    fenetre.blit(img_chargement, (0,0))
    pygame.display.flip()


'''
enregisterScore

Lance la procédure d'enregistrement du score
On est pas obligé de sauvegarder

@param {float}  score       Temps
@param {string} nomNiveau   Le nom du niveau
'''
def enregisterScore(score, nomNiveau) :

    choixSauvegarde = raw_input("Sauvegarde du score ? (o/O/y/Y/yep/*)")

    if choixSauvegarde in ['o', 'O', 'y', 'Y', 'yep'] :

        nom = raw_input("Pseudo :")

        scores.ajoutScore({
            'nom'    : nom,
            'temps'  : score,
            'niveau' : nomNiveau
            })

        lireScores()

    else :
        print("Score non sauvegardé")


'''
lireScores

Print les scores ordonnés dans la console
'''
def lireScores() :

    print("SCORES")

    tousScores = scores.lireScores(lesNiveaux)
    print(tousScores)

'''
main

Différentes options :
- scores : affiche les scores dans la console
- niveaux : afficher les niveaux dispo dans la console
- [nomNiveau] ou vide : lance le niveau nomNiveau ou le premier niveau par défaut
'''
def main() :


    if 'scores' in argv : #l'utilisateur veut simplement consulter les scores
        lireScores()

    elif 'niveaux' in argv : #l'utilisateur veut la liste des niveaux

        print("NIVEAUX")

        for n in lesNiveaux:
            print("- " + n)

    else : #l'utilisateur veut jouer

        pygame.mouse.set_visible(False)
        fenetre = pygame.display.set_mode((f_width, f_height))
        ecranChargement(fenetre)

        if len(argv) > 1 :  #on veut un niveau en particulier
            n = argv[1]
        else :              #defaut : menu
            n = 'menu'

        if n :
            niveau = construireNiveau('niveaux/' + n)
            if niveau :
                niveau['nom'] = n
                lancerJeu(niveau, n)
            else :
                print("Erreur avec le niveau demandé")

main()
