#-*- coding: utf-8 -*-

import pygame
from projectileDroit import ProjectileDroit

#projectile allant en ligne droite

class ProjectileDroitRouge(ProjectileDroit):

    image = pygame.Surface((10, 10))
    pygame.draw.circle(image, (255,0,0), (5, 5), 5)
