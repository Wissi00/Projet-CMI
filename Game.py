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
        Player1.rectpoints=[Player1.rect.topleft,Player1.rect.topright,Player1.rect.bottomleft,Player1.rect.bottomright,Player1.rect.center,Player1.rect.midtop,Player1.rect.midbottom,Player1.rect.midleft,Player1.rect.midright]
        for pique in piques:
            for point in Player1.rectpoints:
                if inTriangle(pique.A,pique.B,pique.C, point)==True:
                    MenuLost()
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
        Player1.mouvY(isJumping)
        #Display ------------------------------------------------------------
        screen.fill((255,255,255))
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
