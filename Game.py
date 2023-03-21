import pygame, sys
from Variables import *
from classes import *
from Lost import *


MenuButton=Button(0,0,placeHolder,50,50)
def game():
    jumpdispo = True
    mur1=mur(placeHolder,0,20)
    mur2=mur(placeHolder,480,20)
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
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            if jumpdispo:
                isJumping = True
                jumpdispo = False
            else:
                isJumping = False
        else:
            isJumping = False
            if jumpdispo == False:
                jumpdispo = True
                isJumping = False
        Player1.mouvY(isJumping)
        if Player1.y>500:
            MenuLost()
        if MenuButton.drawClick():
            menu() 
        pygame.display.update()
        clock.tick(60)
