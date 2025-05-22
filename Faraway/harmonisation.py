import itertools as it
from compte import compte_points

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