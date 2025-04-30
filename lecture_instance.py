#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 14:09:06 2025

@author: loulou
"""

def ouvre(nomf : str):
    with open(nomf, "r") as fichier:
        l=fichier.read().split()
        for k in range(len(l)):
            l[k]=int(l[k])
        return l

def sortie(tab, score, i=0):
    with open(f"sortie{i}.txt", "w") as fichier:
        for k in range(len(tab)):
            fichier.write(str(tab[k]))
            fichier.write(" ")
        fichier.write("\n")
        fichier.write(str(score))