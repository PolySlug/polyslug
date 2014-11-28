import json

class Scores():
    
    '''
    __init__
    ouverture du fichier (txt) et attacher le fichier a self
    *****    scores = Scores('scores.txt') *****
    @param {class}    score
    @param {file}     fichier    utilisation d'un fichier *.txt contenant les scores
    '''
    def __init__(self, fichier) :
        self.fichier = fichier

    '''
    ajoutScore
    
    self.texte = open(fichier)
    convertir le dictionnaire en JSON, ajouter la nouvelle ligne dans le fichier
    '''
    def ajoutScore(self, score) : #score est un dictionnaire
        texte = open(self.fichier, 'a' )
        texte.write(json.dumps(score, ensure_ascii=False)+'\n') 
        
    '''
    pour chaque ligne du fichier, parser le JSON (un JSON = un score)
    mettre tous les scores dans un joli tableau qu'on retourne    
    '''
        
    def lireScores(self):
        texte = open(self.fichier, 'r' )
        
        result = []
        for line in texte.readlines():
            print(line)
            result.append(json.loads(line))
            
        texte.close()
        return result
   
    




