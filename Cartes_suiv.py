#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 14 09:51:55 2025

@author: cragey
"""

#réduire l'instance après les_meilleures()
#proba carte suivante
from Aleatoire import *
from random import choice, sample


def cartes_suiv(inst:list, suiv, mieux):
    """mettre l'instance (réduite ou non), une matrice(mettre index?) avec les probas que deux cartes se suivent et mieux=les_meilleures"""
    somme_l=[7 * len(inst)]
    for j in range(len(mieux)):
        for i in range (len(liste)-1):
            x,y = inst.index(mieux[j][1][i]), inst.index(mieux[j][1][i+1])
            somme_l[x]+=mieux[j][0]
            suiv[x][y]+=mieux[j][0]
    return somme_l
            
    
def rand_inst_w_suiv(inst:list, suiv):
    pr=choice(inst)
    une_inst=[pr]
    while len( une_inst) <8:
        suiv=sample([])
#prendre en compte nb boucles aléa 
def run(inst:list, suiv:list:
    mieux=les_meilleures(inst)
    liste=separe(inst)
    l=len(liste[0])
    suiv=[[7 for _ in range l] for i in range l]
    while True:
        """cond sur le temps, le nb d'iter?"""
        cartes_suiv(liste[0], suiv, mieux)
        #prendre un élément aléatoirement, puis construire une suite de cartes grace a suiv
        """sample([‘red’, ‘blue’], counts=[4, 2], k=5) est équivalent à sample([‘red’, ‘red’, ‘red’, ‘red’, ‘blue’, ‘blue’], k=5)"""
        