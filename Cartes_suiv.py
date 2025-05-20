#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 14 09:51:55 2025

@author: cragey
"""

#réduire l'instance après les_meilleures()
#proba carte suivante
from Aleatoire import *
from random import choice, sample,randrange
from lecture_instance import ouvre
import time
from compte import compte_points

def cartes_suiv(inst:list, suiv, mieux):
    """mettre l'instance (réduite ou non), une matrice avec les probas que deux cartes se suivent et mieux=les_meilleures"""
    somme_l=[0 for i in range (len(inst))]
    for j in range(len(mieux)):
        for i in range (len(mieux[j][1])-1):
            x,y = inst.index(mieux[j][1][i]), inst.index(mieux[j][1][i+1])
            somme_l[x]+=mieux[j][0]//8
            suiv[x][y]+=mieux[j][0]//8
    return somme_l
            
def harmonie(suiv):
    """comble le vide pour pouvoir faire des probas ~"""
    s=suiv.copy()
    for j in range(len(s)):
        somme=0
        zero=[]
        for i in range (len(s[j])):
            if s[j][i]!=0:
                somme+=s[j][i]
            else:
                zero.append(i)
        for i in zero:
            s[j][i]=1
    return s
            
####a verif: harmonie ,cartes_suiv, rand_inst_w_suiv
def rand_inst_w_suiv(inst:list, s):
    """s:harmonie(suiv)"""

    pr=randrange(len(inst))#se servir de somme_l pour meilleur score?
    deb=[]
    fin=[]
    if inst[pr]>100:
        nb_s=1
        nb_r=0
        fin.append(inst[pr])
    else:
        nb_s=0
        nb_r=1
        deb.append(inst[pr])
    while nb_r <8 or nb_s<7:
        suit=sample(inst,counts=s[pr],k=1)
        if (suit[0]<100) :
            if (suit[0] not in deb) and (nb_r <8):
                deb.append(suit[0])
                pr=inst.index(suit[0])
                nb_r+=1
        elif (suit[0] not in fin) and (nb_s<7):
            fin.append(suit[0])
            pr=inst.index(suit[0])
            nb_s+=1
    return deb+fin
#prendre en compte nb boucles aléa 
"""
def recolle(inst:list):
    fin=[]
    deb=[]
    cpt_s=0
    for i in range(len(inst)):
        if inst[i]>100:
            fin.append(inst[i])
            
        else:
            deb.append(inst[i])
            if len(deb)>1 and deb[-1]>deb[-2]:
                cpt_s+=1
    return deb+fin
"""     
def supp_sanct(une_inst)    :
    cpt_s=0
    for i in range(0,7):
        if une_inst[i]<une_inst[i+1]:
            cpt_s+=1
    for i in range(7-cpt_s):
        une_inst.pop(-1)
def run(inst:list):
    mieux=les_meilleures(inst)
    #liste=separe(inst)
    l=len(inst)#liste[0]
    suiv=[[0 for _ in range (l)] for i in range (l)]
    t=time.time()
    la_meilleure=mieux[-1]
    while time.time()-t<20:
        """cond sur le temps, le nb d'iter?"""
        somme_l=cartes_suiv(inst, suiv, mieux)#a ajouter en param pour rand_inst_w_suiv pour choisir une premiere carte ?
        s=harmonie(suiv)
        #prendre un élément aléatoirement, puis construire une suite de cartes grace a suiv
        #ATTENTION SANCT
        """sample([‘red’, ‘blue’], counts=[4, 2], k=5) est équivalent à sample([‘red’, ‘red’, ‘red’, ‘red’, ‘blue’, ‘blue’], k=5)"""
        #ech=[rand_inst_w_suiv(inst,s) for i in range (3)]#parce que pk pas 3
        i=0
        ech=[]
        t2=time.time()
        while time.time()-t2<10:
            temp=rand_inst_w_suiv(inst,s)
            
            #temp=recolle(temp)
            supp_sanct(temp)
            cpts=compte_points(temp)
            if len(ech)==0 or cpts >= ech[-1][0]:
                ech.append((cpts,temp))
                i+=1
        if ech[-1][0]>la_meilleure[0]:
            la_meilleure=ech[-1]
        else: 
            ech.append(la_meilleure)
        """if ech [0][0]== ech[1][0] or ech [0][1]== ech[2][0]:
            return la_meilleure"""
        cartes_suiv(inst, suiv, ech)
        s=harmonie(suiv)
    return la_meilleure
########SUPPRIMER SANCT SUPP
"""
t=time.time()
print(run(ouvre("8_7_a.txt")),"8_7_a.txt")
print(time.time()-t)

t=time.time()
print(run(ouvre("8_7_b.txt")),"8_7_b.txt")
print(time.time()-t)

t=time.time()
print(run(ouvre("8_7_c.txt")),"8_7_c.txt")
print(time.time()-t)

t=time.time()
print(run(ouvre("12_10.txt")),"12_10.txt")
print(time.time()-t)

t=time.time()
print(run(ouvre("14_18.txt")))
print("14_18.txt")
print(time.time()-t)

t=time.time()
print(run(ouvre("15_9.txt")),"15_9.txt")
print(time.time()-t)
"""

t=time.time()
print(run(ouvre("competition_07.txt")),"competition_07.txt")
print(time.time()-t)
