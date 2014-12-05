#test de pygame.mouse
import pygame.display
from pygame.locals import *
from ecouteSouris import ecouteSouris

class Viseur():
		
	'''
	draw

	Dessine le viseur dans fen

	@param {Surface} fen
	'''
	def draw(self, fen):
		#Dessine 4 traits de longueur l=20px
		pygame.draw.line(fen, (0, 0, 0), (ecouteSouris()[0], ecouteSouris()[1]), (ecouteSouris()[0], ecouteSouris()[1]-20), 2)
		pygame.draw.line(fen, (0, 0, 0), (ecouteSouris()[0], ecouteSouris()[1]), (ecouteSouris()[0], ecouteSouris()[1]+20), 2)
		pygame.draw.line(fen, (0, 0, 0), (ecouteSouris()[0], ecouteSouris()[1]), (ecouteSouris()[0]-20, ecouteSouris()()[1]), 2)
		pygame.draw.line(fen, (0, 0, 0), (ecouteSouris()[0], ecouteSouris()[1]), (ecouteSouris()[0]+20, ecouteSouris()[1]), 2)
		#Dessine un cercle rouge de rayon r=4px
		pygame.draw.circle(fen, (255, 50, 50), (ecouteSouris()[0]+1, ecouteSouris()[1]+1), 4)
		pygame.display.flip()
