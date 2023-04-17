import pygame, sys
from Variables import *
MenuButtonLost=Button(225,225,placeHolder,50,50)

def MenuLost(hauteur):
    from Menu import menu
    from Game import game
    scoreTexte=pixelfont.render(("Score : "+str(int(hauteur//100))), True, (255,255,255))
    scoreTexteRect=scoreTexte.get_rect()
    scoreTexteRect.center=(taille[0]/2, 50)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
        screen.blit(Fond2,(0,-1500))
        screen.blit(scoreTexte,scoreTexteRect)
        if StartButton.drawClick():
            game()
        if ExitButton.drawClick():
            pygame.quit()
            sys.exit()
        pygame.display.update()
