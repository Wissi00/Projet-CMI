import pygame, sys
from Variables import *
from classes import *
from Lost import *
from Functions import *


MenuButton=Button(0,0,placeHolder,50,50)
def game():
    jumpdispo = True
    mur1=mur(placeHolder,0,20)
    mur2=mur(placeHolder,480,20)
    Player1=oiseau(oiseauImg,250,250,mur1,mur2)
    piques=[]
    pique1=spike(300,"Left")
    piques.append(pique1)
    from Menu import menu
    #Game Loop ------------------------------------------------------------
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
        isJumping = pygame.key.get_pressed()[pygame.K_SPACE]
        Player1.mouvY(isJumping)
        if isJumping:
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
        for pique in piques:
            for point in CirclePoints(Player1.rect.w/2, Player1.rect.center):
                if inTriangle(pique.A,pique.B,pique.C, point)==True:
                    print(point)
                    print(Player1.x,Player1.y)
                    MenuLost()
        #Display ------------------------------------------------------------
        screen.fill((255,255,255))
        Player1.mouvY(isJumping)
        mur1.draw()
        mur2.draw()
        Player1.mouvX()
        Player1.draw()
        pique1.draw()
        if Player1.y>500:
            MenuLost()
        if MenuButton.drawClick():
            menu() 
        pygame.display.update()
        clock.tick(60)
