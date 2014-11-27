import pygame

pygame.init()
screen = pygame.display.set_mode((468, 60))


background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((170, 100, 50))


if pygame.font:
    font = pygame.font.Font(None, 36)
    text = font.render("Test de Texte OK !", 1, (250, 250, 250))
    textpos = text.get_rect(centerx=background.get_width()/2)
    background.blit(text, textpos)
    
screen.blit(background, (0, 0))
pygame.display.flip()
pygame.time.wait(4000)