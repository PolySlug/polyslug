#-*- coding: utf-8 -*-

import pygame
from projectileDroit import ProjectileDroit

class ProjectileDroitVert(ProjectileDroit):

    multi = 4 #plus rapide que projectileDroitRouge

    image = pygame.Surface((10, 10))
    pygame.draw.circle(image, (0, 255, 0), (5, 5), 5) #vert

