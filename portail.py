#-*- coding: utf-8 -*-

import pygame
from lib.sprites import Sprites

class Portail(pygame.sprite.Sprite) :
    sprite = Sprites("img/tiles_spritesheet.png")
    image = None
    imagesPortail =[]