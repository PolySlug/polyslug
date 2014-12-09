import pygame

#Initialisation
def sonSaut():
    pygame.mixer_music.load('sons/saut.ogg')
    pygame.mixer.music.stop()
    pygame.mixer.music.play()

def sonMort():
    pygame.mixer_music.load('sons/mort.ogg')
    pygame.mixer.music.stop()
    pygame.mixer.music.play()

def sonBlessureEnnemi():
    pygame.mixer_music.load('sons/blessureEnnemi.ogg')
    pygame.mixer.music.stop()
    pygame.mixer.music.play()

def sonBlessureJoueur():
    pygame.mixer_music.load('sons/blessureJoueur.ogg')
    pygame.mixer.music.stop()
    pygame.mixer.music.play()

def sonTir():
    pygame.mixer_music.load('sons/tir.ogg')
    pygame.mixer.music.stop()
    pygame.mixer.music.play()

def sonVictoire():
    pygame.mixer_music.load('sons/victory.ogg')
    pygame.mixer.music.stop()
    pygame.mixer.music.play()

