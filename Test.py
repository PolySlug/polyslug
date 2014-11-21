#test de pygame.mouse
import pygame.display
from pygame.locals import *

class Viseur():

	def recupCoor(self):
		#Récupère la position (x, y) de la souris
		return pygame.mouse.get_pos()
		

	def draw(self, fen, x, y):
		#Dessine 4 traits de longueur l=20px
		pygame.draw.line(fen, (0, 0, 0), (recupCoor()[0], recupCoor()[1]), (recupCoor()[0], recupCoor()[1]-20), 2)
		pygame.draw.line(fen, (0, 0, 0), (recupCoor()[0], recupCoor()[1]), (recupCoor()[0], recupCoor()[1]+20), 2)
		pygame.draw.line(fen, (0, 0, 0), (recupCoor()[0], recupCoor()[1]), (recupCoor()[0]-20, recupCoor()[1]), 2)
		pygame.draw.line(fen, (0, 0, 0), (recupCoor()[0], recupCoor()[1]), (recupCoor()[0]+20, recupCoor()[1]), 2)
		#Dessine un cercle rouge de rayon r=4px
		pygame.draw.circle(fen, (255, 50, 50), (recupCoor()[0]+1, recupCoor()[1]+1), 4)
		pygame.display.flip()


def afficheEcran(fen):
	pygame.display.init()
	fen.fill((255, 255, 255))
	pygame.display.flip()

fenetre = pygame.display.set_mode((800, 600))
pygame.mouse.set_visible(False)
while True:
	pygame.time.wait(60)
	Viseur.draw(fenetre)

