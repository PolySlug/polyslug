
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
        images = [
                [(0, 0), (66, 90)],
                [(66, 0), (66, 90)],
                [(132, 0), (67, 90)],
                [(0, 93), (66, 90)],
                [(66, 93), (66, 90)],
                [(132, 93), (72, 90)],
                [(0, 186), (70, 90)]
                ]

        self.framesDroites = self.sprites.sprites(images)
        self.framesGauches = self.sprites.sprites(images, flip = True)

        self.image = self.framesDroites[0]

        super(Joueur, self).__init__(position)

    def update(self, niveau = {}) :

        self.rect.x += self.vitesse_x

        if self.vitesse_x > 0 :
            self.image = self.framesDroites[(self.rect.x // 30) % len(self.framesDroites)]
        elif self.vitesse_x < 0 :
            self.image = self.framesGauches[(self.rect.x // 30) % len(self.framesGauches)]
        else :
            self.image = self.framesDroites[0]


    def deplacementX(self, vitesse) :
        self.vitesse_x = vitesse

