# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

#R V B J E N I P CHI CHA [P, CHI, CHA]

score_region = [(0, [0,0,0], []), 
                (0, [0,0,0], []), 
                (4, [0,0,0], []), 
                (0, [0,0,0], []),
                (2, [0,0,0], []),
                (0, [0,0,0], []),
                (0, [0,0,0], []),
                (0, [0,0,0], []),
                (5, [0,0,0], []),
                (3, [0,0,0], ["N"]),
                (2, [0,0,0], ["I"]),
                (0, [0,0,0], []),
                (2, [0,0,0], ["P"]),
                (2, [0,0,0], ["N"]),
                (2, [0,0,0], ["CHI"]),
                (2, [0,0,0], ["CHI"]),
                (3, [0,2,0], ["P"]),
                (10, [0,0,0], ["E"]),
                (2, [0,0,0], ["CHA"]),
                (2, [1,0,0], ["N"]),
                (8, [2,0,0], []),
                (1, [0,0,0], ["I"]),
                (10, [0,0,0], ["E"]),
                (2, [0,1,0], ["N"]),
                (1, [0,0,0], ["J", "V"]),
                (3, [0,0,0], ["CHA"]),
                (1, [0,0,0], ["J", "B"]),
                (3, [0,0,0], ["CHI"]),
                (2, [0,0,0], ["CHA"]),
                (2, [0,0,0], ["P"]),
                (1, [0,0,0], ["J", "R"]),
                (7, [3,0,0], []),
                (3, [0,0,0], ["CHA"]),
                (3, [2,0,0], ["CHI"]),
                (10, [0,0,0], ["E"]),
                (4, [0,2,0], ["CHA"]),
                (3, [0,0,1], ["N"]),
                (3, [0,1,1], ["I"]),
                (9, [0,2,0], []),
                (3, [1,1,1], ["N"]),
                (4, [2,1,0], ["N"]),
                (2, [1,1,0], ["J","V"]),
                (10, [0,0,0], ["E"]),
                (2, [1,0,1], ["J", "B"]),
                (13, [0,3,0], []),
                (10, [2,1,0], []),
                (2, [0,1,1], ["J", "R"]),
                (3, [0,0,0], ["P"]),
                (12, [2,0,1], []),
                (4, [0,0,2], ["V"]),
                (14, [4,0,0], []),
                (4, [3,0,0], ["CHI"]),
                (4, [0,0,2], ["R"]),
                (4, [0,0,2], ["I"]),
                (3, [0,1,2], ["P"]),
                (4, [1,2,0], ["B"]),
                (4, [0,0,3], ["P"]),
                (3, [0,3,0], ["I"]),
                (3, [1,3,0], ["J","R"]),
                (16, [2,2,0], []),
                (17, [0,4,0], []),
                (3, [0,0,3], ["J","B"]),
                (15, [0,2,1], []),
                (18, [2,0,2], []),
                (3, [0,0,3], ["J","V"]),
                (20, [4,0,0], []),
                (19, [0,2,2], []),
                (24, [5,0,0], [])
                ]

score_sanctuaire = [(1, ["P"]),
                    (2, ["P"]),
                    (1, ["CHI"]),
                    (2, ["CHI"]),
                    (1, ["CHA"]),
                    (2, ["CHA"]),
                    (0, []),
                    (0, []),
                    (0, []),
                    (1, ["I"]),
                    (1, ["I"]),
                    (1, ["I"]),
                    (2, ["I"]),
                    (1, ["R","B"]),
                    (1, ["V","R"]),
                    (1, ["R","J"]),
                    (1, ["V","B"]),
                    (1, ["B","J"]),
                    (1, ["J","V"]),
                    (4, ["E"]),
                    (5, []),
                    (1, ["N"]),
                    (0, []),
                    (0, []),
                    (0, []),
                    (0, []),
                    (0, []),
                    (0, []),
                    (0, []),
                    (1, ["R"]),
                    (0, []),
                    (0, []),
                    (0, []),
                    (0, []),
                    (1, ["B"]),
                    (0, []),
                    (0, []),
                    (0, []),
                    (1, ["N"]),
                    (1, ["V"]),
                    (0, []),
                    (0, []),
                    (4, ["E"]),
                    (1, ["I"]),
                    (1, ["J"]),
                    ]

#--------------------------------------------------------------------------------------------------------------------------
cartes_region = [['R', None, None, [1, 1, 0]],
['B', None, None, [2, 0, 0]],
['V', None, None, [0, 0, 0]],
['R', None, None, [1, 0, 1]],
['V', None, None, [0, 1, 0]],
['B', None, 'I', [1, 0, 0]],
['R', None, None, [0, 1, 1]],
['V', None, 'I', [0, 1, 0]],
['B', None, None, [0, 0, 0]],
['R', None, None, [0, 0, 0]],
['V', None, None, [0, 0, 0]],
['J', None, 'I', [0, 0, 1]],
['B', None, None, [0, 0, 0]],
['R', None, None, [0, 0, 1]],
['V', None, 'I', [0, 0, 0]],
['R', None, None, [0, 1, 0]],
['B', None, None, [1, 0, 0]],
['V', None, None, [0, 1, 0]],
['R', None, None, [0, 0, 1]],
['V', 'N', 'I', [0, 0, 0]],
['B', 'N', None, [0, 0, 0]],
['V', 'N', 'I', [0, 0, 0]],
['R', 'N', None, [1, 1, 0]],
['B', 'N', None, [1, 0, 0]],
['J', 'N', None, [0, 0, 0]],
['R', 'N', None, [0, 1, 0]],
['J', 'N', None, [0, 0, 0]],
['R', 'N', None, [1, 0, 0]],
['J', 'N', None, [0, 0, 1]],
['R', 'N', None, [1, 0, 0]],
['J', 'N', None, [0, 0, 0]],
['R', 'N', None, [1, 1, 0]],
['J', 'N', 'I', [0, 0, 0]],
['V', 'N', None, [0, 1, 0]],
['J', 'N', None, [0, 1, 0]],
['R', 'N', None, [0, 0, 0]],
['J', 'N', None, [0, 0, 0]],
['V', 'N', None, [1, 0, 0]],
['R', 'N', None, [1, 0, 1]],
['B', 'N', None, [0, 0, 0]],
['V', None, None, [0, 0, 1]],
['J', None, None, [0, 0, 0]],
['B', None, None, [1, 0, 0]],
['J', None, None, [0, 0, 0]],
['V', None, None, [1, 0, 0]],
['B', None, 'I', [0, 0, 0]],
['J', None, None, [0, 0, 0]],
['R', None, None, [0, 1, 0]],
['B', None, 'I', [0, 0, 0]],
['J', None, None, [1, 0, 0]],
['B', None, None, [1, 0, 0]],
['R', None, None, [0, 0, 0]],
['J', None, None, [0, 1, 0]],
['V', None, None, [0, 1, 0]],
['B', None, 'I', [1, 0, 0]],
['J', None, None, [0, 0, 1]],
['R', None, None, [0, 0, 0]],
['V', None, 'I', [0, 0, 0]],
['J', None, 'I', [0, 0, 0]],
['B', None, 'I', [0, 0, 0]],
['V', None, None, [0, 0, 1]],
['J', None, 'I', [0, 0, 0]],
['V', None, 'I', [0, 0, 0]],
['B', None, 'I', [0, 0, 0]],
['J', None, 'I', [0, 0, 0]],
['B', None, None, [0, 0, 0]],
['V', None, 'I', [0, 0, 0]],
['B', None, None, [0, 0, 0]]
]
    

cartes_sanctuaire = [
[None, None, None, [1, 0, 0]],
[None, None, None, [0, 0, 0]],
[None, None, None, [0, 1, 0]],
[None, None, None, [0, 0, 0]],
[None, None, None, [0, 0, 1]],
[None, None, None, [0, 0, 0]],
[None, None, 'I', [1, 0, 0]],
[None, None, 'I', [0, 1, 0]],
[None, None, 'I', [0, 0, 1]],
[None, None, None, [1, 0, 0]],
[None, None, None, [0, 1, 0]],
[None, None, 'I', [0, 0, 0]],
[None, None, None, [0, 0, 0]],
[None, None, None, [0, 0, 0]],
[None, None, None, [0, 0, 0]],
[None, None, None, [0, 0, 0]],
[None, None, None, [0, 0, 0]],
[None, None, None, [0, 0, 0]],
[None, None, None, [0, 0, 0]],
[None, None, 'I', [0, 0, 0]],
[None, None, None, [0, 0, 0]],
[None, None, None, [1, 0, 0]],
[None, 'N', None, [1, 0, 0]],
[None, 'N', None, [0, 1, 0]],
[None, 'N', None, [0, 0, 1]],
['R', None, None, [1, 0, 0]],
['R', None, None, [0, 1, 0]],
['R', None, None, [0, 0, 1]],
['R', 'N', None, [0, 0, 0]],
['R', None, None, [0, 0, 0]],
['B', None, None, [1, 0, 0]],
['B', None, None, [0, 1, 0]],
['B', None, None, [0, 0, 1]],
['B', None, 'I', [0, 0, 0]],
['B', None, None, [0, 0, 0]],
['V', None, None, [1, 0, 0]],
['V', None, None, [0, 1, 0]],
['V', None, 'I', [0, 0, 0]],
['V', None, None, [0, 0, 0]],
['V', None, None, [0, 0, 0]],
['J', None, None, [1, 0, 0]],
['J', None, 'I', [0, 0, 0]],
['J', None, None, [0, 0, 0]],
['J', None, None, [0, 0, 0]],
['J', None, None, [0, 0, 0]]
]
#----------------------------------------------------------------------------------------------------------------------------
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
            