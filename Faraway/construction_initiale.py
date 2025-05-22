import time
from compte import compte_points
import random

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
    while time.time()-n<10 :
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
