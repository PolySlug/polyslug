
from pygame.sprite import Group

'''
gestionJeu

@param {Liste} murs         Une liste d'instances de murs
@param {Liste} obstacles    Une liste d'instances d'obstacles
@param {Liste} ennemis      Une liste d'instances d'ennemis
@param {Liste} joueur       Une instance joueur
'''
def gestionJeu(murs, obstacles, ennemis, joueur):

    groupeMurs      = creationGroupe(murs)
    groupeObstacles = creationGroupe(obstacles)
    groupeEnnemis   = creationGroupe(ennemis)

    #groupeJeu       = creationGroupe(murs + obstacles + ennemis)

    done = False
    while not done :



    return


def creationGroupe(items):
    return Group(*items)
