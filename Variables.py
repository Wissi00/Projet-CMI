import pygame
from Buttons import Button

screen = pygame.display.set_mode((500, 500))
placeHolder=pygame.image.load("sprites/placeHolder.png")
StartButton=Button(200,225,placeHolder,100,50)
ExitButton=Button (425,10,placeHolder,50,50)
oiseauImg=pygame.image.load("sprites/oiseau.png")