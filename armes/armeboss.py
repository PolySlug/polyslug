
import pygame

from arme           import Arme
from lib.sprites    import Sprites
from projectiles.projectileDroitRouge import ProjectileDroitRouge


class ArmeBoss(Arme) :

    delai = 1000

    def __init__(self):

        self.sprites = Sprites('img/raygunPurple.png')
        self.imageNonDim = self.imageDefautNonDim = self.sprites.sprite((0,12), (56, 56))
        tailleimage = self.imageNonDim.get_size()
        self.image = self.imageDefaut = pygame.transform.scale(self.imageNonDim, (tailleimage[0]*2, tailleimage[1]*2))

        super(ArmeBoss, self).__init__()


    def tirer(self, position, vecteur) :

        if pygame.time.get_ticks() - self.dernierTir > self.delai :

            super(ArmeBoss, self).tirer(position, vecteur)
            return [ProjectileDroitRouge((position[0]+30*((2*self.angle)/(1+self.angle*self.angle)), position[1]+20+30*((1-self.angle*self.angle)/(1+self.angle*self.angle))), vecteur)] #cf arme1

        else :
            return []
