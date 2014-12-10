import pygame

pygame.mixer.init()

sons = []

#Initialisation
def sonSaut():
    son = pygame.mixer.Sound('sons/saut.ogg')
    son.play()
    sons.append(sons)

def sonMort():
    son = pygame.mixer.Sound('sons/mort.ogg')
    son.play()
    sons.append(sons)

def sonBlessureEnnemi():
    son = pygame.mixer.Sound('sons/blessureEnnemi.ogg')
    son.play()
    sons.append(sons)

def sonBlessureJoueur():
    son = pygame.mixer.Sound('sons/blessureJoueur.ogg')
    son.play()
    sons.append(sons)

def sonTir():
    son = pygame.mixer.Sound('sons/tir.ogg')
    son.set_volume(0.5)
    son.play()
    sons.append(sons)

def sonVictoire():
    son = pygame.mixer.Sound('sons/victory.ogg')
    son.play()
    sons.append(sons)
