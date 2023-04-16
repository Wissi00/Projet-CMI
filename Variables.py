import pygame
from Buttons import Button
from PIL import Image
from pygame.locals import *
pygame.init()

taille = [500,500]
fond = Image.open("sprites/Fond.png")
fond = fond.resize((taille[0], taille[1]))
fond.save("sprites/Fondr.png")
fond2 = Image.open("sprites/Fond2.png")
fond2 = fond2.resize((taille[0], taille[1]))
fond2.save("sprites/Fond2r.png")

hauteur = 0
plafond = taille[0]*2/5
screen = pygame.display.set_mode(taille)
pixelfont=pygame.font.Font('Pixel.ttf',40)
scoreTexte=pixelfont.render((str(hauteur)), True, (255,255,255))
placeHolder=pygame.image.load("sprites/placeHolder.png")
Jouer=pygame.image.load("sprites/Jouer.png")
Power=pygame.image.load("sprites/Power.png")
Fond=pygame.image.load("sprites/Fondr.png")
Fond2=pygame.image.load("sprites/Fond2r.png")
piqueImg=pygame.image.load("sprites/pique.png")
StartButton=Button(taille[0]/2.5,taille[1]/2.22,Jouer,taille[0]/5,taille[1]/10)
ExitButton=Button(taille[0]/1.15,taille[1]/50,Power,taille[0]/10,taille[1]/10)
img=pygame.image.load("sprites/oiseau.png")
oiseauImg = pygame.transform.scale(img, (100, 100))
clock=pygame.time.Clock()
rect = screen.get_rect()
icon = pygame.image.load("sprites/oiseau.png")
hauteur = 0
scoreTexte= pixelfont.render(str(hauteur),True,(255,255,255))