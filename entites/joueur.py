
from entite      import Entite
from lib.sprites import Sprites
#TODO import armes


class Joueur(Entite):

    vitesse_x = 0
    vitesse_y = 0

    vie     = 100

    sprites = Sprites('img/p1_walk.png')
    frames  = []

    def __init__(self, position) :

        #Test images mouvement
        image = self.sprites.sprite((0, 0), (66, 90))
        self.frames.append(image)
        image = self.sprites.sprite((66, 0), (66, 90))
        self.frames.append(image)
        image = self.sprites.sprite((132, 0), (67, 90))
        self.frames.append(image)
        image = self.sprites.sprite((0, 93), (66, 90))
        self.frames.append(image)
        image = self.sprites.sprite((66, 93), (66, 90))
        self.frames.append(image)
        image = self.sprites.sprite((132, 93), (72, 90))
        self.frames.append(image)
        image = self.sprites.sprite((0, 186), (70, 90))
        self.frames.append(image)

        self.image = self.frames[0]

        super(Joueur, self).__init__(position)

    def update(self, niveau = {}) :

        self.rect.x += self.vitesse_x

        if self.vitesse_x :
            self.image = self.frames[(self.rect.x // 30) % len(self.frames)]
        else :
            self.image = self.frames[0]


    def deplacementX(self, vitesse) :
        self.vitesse_x = vitesse

