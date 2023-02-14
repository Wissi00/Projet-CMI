import pygame, sys
from Variables import *
from classes import *

MenuButton=Button(0,0,placeHolder,50,50)

def game():
    Player1=oiseau(oiseauImg,250,250)
    from Menu import menu
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
            screen.fill((255,255,255))
            Player1.draw()
            if MenuButton.drawClick():
                menu()
            pygame.display.update()