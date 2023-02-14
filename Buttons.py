import pygame
from Variables import *

screen = pygame.display.set_mode((500, 500))

class Button():
    def __init__(self,x,y,image,w,h):
        self.image=image
        self.image=pygame.transform.scale(self.image,(w,h))
        self.rect=self.image.get_rect()
        self.rect.topleft= (x,y)
        self.clicked = False

    def drawClick(self): # Draw button on screen and check if pressed
        action = False
        pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.clicked = True
            if pygame.mouse.get_pressed()[0]==0 and self.clicked==True:
                action = True
        if pygame.mouse.get_pressed()[0]== 0:
            self.clicked = False
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action
