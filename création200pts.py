# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 18:50:35 2023

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