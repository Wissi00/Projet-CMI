import pygame, sys
from Variables import *

def MenuWin():
    from Game import game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
        screen.blit(Fond2,(0,-1500))
        if StartButton.drawClick():
            game()
        if ExitButton.drawClick():
            pygame.quit()
            sys.exit()
        pygame.display.update()