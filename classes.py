
from Variables import *

class oiseau():
    def __init__(self, imagepiaf, x, y):
        self.sprite = imagepiaf
        self.x = x 
        self.y = y
        self.dir = 1
        self.vitesseHorizontale = 5
        self.gravite = 5
        self.prochainMur = mur1


    def posistionX(self):
        if self.dir == -1:
            if self.prochainMur.x < (self.x + self.vitesseHorizontale*self.dir) :
                self.x = self.x + self.vitesseHorizontale*self.dir 
            else:
                 self.x + self.x + (self.vitesseHorizontale) - (self.x - self.prochainMur.x)
                 self.dir = 1
                 self.prochainMur = mur2
        else:
            if self.prochainMur.x > (self.x + self.vitesseHorizontale*self.dir) :
                self.x = self.x + self.vitesseHorizontale*self.dir 
            else:
                 self.x + self.x - (self.vitesseHorizontale) - (self.x - self.prochainMur.x)
                 self.dir = -1
                 self.prochainMur = mur1

        return 

    def draw(self):
        screen.blit(self.sprite,(self.posistionX(),self.y))
        



class mur():
    def __init__(self, x):
        self.x = x































caca="lénazis"

