#-*- coding: utf-8 -*-

import json
import importlib


'''
Parser

Parse un export JSON de Tiled
et couvertit les tiles qui ont des propriétés spéciales en entités du Jeu
'''


#Appartenance classe / groupe pour envoi final des données
groupes  = {
    'ennemis'     : ['Ennemi1', 'Ennemi2', 'Ennemi3', 'Ennemi4'],
    'murs'        : ['Mur', 'Plateforme'],
    'obstacles'   : ['Obstacle1', 'Obstacle2', 'Obstacle3'],
    'checkpoints' : ['Checkpoint'],
    'portails'    : ['Portail'],
    'joueur'      : ['Joueur'],
    'boss'        : ['Boss']
}


#les entités de ces groupes sont dynamiques,
#on ne leur passe pas d'image à découper
dynamiques = ['ennemis', 'checkpoints', 'joueur', 'boss', 'obstacles']


'''
groupe

@return {str|None}   le groupe de `classe` ou None
'''
def groupe(classe) :

    for k, v in groupes.items() :
        if classe in v :
            return k

    return None


'''
constructionTiles

Pour chaque tile avec paramètres spéciaux,
construire leur propriétés

@param {dict}   data    L'export JSON de Tiled
'''
def constructionTiles(data) :

    tiles = {}

    #Pour toutes les png
    for tileset in data['tilesets'] :

        setId = tileset['firstgid']

        image = 'img/' + tileset['name'] + '.png'

        tileHeight = tileset['tileheight']
        tileWidth  = tileset['tilewidth']

        margin  = tileset['margin']
        spacing = tileset['spacing']

        gridWidth  = tileset['imagewidth'] / tileWidth
        gridHeight = tileset['imageheight'] / tileHeight
        grid       = gridWidth * gridHeight

        if 'tileproperties' in tileset :
            for t, val in tileset['tileproperties'].items() :
                id = setId + int(t)

                i = int(t) % gridWidth
                j = int(t) // gridWidth

                if 'class' in val :
                    classe = val['class']
                else :
                    classe = None

                if 'suivant' in val :
                    suivant = val['suivant']
                else:
                    suivant = None

                if 'nom' in val :
                    nom = val['nom']
                else:
                    nom = None


                #on en déduit les paramètres du tile
                tiles[id] = {
                    'image' : image,
                    'rect'  : {
                        'x'     : margin + i * tileWidth + spacing * i,
                        'y'     : margin + j * tileHeight + spacing * j,
                        'width' : tileWidth,
                        'height': tileHeight
                        },
                    'classe'  : classe,
                    'groupe'  : groupe(classe),
                    'suivant' : suivant,
                    'nom'     : nom
                }


    #with open('lib/data.json', 'w') as outfile:
        #json.dump(tiles, outfile)

    return tiles


'''
recupererCalquePrincipal

@param  {dict}   data    l'export de JSON de Tiled
@return {dict}           l'extrait du JSON correpondant au calque 'principal'
'''
def recupererCalquePrincipal(data) :

    for l in data['layers'] :
        if l['name'] in ['Principal', 'principal'] :
            return l

'''
importClass

@param  {str}   groupe  Le groupe de la sprite
@param  {str}   classe  Le nom de la classe
return  {Class}         Une classe issue des modules d'entités, checkpoint, etc.
'''
def importClass(groupe, classe):

    if groupe not in ['ennemis', 'obstacles', 'boss', 'murs', 'joueur'] :
        module = importlib.import_module(classe.lower())
    else :
        module = importlib.import_module('entites.' + classe.lower())

    return getattr(module, classe)


'''
construction

@param  {dict}  calque      Le calque de travail (principal)
@param  {dict}  tiles       Les infos sur les tiles construites par constructionTiles()
@param  {int}   tileWidth
@param  {int}   tileHeight
'''
def construction(calque, tiles, tileWidth, tileHeight):

    #L'objet à retourner
    niveau = {
        'murs':        [],
        'obstacles':   [],
        'plateformes': [],
        'ennemis':     [],
        'boss':        [],
        'checkpoints': [],
        'portails':    [],
        'joueur':      [],
        'width':       0,  #longueur du niveau en px
        'height':      0   #hauteur du niveau en px
    }

    layerWidth  = calque['width']
    layerHeight = calque['height']

    #Pour chaque case de la grille
    for index, item in enumerate(calque['data']) :

        #Si c'est un tile connu
        if item != 0 and item in tiles:

            tile   = tiles[item]
            groupe = tile['groupe']
            classe = tile['classe']

            #On calcul la position du tile dans la grille
            i = (index % layerWidth) * tileWidth
            j = (index // layerWidth) * tileHeight

            #On instancie les entités
            if groupe in niveau :

                if classe == "Joueur" :
                    instance = (i,j)
                elif classe == "Portail" :
                    instance = importClass(groupe, classe)((i,j), tile['suivant'], tile['nom'])
                elif groupe in dynamiques :
                    instance = importClass(groupe, classe)((i,j))
                else :
                    instance = importClass(groupe, classe)((i,j), tile['image'], tile['rect'])

                niveau[groupe].append(instance)

    return niveau


'''
genererNiveau

Parse le fichier JSON exporté par Tiled

@param  {str} fichier  Le fichier contenant le JSON
@return {dict}         Une structure de niveau
'''
def genererNiveau(fichier) :

    print("Construction niveau :")

    contenu = open(fichier, 'r' ).read()

    data = json.loads(contenu)

    print("- les éléments")
    tiles = constructionTiles(data)
    tileWidth  = data['tilewidth']
    tileHeight = data['tileheight']

    print("- les positions")
    principal = recupererCalquePrincipal(data)

    width  = data['width'] * tileWidth
    height = data['height'] * tileHeight

    if not principal :
        print("Pas de calque principal")
        return None
    else :
        print("- instanciation")
        niveau           = construction(principal, tiles, tileWidth, tileHeight)
        niveau['width']  = width
        niveau['height'] = height

        return niveau


