#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 10:33:08 2025

@author: loulou
"""

from random import *
import time
from compte import compte_points

def construit(rinit, sinit):
    rfin=[]
    sfin=[]
    
    #choisit aléatoirement les 8 cartes régions à jouer
    for n in range(8):
        #print(rinit, rfin)
        rfin.append(choices(rinit)[0])
        rinit.remove(rfin[-1])
    
    compteur=0
    
    #compte le nombre de sanctuaires piochés
    for k in range(7):
        if rfin[k+1]>rfin[k]:
            compteur+=1
    
    #choisit les sanctuaires aléatoirement
    for n in range(compteur):
        sfin.append(choices(sinit)[0])
        sinit.remove(sfin[-1])
    return rfin+sfin
    

#separe les cartes regions et les cartes sanctuaire en 2 listes
def separe(l):
    condition=True
    debut=[]
    fin=[]
    compteur=0
    while condition and compteur<len(l):
        if l[compteur]<100 :
            debut.append(l[compteur])
            compteur+=1
        else :
            fin+=l[compteur:]
            condition=False
    return (debut,fin)
        

def cherche_meilleur(instance : list):
    meilleur_combinaison=[]
    meilleur_score=0
    
    t=separe(instance)
    region=t[0]
    sanct=t[1]
    
    n=time.time()
    while time.time()-n<55 :
        combinaison=construit(region.copy(),sanct.copy())
        score=compte_points(combinaison)
        if score>meilleur_score:
            meilleur_combinaison=combinaison.copy()
            meilleur_score=score
    return (meilleur_combinaison, meilleur_score)

def les_meilleures(instance:list):
    meilleur_combinaison=[]
    meilleur_score=0
    res=[]
    t=separe(instance)
    region=t[0]
    sanct=t[1]
    
    n=time.time()
    while time.time()-n<10 :
        combinaison=construit(region.copy(),sanct.copy())
        score=compte_points(combinaison)
        if score>meilleur_score:
            meilleur_combinaison=combinaison.copy()
            meilleur_score=score
            res.append((meilleur_score,meilleur_combinaison))
    return res
