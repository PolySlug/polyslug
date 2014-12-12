
import pygame

from arme           import Arme
from lib.sprites    import Sprites
from projectiles.projectileDroitRouge import ProjectileDroitRouge
import math

class Arme1(Arme) :

    delai = 1000

    def __init__(self):

        self.sprites = Sprites('img/raygunPurple.png')
        self.image = self.imageDefaut = self.sprites.sprite((0,12), (56, 56))

        super(Arme1, self).__init__()

    def tirer(self, position, vecteur) :

        if pygame.time.get_ticks() - self.dernierTir > self.delai :

            super(Arme1, self).tirer(position, vecteur)

            '''
            On retourne un ou des projectiles

            Le tuple position est modifie afin de parametrer
            un cercle de rayon r=30px selon l'angle
            car on a besoin de faire sortir le projectile du canon de l'arme
            et non de la positionMain.
            Comme l'arme effectue une rotation sur elle meme
            et qu'elle est environ de rayon 30px, on a besoin d'utiliser
            l'expression d'un cercle
            '''
            return [ProjectileDroitRouge(
                (position[0]+30*((2*self.angle)/(1+self.angle*self.angle)),
                position[1]+20+30*((1-self.angle*self.angle)/(1+self.angle*self.angle))
                ),
                vecteur
            )]


        else :
            return []

