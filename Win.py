import pygame, sys
from Variables import *

def MenuWin():
    from Game import game
    gagnezText=pixelfont30.render(("Bravo vous avez gagnez!"), True, (255,255,255))
    gagnezTextRect=gagnezText.get_rect()
    gagnezTextRect.center=(taille[0]/2, 350)
    goatText=pixelfont30.render(("Vous faites partie des GOATS!"), True, (255,255,255))
    goatTextRect=goatText.get_rect()
    goatTextRect.center=(taille[0]/2, 400)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
        screen.blit(FondWin,(0,0))
        screen.blit(gagnezText,gagnezTextRect)
        screen.blit(goatText,goatTextRect)
        if StartButton.drawClick():
            game()
        if ExitButton.drawClick():
            pygame.quit()
            sys.exit()
        pygame.display.update()