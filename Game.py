import pygame, sys
from Variables import *
from classes import *
from Lost import *
from Functions import *


def game():
    jumpdispo = True
    mur1=mur(placeHolder,0,20)
    mur2=mur(placeHolder,taille[1]-20,20)
    mursGauche=[murEtPics(0),murEtPics(1),murEtPics(2)]
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
        Player1.rectpoints=[Player1.rect.topleft,Player1.rect.topright,Player1.rect.bottomleft,Player1.rect.bottomright,Player1.rect.center,Player1.rect.midtop,Player1.rect.midbottom,Player1.rect.midleft,Player1.rect.midright]
        for pique in piques:
            for point in Player1.rectpoints:
                if inTriangle(pique.A,pique.B,pique.C, point)==True:
                    MenuLost()
        for murGauche in mursGauche :
            #Remettre le mur en haut et générer de nouveaux pics
            if murGauche.y > 500:
                murGauche.y = -500
                murGauche.picsPositions = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                murGauche.pics = generationPics(murGauche.picsPositions, murGauche.cote)
            #Actualiser la hauteur des murs
            else:
                murGauche.y = murGauche.yInit + (hauteur%1000)
            #Pics---Affichage et collision
            for pique in murGauche.pics:
                #Actualiser la position des pics
                pique.y = 100
                #Collision
                for point in CirclePoints(Player1.rect.w/2, Player1.rect.center):
                    if inTriangle(pique.A,pique.B,pique.C, point)==True:
                        print(point)
                        print(Player1.x,Player1.y)
                        MenuLost()
                #Affichage
            for pique in murGauche.pics:
                pique.draw()
        for pique in piques:
            for point in CirclePoints(Player1.rect.w/2, Player1.rect.center):
                if inTriangle(pique.A,pique.B,pique.C, point)==True:
                    print(point)
                    print(Player1.x,Player1.y)
                    MenuLost()
        #Display ------------------------------------------------------------
        screen.blit(Fond,(0,0))
        Player1.mouvY(isJumping)
        mur1.draw()
        mur2.draw()
        Player1.mouvX()
        Player1.draw()
        pique1.draw()
        if Player1.y>500:
            MenuLost()
        pygame.display.update()
        clock.tick(60)
