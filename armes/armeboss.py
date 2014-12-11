
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
        self.image = self.imageNonDim = pygame.transform.scale(self.imageNonDim, (tailleimage[0]*2, tailleimage[1]*2))


        super(Arme1, self).__init__()

    def tirer(self, position, vecteur) :

        if pygame.time.get_ticks() - self.dernierTir > self.delai :

            super(ArmeBoss, self).tirer(position, vecteur)
            return [ProjectileDroitRouge(position, vecteur)]

        else :
            return []
