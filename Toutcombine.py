import time
import random
from cartes import cartes_region, cartes_sanctuaire, score_region, score_sanctuaire
import itertools as it

def run(instance:str) -> None:
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
    inst=ouvre(instance)#convertir le fichier en une liste
    mieux=les_meilleures(inst)
    l=len(inst)
    suiv=[[0 for _ in range (l)] for i in range (l)]
    t=time.time()
    la_meilleure=mieux[-1]
    while time.time()-t<21600:
        s=harmonie(suiv)
        #prendre un élément aléatoirement, puis construire une suite de cartes grace a suiv
        i=0
        ech=[]
        t2=time.time()
        while time.time()-t2<500:
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
    return 

def ouvre(nomf : str) -> list:
    """
    Ouvre un fichier

    Parameters
    ----------
    nomf : str
        nom du fichier de l'instance à traiter

    Returns
    -------
    list
        liste avec les cartes de l'instance

    """
    with open(nomf, "r") as fichier:
        l=fichier.read().split()
        for k in range(len(l)):
            l[k]=int(l[k])
        return l

def sortie(tab : tuple, i=1) -> None:
    """
    Ecrit le résultat dans un fichier
    
    Parameters
    ----------
    tab : tuple
        tuple : (liste des cartes, score)
    i : int, optional
        Numéro du fichier, 1 par défaut

    Returns
    -------
    None
        Un fichier nommé 'resultat_competition_{numéro du fichier}' est créé

    """
    with open(f"resultat_competition_{i}.txt", "w") as fichier:
        for k in range(len(tab[1])):
            fichier.write(str(tab[1][k]))
            fichier.write(" ")
        fichier.write("\n")
        fichier.write(str(tab[0]))
    return

def les_meilleures(instance:list) -> list:
    """
    Génère aléatoirement une liste de main de jeu
    
    Parameters
    ----------
    instance : list
        L'instance à traiter

    Returns
    -------
    resultat : list
        Une première liste de combinaisons de cartes comme point de départ

    """
    meilleur_combinaison=[]
    meilleur_score=0
    resultat=[]
    t=separe(instance) #separe les regions et les sanctuaires en 2 listes
    region=t[0]
    sanct=t[1]
    
    n=time.time()
    while time.time()-n<3 :
        combinaison=construit(region.copy(),sanct.copy())
        score=compte_points(combinaison)
        if score>meilleur_score:
            meilleur_combinaison=combinaison.copy()
            meilleur_score=score
            resultat.append((meilleur_score,meilleur_combinaison))
    return resultat

def separe(instance : list) -> tuple:
    """
    Sépare les cartes régions et les cartes sanctuaires
    Les cartes sont supposées triées dans l'ordre croissant
    
    Parameters
    ----------
    instance : list
        Liste de cartes régions et sanctuaire à couper en deux

    Returns
    -------
    tuple
        Les deux listes : (régions, sanctuaires)

    """
    condition=True
    debut=[]
    fin=[]
    compteur=0
    while condition and compteur<len(instance):
        if instance[compteur]<100 :
            debut.append(instance[compteur])
            compteur+=1
        else :
            fin+=instance[compteur:]
            condition=False
    return (debut,fin)

def construit(rinit:list, sinit:list) -> list:
    """
    Construit en pur aléatoire une liste de cartes à partir d'une instance
    
    Parameters
    ----------
    rinit : list
        Liste des cartes régions à l'initialisation
    sinit : list
        Liste des cartes sanctuaires à l'initialisation

    Returns
    -------
    list
        Une combinaison de cartes

    """
    rfin=[]
    sfin=[]
    compteur=0
    
    #choisit aléatoirement les 8 cartes régions à jouer
    for n in range(8):
        rfin.append(random.choices(rinit)[0])
        rinit.remove(rfin[-1])
        if rfin[n]>rfin[n-1]:
            compteur+=1
    
    #choisit les sanctuaires aléatoirement
    for n in range(compteur):
        sfin.append(random.choices(sinit)[0])
        sinit.remove(sfin[-1])
    return rfin+sfin

def compte_points(main : list) -> int :
    """
    Compte le nombre de points d'une main de jeu

    Parameters
    ----------
    main : list
        Main jouée

    Returns
    -------
    int
        Score de la main

    """
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

def cartes_suiv(inst : list, suiv : list, mieux : list) -> None:
    """
    Met à jour les probabilitées

    Parameters
    ----------
    inst : list
        Instance de cartes
    suiv : list
        Matrice avec les probabilitées que 2 cartes se suivent
    mieux : list
        Liste des meilleures mains trouvées

    Returns
    -------
    None
        Il n'y a rien à renvoyer

    """
    """mettre l'instance (réduite ou non), une matrice avec les probas que deux cartes se suivent et mieux=les_meilleures"""
    somme_l=[0 for i in range (len(inst))]
    for j in range(len(mieux)):
        for i in range (len(mieux[j][1])-1):
            x,y = inst.index(mieux[j][1][i]), inst.index(mieux[j][1][i+1])
            somme_l[x]+=mieux[j][0]//8
            suiv[x][y]+=mieux[j][0]//8
    return 

def harmonie(suiv : list) -> list:
    """
    Comble le vide pour pouvoir faire des probas

    Parameters
    ----------
    suiv : list
        Matrice avec les probabilitées que 2 cartes se suivent

    Returns
    -------
    s : list
        Même matrice réajustée pour n'avoir aucune probabilitée nulle

    """
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

def rand_inst_w_suiv(inst:list, s : list) -> list:
    """
    Génère une main avec les probabilitées de la matrice

    Parameters
    ----------
    inst : list
        Instance de cartes
    s : list
        Matrice avec les probabilitées que 2 cartes se suivent

    Returns
    -------
    list
        Main trouvée

    """
    pr=random.randrange(len(inst))
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
        suit=random.sample(inst,counts=s[pr],k=1)
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

def supp_sanct(instance : list) -> tuple:
    """
    Supprime les sanctuaires en trop en gardant la meilleur combinaison possible

    Parameters
    ----------
    instance : list
        Liste de cartes avec 7 sanctuaires

    Returns
    -------
    tuple
        Score et liste des cartes avec le bon nombre de sanctuaires

    """
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