import pygame, sys
from Variables import *
from classes import *
from Lost import *


MenuButton=Button(0,0,placeHolder,50,50)

def game():
    mur1=mur(placeHolder,0,20)
    mur2=mur(placeHolder,480,20)
    mur3=mur(placeHolder,200,20)
    Player1=oiseau(oiseauImg,250,250,mur1,mur2)
    from Menu import menu
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    MenuLost()
        screen.fill((255,255,255))
        mur1.draw()
        mur2.draw()
        Player1.mouvX()
        Player1.draw()
        isJumping = 0
        Player1.mouvY(isJumping)
        if MenuButton.drawClick():
            menu() 
        pygame.display.update()
        clock.tick(120)
