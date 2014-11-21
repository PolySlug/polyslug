import pygame
pygame.mixer.init()
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

pygame.mixer.music.load('C:\Users\lj.Gaelle\Music\test.mp3)
pygame.mixer.music.play()
import pysic