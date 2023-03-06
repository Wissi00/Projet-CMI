from Variables import *

class mur():
    def __init__(self, image,x,w):
        self.image=image
        self.image=pygame.transform.scale(self.image,(w,500))
        self.rect=self.image.get_rect()
        self.x=x
        self.rect.x=self.x
    
    def draw(self):    
        screen.blit(self.image,(self.x,0))
        

class oiseau():
    def __init__(self, imagepiaf, x, y,mur1,mur2):
        self.sprite = imagepiaf
        self.rect=self.sprite.get_rect()
        self.x = x 
        self.rect.x=self.x
        self.y = y
        self.rect.y=self.y
        self.dir = 1
        self.vitesseHorizontale = 1
        self.gravite = 5
        self.mur1 = mur1
        self.mur2 = mur2


    def mouvX(self):
        if self.dir==1:
            self.x+=self.vitesseHorizontale
        if self.dir==-1:
            self.x-=self.vitesseHorizontale
        if pygame.Rect.colliderect(self.rect, self.mur1.rect):
            self.dir=1
        if pygame.Rect.colliderect(self.rect, self.mur2.rect):
            self.dir=-1
        self.rect.x=self.x


    def draw(self):
        screen.blit(self.sprite,(self.x,self.y))

