import pygame
from Buttons import Button

global hauteur 
hauteur = 0
global plafond
plafond = 150
screen = pygame.display.set_mode((500, 500))
placeHolder=pygame.image.load("sprites/placeHolder.png")
Jouer=pygame.image.load("sprites/Jouer.png")
Power=pygame.image.load("sprites/Power.png")
Fond=pygame.image.load("sprites/Fond.png")
Fond2=pygame.image.load("sprites/Fond2.png")
piqueImg=pygame.image.load("sprites/pique.png")
StartButton=Button(200,225,Jouer,100,50)
ExitButton=Button (425,10,Power,50,50)
oiseauImg=pygame.image.load("sprites/oiseau.png")
clock=pygame.time.Clock()
rect = screen.get_rect()
