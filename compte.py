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
        carte = cartes_sanctuaire[main[i]-101]
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
        #print(ressources, main[i])
    points = 0
    #compte des points au reveal des cartes
    for k in range(7, -1, -1):
        carte = cartes_region[main[k]-1]
        #maj ressources
        for ele in carte[:3] :
            if ele != None :
                ressources[ele] += 1
        for j in range(3) :
            if j == 0:
                ressources["P"] += carte[3][j]
            elif j == 1:
                ressources["CHI"] += carte[3][j]
            elif j == 2:
                ressources["CHA"] += carte[3][j]
        carte = score_region[main[k]-1]
        #print(main[k])
        #nb ensemble
        ressources["E"] = min([ressources["R"], ressources["V"], ressources["B"], ressources["J"]])
        #voir condition validee
        s = 0
        valide = True
        while s < 3 and valide :
            if s == 0 :
                valide = ressources["P"] >= carte[1][s]
            elif s == 1 :
                valide = ressources["CHI"] >= carte[1][s]
            elif s == 2 :
                valide = ressources["CHA"] >= carte[1][s] 
            s += 1
            
        #ajout des points 
        if valide and len(carte[2]) == 0 :
            points += carte[0]
        elif valide and len(carte[2]) > 0 :
            for ele in carte[2]:
                points += ressources[ele] * carte[0]
        #print(ressources, points)
    #compte points sanctuaire
    for sanct in main[8:] :
        carte = score_sanctuaire[sanct-101]
        if len(carte[1]) == 0 :
            points += carte[0]
        elif len(carte[1]) > 0 :
            for ele in carte[1]:
                points += ressources[ele] * carte[0]
    return points
