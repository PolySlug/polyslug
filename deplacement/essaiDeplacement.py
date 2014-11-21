#test de deplacement
import pygame

def ecouteTouche():
    done = False

    while not done:
     
        for event in pygame.event.get():
     
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    print ('q')
                elif event.key == pygame.K_d:
                    print ('d')
                elif event.key == pygame.K_z:
                    print ('z')
                elif event.key == pygame.K_s:
                    print ('s')
                elif event.key == pygame.K_ESCAPE:
                    print ('echap')
                elif event.key == pygame.K_SPACE:
                    print ('espace')
     
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    print ('q')
                elif event.key == pygame.K_d:
                    print ('d')
                elif event.key == pygame.K_z:
                    print ('z')
                elif event.key == pygame.K_s:
                    print ('s')
                elif event.key == pygame.K_ESCAPE:
                    print ('echap')
                elif event.key == pygame.K_SPACE:
                    print ('espace')
         
pygame.init()         
fenetre=pygame.display.set_mode((100, 100))
ecouteTouche()                             
    
