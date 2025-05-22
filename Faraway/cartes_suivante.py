import random

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