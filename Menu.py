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
            screen.fill((255,255,255))
            if StartButton.drawClick():
                game()
            if ExitButton.drawClick():
                print("Exit")
            pygame.display.update()

    