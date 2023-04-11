from Variables import *



def generationPics(_tableauPicsPos, _cote):
    _tabPicsARenvoyer = []
    for _pos in range(len(_tableauPicsPos)):
        if _tableauPicsPos[_pos] == 1:
            _tabPicsARenvoyer.append(spike(50*_pos, _cote))
    return _tabPicsARenvoyer



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
        self.rect=pygame.Rect(0,0,60,60)
        self.x = x 
        self.rect.x=self.x+20
        self.y = y
        self.rect.y=self.y+20
        self.dir = 1
        self.vitesseHorizontale = 6
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
            self.sprite=pygame.transform.flip(self.sprite,True,False)
        if pygame.Rect.colliderect(self.rect, self.mur2.rect):
            self.dir=-1
            self.sprite=pygame.transform.flip(self.sprite,True,False)
        self.rect.x=self.x+20


    def draw(self):
        screen.blit(self.sprite,(self.x,self.y))
       # pygame.draw.rect(screen, (255, 0, 0), self.rect, 2) #Ne pas supprimer j'en ai besoin ~Wissam

    def mouvY(self, jump, hauteur):
        if jump == False:
            self.vitesseVerticale= approach(self.vitesseVerticale,7,0.5)
        else:
            self.vitesseVerticale= -8
        self.y += self.vitesseVerticale
        if 0 < max(0,(plafond-(self.y + self.vitesseVerticale))):
            hauteur += max(0,(plafond-(self.y + self.vitesseVerticale)))
        self.y = max(plafond, self.y)
        
        self.rect.y=self.y+20
        self.rect.x=self.x
        
        return hauteur

class spike():
    def __init__(self, y, s):
        self.y = y
        self.h = 50
        self.w = 50
        if s == "Right":
            self.sprite=piqueImg
            self.sprite=pygame.transform.scale(self.sprite,(self.w,self.h))
            self.sprite=pygame.transform.flip(self.sprite,True,False)
            self.x=500-self.w
            self.A=(self.x+self.w, self.y)
            self.B=(self.x,self.y+(self.h)/2)
            self.C=(self.x+self.w, self.y+self.h)
        if s == "Left":
            self.sprite=piqueImg
            self.sprite=pygame.transform.scale(self.sprite,(self.w,self.h))
            self.x=0
            self.A=(self.x, self.y)
            self.B=(self.x+self.w,self.y+(self.h)/2)
            self.C=(self.x, self.y+self.h)
        self.rect=self.sprite.get_rect()
        self.rect.y=self.y
        self.rect.x=self.x
        self.vertices = [self.A, self.B, self.C]



    def draw(self):
        screen.blit(self.sprite,(self.rect))
    # pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)
    #    pygame.draw.polygon(screen, (255, 0, 0), self.vertices, 2)

class murEtPics():
    def __init__(self,id, cote):
        self.picsPositions = [1, 0, 0, 1, 0, 0, 0, 1, 0, 0]
        self.id = id
        self.yInit= -500+(id*500)
        self.y = self.yInit
        self.cote = cote
        self.picsGeneres = True
        self.pics = generationPics(self.picsPositions, self.cote)