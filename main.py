#-*- coding: utf-8 -*-

import pygame
import datetime
import importlib
from   sys      import argv

from jeu         import gestionJeu
from lib.scores  import Scores

from niveaux.niveau import construireNiveau


lesNiveaux = ['niveau1']

#Notre DB de scores (veiller à ce que le fichier existe, même vide)
scores = Scores('scores.json')

pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 28) #defaut

f_width, f_height = 800, 600
img_chargement = pygame.image.load('img/chargement.png')

'''
lancerJeu

Lance un niveau

@param  {Module}    niveau
@param  {String}    nomNiveau   Le nom de niveau pour l'enregistrement du score
@param  {foat}      temps       timestamp. Score du sous-niveau précédent
'''
def lancerJeu(niveau, nomNiveau = None, temps = 0) :

    nomNiveau = niveau['nom']

    print("Niveau : " + nomNiveau)

    fenetre = pygame.display.set_mode((f_width, f_height))

    score, suivant = gestionJeu(fenetre, niveau, temps)

    if suivant :

        del niveau #FIXME : ça fait quelque chose ?

        ecranChargement(fenetre)
        print("Niveau suivant : " + suivant)
        niveau = construireNiveau('niveaux/' + suivant)
        niveau['nom'] = suivant

        lancerJeu(niveau, nomNiveau, -score)

    else :
        enregisterScore(temps + score, nomNiveau)


'''
ecranChargement
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

    tousScores = scores.lireScores()

    for n in lesNiveaux :
        scoresNiveau = [s for s in tousScores if s['niveau'] == n]

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

    pygame.mouse.set_visible(False)

    if 'scores' in argv : #l'utilisateur veut simplement consulter les scores
        lireScores()

    elif 'niveaux' in argv : #l'utilisateur veut la liste des niveaux

        print("NIVEAUX")

        for n in lesNiveaux:
            print("- " + n)

    else : #l'utilisateur veut jouer

        fenetre = pygame.display.set_mode((f_width, f_height))
        ecranChargement(fenetre)

        if len(argv) > 1 :              #on veut un niveau en particulier
            if argv[1] in lesNiveaux :
                n = argv[1]
            else : #on a pas ce niveau en stock
                print("Pas de niveau " + argv[1] + ". Essayer la commande `niveaux`")
                n = None
        else : #defaut : premier niveau
            n = 'menu' #TODO : temp

        if n :
            niveau = construireNiveau('niveaux/' + n)
            niveau['nom'] = n

            lancerJeu(niveau, n)

main()
