import pygame
pygame.init()
screen = pygame.display.set_mode((468, 150))

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((170, 100, 50))
#***********************************************
fond = background #image de fond
joueur = pygame.Surface((20,20))
joueur.fill((0, 200, 50))

fond.blit(joueur, (0,0))
screen.blit(fond,(0,0))

pygame.time.wait(3000)
