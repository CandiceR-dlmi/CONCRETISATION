#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 20 14:24:29 2025

@author: loulou
"""
import itertools as it
from compte import *
from cartes import *

def supp_sanct(instance):
    region=instance[:8]
    sanct=instance[8:]
    compteur = 0
    for k in range(7):
        if instance[k+1]>instance[k]:
            compteur+=1
    combinations=list(it.combinations(sanct, compteur))
    meilleur=[]
    meilleur_score=0
    for k in combinations:
        k=list(k)
        l=compte_points(region+k)
        if l>meilleur_score:
            meilleur_score=l
            meilleur=k
    return (meilleur_score,region+meilleur)
