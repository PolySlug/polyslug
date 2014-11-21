import pygame

screen = pygame.display.set_mode(300, 100)

class Platform() :

    fond = pygame.image.load("background_01.png")

    decalageX = 0


    def __init__(self) :
        pass

    def swift_world(self, decalage) :

        self.decalageX += decalage

    def draw(self, screen) :

        screen.fill("blue")
        screen.blit(fond, (self.decalageX // 3, 100)


platform = Platform()


