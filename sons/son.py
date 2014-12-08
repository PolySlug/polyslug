import pygame
from pygame.locals import *

#Initialisation
def sonSaut():

    pygame.mixer_music.load('sons/saut.ogg')
    pygame.mixer.music.stop()
    pygame.mixer.music.play()
    
def sonMort():
    pygame.mixer_music.load('sons/mort.ogg')
    pygame.mixer.music.stop()
    pygame.mixer.music.play()
    
def sonBlessureEnnemie ():
    pygame.mixer_music.load('sons/blessureEnnemie.ogg')
    pygame.mixer.music.stop()
    pygame.mixer.music.play()

def sonBlessureJoueur ():
    pygame.mixer_music.load('sons/blessureJoueur.ogg')
    pygame.mixer.music.stop()
    pygame.mixer.music.play()
    
def sonTire ():
    pygame.mixer_music.load('sons/tire.ogg')
    pygame.mixer.music.stop()
    pygame.mixer.music.play()
    
def sonVictoire ():
    pygame.mixer_music.load('sons/victory.ogg')
    pygame.mixer.music.stop()
    pygame.mixer.music.play()
    
    
'''
continuer = 1 #Variable de boucle
joue = 0 #1 si le son a ete mis en pause
pygame.mixer_music.load("saut.wav")
while continuer:
    for event in pygame.event.get():
                #Quitter
        if event.type == QUIT:
            continuer = 0
        
        #Lancer le son
        if event.type == KEYDOWN and event.key == K_SPACE and joue == 0:
            pygame.mixer.music.play()
            while pygame.mixer_music.get_busy():
                pass
            pygame.mixer.music.stop()
            joue = 0
        #Sortir de pause
        if event.type == KEYDOWN and event.key == K_SPACE and joue == 1:
            pygame.mixer.unpause()
        #Mettre en pause
        if event.type == KEYUP and event.key == K_SPACE:
            pygame.mixer.pause()
        #Stopper
        if event.type == KEYDOWN and event.key == K_RETURN:
            son.stop()
            joue = 0
'''