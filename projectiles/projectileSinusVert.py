#-*- coding: utf-8 -*-

import pygame
from projectileSinus import ProjectileSinus

#projectile suivant une courbe sinusoidale

class ProjectileSinusVert(ProjectileSinus):

    image = pygame.Surface((10, 10))
    pygame.draw.circle(image, (0,255,0), (5, 5), 5)
