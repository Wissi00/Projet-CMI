import pygame, sys
from Buttons import Button
from Game import game
from Variables import *
pygame.init()
StartButton=Button(200,225,placeHolder,100,50)
ExitButton=Button (425,10,placeHolder,50,50)
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


menu()


    