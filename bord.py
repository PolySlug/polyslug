import pygame

class Bord(pygame.sprite.Sprite):
        
        def __init__(self, position, taille):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface(taille)
            self.rect = pygame.Rect(position, taille)
            
        def update(self, decalageX):
            self.rect.x += decalageX
        