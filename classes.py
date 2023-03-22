from Variables import *

def approach(start, end, shift):
    if start < end:
        return min(start+shift,end)
    else:
        return max(start-shift,end)

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
        self.vitesseHorizontale = 5
        self.vitesseVerticale = 0
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
      #  pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)

    def mouvY(self, jump):
        if jump == False:
            self.vitesseVerticale= approach(self.vitesseVerticale,8,0.5)
        else:
            self.vitesseVerticale= -7
        self.y += self.vitesseVerticale
        global hauteur
        hauteur += max(0,(plafond-(self.y + self.vitesseVerticale)))
        if hauteur > 10:
            hauteur += 1
        self.y = max(plafond, self.y)
        
        self.rect.y=self.y
        self.rect.x=self.x

class spike():
    def __init__(self, imagepique, x, y, h, w):
        self.sprite = imagepique
        self.rect=self.sprite.get_rect()
        self.x = x 
        self.rect.x=self.x
        self.y = y
        self.rect.y=self.y
        self.h = h
        self.w = w
        self.A=(self.x, self.y)
        self.B=(self.x+self.w,self.y+(self.h)/2)
        self.C=(self.x, self.y+self.h)
        self.vertices = [self.A, self.B, self.C]



    def draw(self):
        screen.blit(self.sprite,(self.x,self.y))
        pygame.draw.polygon(screen, (255, 0, 0), self.vertices, 2)

