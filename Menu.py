import pygame, sys
from Game import game
from Variables import *
pygame.init()

def menu():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
            screen.blit(Fond2,(0,0))
            if StartButton.drawClick():
                game()
            if ExitButton.drawClick():
                pygame.quit()
            pygame.display.update()
            clock.tick(60)

    