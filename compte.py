#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 15:49:10 2025

@author: lhrouch
"""

def compte_points(main : list) -> int :
    ressources = {"R" : 0, "V" : 0, "B" : 0, "J" : 0, "E" : 0, "N" : 0, "I" : 0, "P" : 0, "CHI" : 0, "CHA" : 0}
    #recupere ressources des sanctuaires
    for i in range(8, len(main)):
        carte = cartes_sanctuaires[main[i]-101]
        for ele in carte[:3]:
            if ele != None:
                ressources[ele] += 1
        for j in range(3):
            if j == 0:
                ressources["P"] += carte[3][j]
            elif j == 1:
                ressources["CHI"] += carte[3][j]
            elif j == 2:
                ressources["CHA"] += carte[3][j]
    points = 0
    #compte des points au reveal des cartes
    for k in range(7, -1, -1):
        carte = score_region[main[k]-1]
        if c