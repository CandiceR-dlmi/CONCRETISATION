#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 14:09:06 2025

@author: loulou
"""

def ouvre(nomf : str):
    fichier = open(nomf, "r")
    l=fichier.read().split()
    fichier.close()
    for k in range(len(l)):
        l[k]=int(l[k])
    return l
