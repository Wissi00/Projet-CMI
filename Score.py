import random

def generationPiquesPosition(hauteur):
    liste=[0]*10
    if hauteur<10000:
        n=random.randint(2,3)
        cpt=0
        while cpt<n:
            a=random.randint(0,9)
            if liste[a]==0:
                liste[a]=1
                cpt+=1
    elif hauteur<23000:
        n=random.randint(3,4)
        cpt=0
        while cpt<n:
            a=random.randint(0,9)
            if liste[a]==0:
                liste[a]=1
                cpt+=1
    elif hauteur<50000:
        n=random.randint(4,5)
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
    
generationPiquesPosition(349)