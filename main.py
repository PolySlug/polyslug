#-*- coding: utf-8 -*-

import pygame
import datetime
from   sys      import argv

from jeu        import gestionJeu
from niveaux    import niveau1
from lib.scores import Scores


scores = Scores('scores.json')


'''
main

'''
def main() :

    if 'scores' in argv : #l'utilisateur veut simplement consulter les scores
        lireScores()

    else :
        pygame.init()
        fenetre = pygame.display.set_mode((800, 600))

        score = gestionJeu(fenetre, niveau1.niveau)

        enregisterScore(score)


'''
enregisterScore

Lance la procédure d'enregistrement du score
On est pas obligé de sauvegarder

@param {float}  score   Temps
'''
def enregisterScore(score) :

    choixSauvegarde = raw_input("Sauvegarde du score ? (o/O/y/Y/yep/*)")

    if choixSauvegarde in ['o', 'O', 'y', 'Y', 'yep'] :

        nom = raw_input("Pseudo :")

        scores.ajoutScore({
            'nom'   : nom,
            'temps' : score
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

    for score in sorted(scores.lireScores(), key = lambda score: score['temps']) : #On tri les scores
        temps = datetime.datetime.fromtimestamp(score['temps']).strftime('%M:%S')
        print(score['nom'] + ' : ' + temps)


main()
