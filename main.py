
import pygame

from jeu import gestionJeu
from niveaux import niveau1

def main() :

    pygame.init()
    fenetre = pygame.display.set_mode((800, 600))

    gestionJeu(fenetre, niveau1.niveau)


main()
