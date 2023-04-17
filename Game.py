import pygame, sys
from Variables import *
from classes import *
from Lost import *
from Functions import *
from Score import *
from Win import *


def game():
    hauteur = 0
    scroll = -1500
    jumpdispo = True
    mur1=mur(placeHolder,0,20)
    mur2=mur(placeHolder,taille[1]-20,20)
    Player1=oiseau(oiseauImg,250,250,mur1,mur2)
    nuage1x=200
    nuage2x=600


    #Initialisation des murs
    mursGauche = [murEtPics("Left"), murEtPics("Left")]
    mursDroit = [murEtPics("Right"), murEtPics("Right")]
    for i in range(2):
        mursGauche[i].yInit = 0 + (-taille[1] * i)
        mursDroit[i].yInit = 0 + (-taille[1] * i)
        mursDroit[i].y     = mursDroit[i].yInit
        mursGauche[i].y     = mursGauche[i].yInit
    yPremierMurFramePrecedente = mursDroit[0].y
    ySecondMurFramePrecedente = mursDroit[1].y

    from Menu import menu
    #Game Loop ------------------------------------------------------------
    while True:
        scoreTexte=pixelfont.render((str(int(hauteur)//100)), True, (255,255,255))
        if scroll>=0:
            MenuWin()
        scroll=-1500+hauteur/10
        nuage1Scroll=150+hauteur/10
        nuage2Scroll=-200+hauteur/10
        #RÉINITIALISATION DES PICS, GÉNÉRATION DE NOUVEAUX PICS
        if yPremierMurFramePrecedente > mursDroit[0].y:
            mursDroit[0].picsPositions = generationPiquesPosition(hauteur=hauteur)
            mursDroit[0].pics = generationPics(mursDroit[0].picsPositions, "Right")
            mursGauche[0].picsPositions = generationPiquesPosition(hauteur=hauteur)
            mursGauche[0].pics = generationPics(mursGauche[0].picsPositions, "Left")
        if ySecondMurFramePrecedente > mursDroit[1].y:
            mursDroit[1].picsPositions = generationPiquesPosition(hauteur=hauteur)
            mursDroit[1].pics = generationPics(mursDroit[1].picsPositions, "Right")
            mursGauche[1].picsPositions = generationPiquesPosition(hauteur=hauteur)
            mursGauche[1].pics = generationPics(mursGauche[1].picsPositions, "Left")
        ySecondMurFramePrecedente = mursDroit[1].y
        yPremierMurFramePrecedente = mursDroit[0].y

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
        #CALCUL DISTANCE VERTICALE PARCOURUE
        hauteur = Player1.mouvY(isJumping, hauteur)
        

        #POSITION MURS
        mursDroit[1].y = mursDroit[1].yInit + (hauteur % (taille[1]*2))
        if (mursDroit[1].y < mursDroit[1].yInit + taille[1]):
            mursDroit[0].y = mursDroit[1].y + taille[1]
        else:
            mursDroit[0].y = mursDroit[1].y - taille[1]
        mursGauche[0].y = mursDroit[0].y
        mursGauche[1].y = mursDroit[1].y

        Player1.mouvX()
        #Position pics et collisions pics/joueur   
        for murGauche in mursGauche:
            iterateurPic = 0
            for i in range(10):
                if murGauche.picsPositions[i] == 1:
                    #POSITION PICS
                    murGauche.pics[iterateurPic].rect.y = murGauche.y + ((taille[1]/10)*i)
                    murGauche.pics[iterateurPic].y = murGauche.pics[iterateurPic].rect.y
                    murGauche.pics[iterateurPic].update("Left")
                    #COLLISION
                    for point in CirclePoints(Player1.rect.w/2, Player1.rect.center):
                        if inTriangle(murGauche.pics[iterateurPic].A,murGauche.pics[iterateurPic].B,murGauche.pics[iterateurPic].C, point)==True:
                            print(point)
                            print(Player1.x,Player1.y)
                            MenuLost(hauteur)
                    #INCREMENTER L'ITERATEUR
                    iterateurPic += 1             
        for murDroit in mursDroit:
            iterateurPic = 0
            for i in range(10):
                if murDroit.picsPositions[i] == 1:
                    #POSITION PICS
                    murDroit.pics[iterateurPic].rect.y = murDroit.y + ((taille[1]/10)*i)
                    murDroit.pics[iterateurPic].y = murDroit.pics[iterateurPic].rect.y
                    murDroit.pics[iterateurPic].update("Right")
                    #COLLISION
                    for point in CirclePoints(Player1.rect.w/2, Player1.rect.center):
                        if inTriangle(murDroit.pics[iterateurPic].A,murDroit.pics[iterateurPic].B,murDroit.pics[iterateurPic].C, point)==True:
                            print(point)
                            print(Player1.x,Player1.y)
                            MenuLost(hauteur)
                    #INCREMENTER L'ITERATEUR
                    iterateurPic += 1
        if Player1.y>taille[1]:
            MenuLost(hauteur)




        #Display ------------------------------------------------------------
        screen.blit(Fond,(0,scroll))
        screen.blit(nuageImg,(nuage1x,nuage1Scroll))
        screen.blit(nuageImg,(nuage2x,nuage2Scroll))
        nuage1x+=1
        nuage2x-=1
        mur1.draw()
        mur2.draw()
        for murGauche in mursGauche: #dessin des pics gauche
            for pic in murGauche.pics:
                pic.draw()
        for murDroit in mursDroit: #dessin des pics droit
            for pic in murDroit.pics:
                pic.draw()
        screen.blit(scoreTexte,scoreTexteRect) #affichage du score
        Player1.draw()
        
        pygame.display.update()
        clock.tick(60)

