# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire. 
"""
from cartes import *

#fonction qui renvoie une liste des cartes qui apporteront 0 points

def aucun_points(main : list) -> list :
    inutile = []
    ressources = {"R" : 0, "V" : 0, "B" : 0, "J" : 0, "E" : 0, "N" : 0, "I" : 0, "P" : 0, "CHI" : 0, "CHA" : 0}
    #recup ressources
    for i in range(len(main)):
        if i > 7 :
            carte = cartes_sanctuaire[main[i]-101]
        else :
            carte = cartes_region[main[i]-1]
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
    #nb ensemble
    ressources["E"] = min([ressources["R"], ressources["V"], ressources["B"], ressources["J"]])
    #voit par carte si possible
    for ele in main :
        valide = True
        if ele < 100 :
            carte = score_region[ele-1]
            #voir condition validee
            s = 0
            while s < 3 and valide :
                if s == 0 :
                    valide = ressources["P"] >= carte[1][s]
                elif s == 1 :
                    valide = ressources["CHI"] >= carte[1][s]
                elif s == 2 :
                    valide = ressources["CHA"] >= carte[1][s] 
                s += 1
        else :
            carte = score_sanctuaire[ele-101]
        if valide :
            if len(carte[-1]) == 1:
                valide = ressources[carte[-1][0]] != 0
            elif len(carte[-1]) == 2:
                valide = ressources[carte[-1][0]] != 0 or ressources[carte[-1][1]] != 0
        if not valide :
            inutile.append(ele)
    return inutile
            
