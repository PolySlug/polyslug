#-*- coding: utf-8 -*-

import pygame
import datetime
import importlib
from   sys      import argv

from jeu         import gestionJeu
from lib.scores  import Scores
from lib.inspect import recupererSousModules

import niveaux


#Notre DB de scores (veiller à ce que le fichier existe, même vide)
scores = Scores('scores.json')

'''
lancerJeu

Lance un niveau

@param  {Module}    niveau
@param  {String}    nomNiveau   Le nom de niveau pour l'enregistrement du score
'''
def lancerJeu(niveau, nomNiveau) :

    pygame.init()
    fenetre = pygame.display.set_mode((800, 600))

    score = gestionJeu(fenetre, niveau.niveau)

    enregisterScore(score, nomNiveau)


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

    lesNiveaux = recupererSousModules(niveaux)

    for n in lesNiveaux :
        scoresNiveau = [s for s in scores.lireScores() if s['niveau'] == n]

        print('Niveau : ' + n)

        if len(scoresNiveau) == 0 :
            print("Pas de scores")
        else :
            for score in sorted(scoresNiveau, key = lambda score: score['temps']) : #On tri les scores
                temps = datetime.datetime.fromtimestamp(score['temps']).strftime('%M:%S')
                print(score['nom'] + ' : ' + temps)


'''
main

Différentes options :
- scores : affiche les scores
- niveaux : afficher les niveaux dispo
- [nomNiveau] ou vide : lance le niveau nomNiveau ou le premier niveau par défaut
'''
def main() :

    if 'scores' in argv : #l'utilisateur veut simplement consulter les scores
        lireScores()

    elif 'niveaux' in argv : #l'utilisateur veut la liste des niveaux

        print("NIVEAUX")

        for n in recupererSousModules(niveaux):
            print("- " + n)

    else : #l'utilisateur veut jouer

        lesNiveaux = recupererSousModules(niveaux)

        if len(argv) > 1 :              #on veut un niveau en particulier
            if argv[1] in lesNiveaux :
                n = argv[1]
            else : #on a pas ce niveau en stock
                print("Pas de niveau " + argv[1] + ". Essayer la commande `niveaux`")
                n = None
        else : #defaut : premier niveau
            n = lesNiveaux[0]

        if n :
            niveau = importlib.import_module('niveaux.' + n)
            lancerJeu(niveau, n)

main()
