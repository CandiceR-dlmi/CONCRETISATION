def lecture(nomf : str) -> list:
    """
    Lit un fichier

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