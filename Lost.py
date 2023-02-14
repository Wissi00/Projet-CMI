import pygame, sys
from Variables import *
MenuButtonLost=Button(225,225,placeHolder,50,50)

def MenuLost():
    from Menu import menu
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
            screen.fill((255,255,255))
            if MenuButtonLost.drawClick():
                menu()
            if ExitButton.drawClick():
                print("Adieu")
                pygame.quit()
                sys.exit()
            pygame.display.update() 