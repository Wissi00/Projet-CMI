import pygame, sys
from Variables import *
MenuButtonLost=Button(225,225,placeHolder,50,50)

def MenuLost():
    from Menu import menu
    from Game import game
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
                sys.exit()
            pygame.display.update() 