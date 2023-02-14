import pygame, sys
from Variables import *
MenuButton=Button(0,0,placeHolder,50,50)


def game():
    from Menu import menu
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
            screen.fill((255,255,255))
            if MenuButton.drawClick():
                menu()
            pygame.display.update()