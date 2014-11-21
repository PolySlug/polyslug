#test de pygame.mouse

import pygame.display

def recupCoor():
	(x, y) = pygame.mouse.get_pos()
	print("Position de la souris :"+ str(x) +"," + str(y))

def afficheEcran(fen):
	pygame.display.init()
	fen.fill((255, 255, 255))

fenetre = pygame.display.set_mode((800, 600))
afficheEcran(fenetre)
while True:
	recupCoor()
