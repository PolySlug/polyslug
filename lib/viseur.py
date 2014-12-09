#test de pygame.mouse
import pygame.display
from ecouteSouris import ecouteSouris

class Viseur():

	'''
	draw

	Dessine le viseur dans fen

	@param {Surface} fen
	'''
	def draw(self, fen,decalageX):

            position = (ecouteSouris()[0]-int(decalageX),ecouteSouris()[1])

            #Dessine 4 traits de longueur l=20px
            pygame.draw.line(fen, (0, 0, 0), (position[0],position[1]), (position[0],position[1]-20), 2)
            pygame.draw.line(fen, (0, 0, 0), (position[0],position[1]), (position[0],position[1]+20), 2)
            pygame.draw.line(fen, (0, 0, 0), (position[0],position[1]), (position[0]-20,position[1]), 2)
            pygame.draw.line(fen, (0, 0, 0), (position[0],position[1]), (position[0]+20,position[1]), 2)
            #Dessine un cercle rouge de rayon r=4px
            pygame.draw.circle(fen, (255, 50, 50), (position[0]+1, position[1]+1), 4)
<<<<<<< HEAD
=======


			
>>>>>>> origin/clement/plateforme
