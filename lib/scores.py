#-*- coding:utf-8 -*-

import json

'''
Scores

Aide à la sauvegarde des scores sous format JSON
'''
class Scores():

    '''
    __init__

    Exemple : scores = Scores('scores.txt') *****

    @param {string}     fichier    path d'un fichier contenant les scores
                                   usuellement un .txt ou un .json
    '''
    def __init__(self, fichier) :
        self.fichier = fichier

    '''
    ajoutScore

    Ajoute un nouveau score dans le fichier
    @param {dic}    score   Dictionnaire à convertir en JSON
    '''
    def ajoutScore(self, score) : #score est un dictionnaire
        texte = open(self.fichier, 'a' )
        texte.write(json.dumps(score, ensure_ascii=False)+'\n')

    '''
    lireLignes

    pour chaque ligne du fichier, parser le JSON (un JSON = un score)
    mettre tous les scores dans un joli tableau qu'on retourne

    @return  {liste}    liste de dictionnaires
    '''
    def lireLignes(self):
        texte = open(self.fichier, 'r' )

        result = []
        for line in texte.readlines():
            result.append(json.loads(line))

        texte.close()
        return result


    '''
    lireScores

    @param  {Liste}  lesNiveaux  Liste des niveaux
    @return {dict}              les scores ordonnés par niveau et par temps
    '''
    def lireScores(self, lesNiveaux) :

        tousScores = self.lireScores()

        result = {}

        for n in lesNiveaux :
            scoresNiveau = [s for s in tousScores if s['niveau'] == n]

            result['n'] = []

            if len(scoresNiveau) == 0 :
                print("Pas de scores")
            else :
                for score in sorted(scoresNiveau, key = lambda score: score['temps']) : #On tri les scores
                    temps = datetime.datetime.fromtimestamp(score['temps']).strftime('%M:%S')

                    result['n'].append(score['nom'] + ' : ' + temps)

        return result
