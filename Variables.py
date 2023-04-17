import pygame
from Buttons import Button
from pygame.locals import *
pygame.init()

taille = [500,500]

#Images---------------------------------------------------------------------------------------------------

#Background

Fond=pygame.image.load("sprites/FondA.png")
Fond2=pygame.image.load("sprites/FondA2.png")
#Sprites

placeHolder=pygame.image.load("sprites/placeHolder.png")
piqueImg=pygame.image.load("sprites/pique.png")
oiseauImg=pygame.image.load("sprites/oiseau.png")
oiseauImg = pygame.transform.scale(oiseauImg, (80, 80))
icon = pygame.image.load("sprites/oiseau.png")

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
scoreTexte=pixelfont.render((str(hauteur)), True, (255,255,255))
scoreTexteRect=scoreTexte.get_rect()
scoreTexteRect.center=(taille[0]/2, 50)
