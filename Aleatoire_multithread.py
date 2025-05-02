#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 10:33:08 2025

@author: loulou
"""

from random import *
import time
from compte import compte_points
import threading 
from lecture_instance import *

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
    print (meilleur_combinaison, meilleur_score)

def bourriner(f):
    l=ouvre(f)
    t1=threading.Thread(target=cherche_meilleur, args=(l,))
    t2=threading.Thread(target=cherche_meilleur, args=(l,))
    t3=threading.Thread(target=cherche_meilleur, args=(l,))
    t4=threading.Thread(target=cherche_meilleur, args=(l,))
    t5=threading.Thread(target=cherche_meilleur, args=(l,))
    t6=threading.Thread(target=cherche_meilleur, args=(l,))
    t7=threading.Thread(target=cherche_meilleur, args=(l,))
    t8=threading.Thread(target=cherche_meilleur, args=(l,))
    t9=threading.Thread(target=cherche_meilleur, args=(l,))
    t10=threading.Thread(target=cherche_meilleur, args=(l,))
    t11=threading.Thread(target=cherche_meilleur, args=(l,))
    t12=threading.Thread(target=cherche_meilleur, args=(l,))
    t13=threading.Thread(target=cherche_meilleur, args=(l,))
    t14=threading.Thread(target=cherche_meilleur, args=(l,))
    t15=threading.Thread(target=cherche_meilleur, args=(l,))
    t16=threading.Thread(target=cherche_meilleur, args=(l,))
    t17=threading.Thread(target=cherche_meilleur, args=(l,))
    t18=threading.Thread(target=cherche_meilleur, args=(l,))
    t19=threading.Thread(target=cherche_meilleur, args=(l,))
    t20=threading.Thread(target=cherche_meilleur, args=(l,))
    t21=threading.Thread(target=cherche_meilleur, args=(l,))
    t22=threading.Thread(target=cherche_meilleur, args=(l,))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    t13.start()
    t14.start()
    t15.start()
    t16.start()
    t17.start()
    t18.start()
    t19.start()
    t20.start()
    t21.start()
    t22.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()
    t12.join()
    t13.join()
    t14.join()
    t15.join()
    t16.join()
    t17.join()
    t18.join()
    t19.join()
    t20.join()
    t21.join()
    t22.join()