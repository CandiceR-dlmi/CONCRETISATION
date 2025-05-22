#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 22 13:19:21 2025

@author: loulou
"""
from lecture_fichier import lecture, sortie
from construction_initiale import les_meilleures
import time
from cartes_suivante import rand_inst_w_suiv, cartes_suiv
from harmonisation import harmonie, supp_sanct

def run(instance:str) -> None:
    temps=time.time()
    """
    Cherche la meilleure main théoriquement jouable à partir d'une instance de cartes
    
    Parameters
    ----------
    instance : str
        nom du fichier de l'instance à traiter

    Returns
    -------
    None
        Un fichier nommé 'resultat_competition_{numéro du fichier}' est créé

    """
    inst=lecture(instance)#convertir le fichier en une liste
    mieux=les_meilleures(inst)
    l=len(inst)
    suiv=[[0 for _ in range (l)] for i in range (l)]
    t=time.time()
    la_meilleure=mieux[-1]
    while time.time()-t<42:
        s=harmonie(suiv)
        #prendre un élément aléatoirement, puis construire une suite de cartes grace a suiv
        i=0
        ech=[]
        t2=time.time()
        while time.time()-t2<9:
            temp=rand_inst_w_suiv(inst,s)
            temp_t=supp_sanct(temp)
            if len(ech)==0 or temp_t[0] >= ech[-1][0]:
                ech.append(temp_t)
                i+=1
        if ech[-1][0]>la_meilleure[0]:
            la_meilleure=ech[-1]
        else: 
            ech.append(la_meilleure)
        cartes_suiv(inst, suiv, ech)
    sortie(la_meilleure, int(instance[-6:-4]))
    print(temps-time.time())
    return 