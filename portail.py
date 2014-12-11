
import pygame
from lib.sprites import Sprites

class Portail(pygame.sprite.Sprite) :

    sprite = Sprites("img/tiles.png")
    image = self.sprite.sprite((280, 280), (70, 70))

    def __init__(self, position, suivant) :

        pygame.sprite.Sprite.__init__(self)

        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = position

        self.suivant = suivant
