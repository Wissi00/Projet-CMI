import random
from Variables import scoreTexte,screen
def maxPiques():
    return 8

def generationPiquesPosition(hauteur):
    liste=[0]*10
    if hauteur<1000:
        n=random.randint(2,3)
        cpt=0
        while cpt<n:
            a=random.randint(0,9)
            if liste[a]==0:
                liste[a]=1
                cpt+=1
    elif hauteur<2300:
        n=random.randint(4,5)
        cpt=0
        while cpt<n:
            a=random.randint(0,9)
            if liste[a]==0:
                liste[a]=1
                cpt+=1
    elif hauteur<5000:
        n=random.randint(6,7)
        cpt=0
        while cpt<n:
            a=random.randint(0,9)
            if liste[a]==0:
                liste[a]=1
                cpt+=1
    else:
        n=random.randint(3,6)
        cpt=0
        while cpt<n:
            a=random.randint(0,9)
            if liste[a]==0:
                liste[a]=1
                cpt+=1
    return liste
        
def afficherScore():
    screen.blit(scoreTexte,(242,10))
    
generationPiquesPosition(349)