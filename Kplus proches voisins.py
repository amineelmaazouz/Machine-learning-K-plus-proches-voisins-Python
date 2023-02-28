# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 15:37:18 2023

@author: amine el maazouz
"""
from math import sqrt
from random import *
import matplotlib.pyplot as plt
from collections import Counter
## Données d'apprentissage
plt.figure(1)
N=200 #nombre de points
#liste des points rouges
rouges=[[[gauss(1,1),gauss(-1,1)],"r"] for i in range(N//2)]
#liste des points bleus
bleus=[[[gauss(-1,1),gauss(1,1)],"b"] for i in range(N//2+1)]
#tracé de points rouges
for i in range(N//2):
    plt.plot(rouges[i][0][0],rouges[i][0][1],"or")
#tracé de points bleus
for i in range(N//2+1):
    plt.plot(bleus[i][0][0],bleus[i][0][1],"ob")
    
    
donnees=rouges+bleus
for i in range(N):
    plt.plot(donnees[i][0][0],donnees[i][0][1],"o"+donnees[i][1])
plt.show()

def distancem (p1,p2):
    d=0
    m=len(p1)
    for i in range (m):
        d = d + (p2[i]-p1[i])**2
    return sqrt(d)


def kPlusProchesVoisins (L,p,k):#utilisation de la bibliothèque collections a
#pour intérer de dénombrer le nombre de couleurs qu'on a en inventaire 
    
    
    D=[] #contiendra la distance séparant notre point P des autres points de L 
    for i in range(len(L)):
        d=distancem(L[i][0],p)
        D.append([d,L[i][1]])
    D.sort()
    couleurs=[]
    for i in range(k):
        couleurs.append(D[i][1])
    S=''.join(couleurs)
    DICT=Counter(S)
    return DICT.most_common(1)[0][0]








        
        
    
    
        
    









