import pygame
from Buttons import Button
from pygame.locals import *
pygame.init()

taille = [500,500]

#Images---------------------------------------------------------------------------------------------------

#Background

Fond=pygame.image.load("sprites/Fond.png")
Fond2=pygame.image.load("sprites/FondFlou.png")
FondWin=pygame.image.load("sprites/FondWin.png")
#Sprites

placeHolder=pygame.image.load("sprites/placeHolder.png")
piqueImg=pygame.image.load("sprites/pique.png")
oiseauImg=pygame.image.load("sprites/oiseau.png")
oiseauImg = pygame.transform.scale(oiseauImg, (80, 80))
icon = pygame.image.load("sprites/oiseau.png")
nuageImg=pygame.image.load("sprites/nuage.png")
spaceShipImg=pygame.image.load("sprites/SpaceShip.png")
spaceShipImg = pygame.transform.scale(spaceShipImg, (100, 120))
spaceShipImg = pygame.transform.rotate(spaceShipImg, 90)

#Boutons
Jouer=pygame.image.load("sprites/Jouer.png")
Power=pygame.image.load("sprites/Power.png")
StartButton=Button(taille[0]/2.5,taille[1]/2.22,Jouer,taille[0]/5,taille[1]/10)
ExitButton=Button(taille[0]/1.15,taille[1]/50,Power,taille[0]/10,taille[1]/10)

#Autres-----------------------------------------------------------------------------------------------
hauteur = 0
plafond = taille[0]*2/5
screen = pygame.display.set_mode(taille)
clock=pygame.time.Clock()
rect = screen.get_rect()

#Text-----------------------------------------------------------------------------------------------

pixelfont=pygame.font.Font('Pixel.ttf',40)
pixelfont30=pygame.font.Font('Pixel.ttf',30)
scoreTexte=pixelfont.render((str(hauteur)), True, (255,255,255))
scoreTexteRect=scoreTexte.get_rect()
scoreTexteRect.center=(taille[0]/2, 50)
