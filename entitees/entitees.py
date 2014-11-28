
import pygame

class Entite(pygame.sprite.Srite) :

    self.vie = 100

    def __init__(self, position) :
        self.position = position

    def update(self) :
        pass

    def draw(self, calque):
        pass

    def blessure(self, vie):
        self.vie -= vie
        return self.vie

