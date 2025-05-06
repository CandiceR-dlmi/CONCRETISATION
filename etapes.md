# Liste des étapes suivies/à suivre pour ce projet

* FAIT
  + representation des cartes
  + calcul du score pour une liste de cartes
  + création du git
  
* A FAIRE
  + définir la meilleure stratégie à adopter
  + programmer un/plusieurs algo sol


## Idée de stratégie
  * 1ère idée candice 
    + Trier cartes décroissant nb points apportés (enlever celles qui n'apportent aucun point et priorité aux cartes sans cond et/ou avec ressources si égalité dans points)
    + prendre pour les cartes rapportant le plus une carte leur permettant de se rapprocher de l'obj la moins loin dans la liste triée précédente, jusqu'à ce qu'une condition ne soit plus validée ou qu'on aie atteint le bon nb de cartes(8)
    + recommencer en changeant de 1ere carte???
    + jouer avec des permutations pour mettre un max de sanct si besoin, ou rapporter plus de pts si ressources d'une carte non utilisée par les précédentes
  * idée 2
    + faire un algorithme de colonies de fourmis, utiliser matrices + probas
    + la proba originelle d'aller sur une carte en premier est 1/8 etc mais une fois un chemin emprunté, elle est multipliée par (100+ nb de points rapportés par le chemin )/100 par ex (bon pas ouf on changera ça mais c'estpour avoir une idée)
    + il faudrait une borne pour ces probas 
