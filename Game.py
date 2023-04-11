import pygame, sys
from Variables import *
from classes import *
from Lost import *
from Functions import *

nombreDeCouloirs = 3
def creerMurs(nombreDeCouloirs):
    return 0

def game():
    hauteur = 0
    jumpdispo = True
    mur1=mur(placeHolder,0,20)
    mur2=mur(placeHolder,taille[1]-20,20)
    Player1=oiseau(oiseauImg,250,250,mur1,mur2)
    piques=[]


    #Initialisation des murs
    mursGauche = [murEtPics("Left"), murEtPics("Left")]
    mursDroit = [murEtPics("Right"), murEtPics("Right")]
    for i in range(2):
        mursGauche[i].yInit = -500 + (500*i)
        mursDroit[i].yInit = -500 + (500*i)
        mursDroit[i].y     = mursDroit[i].yInit
        mursGauche[i].y     = mursGauche[i].yInit

    from Menu import menu
    #Game Loop ------------------------------------------------------------
    while True:
        #Entrée joueur
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
        hauteur = Player1.mouvY(isJumping, hauteur)
        
        #Position murs, pics et collisions pics/joueur ////GAUCHE////    
        for murGauche in mursGauche:
            murGauche.y = murGauche.yInit + (hauteur % 500)
            iterateurPic = 0
            for i in range(10):
                if murGauche.picsPositions[i] == 1:
                    #POSITION PICS
                    murGauche.pics[iterateurPic].rect.y = murGauche.y + ((500/10)*i)
                    murGauche.pics[iterateurPic].y = murGauche.pics[iterateurPic].rect.y
                    murGauche.pics[iterateurPic].update("Left")
                    #COLLISION
                    for point in CirclePoints(Player1.rect.w/2, Player1.rect.center):
                        if inTriangle(murGauche.pics[iterateurPic].A,murGauche.pics[iterateurPic].B,murGauche.pics[iterateurPic].C, point)==True:
                            print(point)
                            print(Player1.x,Player1.y)
                            MenuLost()
                    #INCREMENTER L'ITERATEUR
                    iterateurPic += 1

                    
        for murDroit in mursDroit:
            murDroit.y = murDroit.yInit + (hauteur % 500)
            iterateurPic = 0
            for i in range(10):
                if murDroit.picsPositions[i] == 1:
                    #POSITION PICS
                    murDroit.pics[iterateurPic].rect.y = murDroit.y + ((500/10)*i)
                    murDroit.pics[iterateurPic].y = murDroit.pics[iterateurPic].rect.y
                    murDroit.pics[iterateurPic].update("Right")
                    #COLLISION
                    for point in CirclePoints(Player1.rect.w/2, Player1.rect.center):
                        if inTriangle(murDroit.pics[iterateurPic].A,murDroit.pics[iterateurPic].B,murDroit.pics[iterateurPic].C, point)==True:
                            print(point)
                            print(Player1.x,Player1.y)
                            MenuLost()
                    #INCREMENTER L'ITERATEUR
                    iterateurPic += 1

        



        #Display ------------------------------------------------------------
        screen.blit(Fond,(0,0))
        #Player1.mouvY(isJumping, )
        mur1.draw()
        mur2.draw()
        Player1.mouvX()
        for murGauche in mursGauche:
            for pic in murGauche.pics:
                pic.draw()
        for murDroit in mursDroit:
            for pic in murDroit.pics:
                pic.draw()
        Player1.draw()
        if Player1.y>500:
            MenuLost()
        
        pygame.display.update()
        clock.tick(60)
        #print(mursGauche[0].y)
        #print(mursGauche[1].y)
        print(mursGauche[1].pics[0].y)

