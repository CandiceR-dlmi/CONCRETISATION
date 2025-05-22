# Méthode utilisée:
* Adapation de l'algorithme d'estimation distribution
  + Créer un échantillon de 8 cartes régions ainsi que une main de sanctuaire aléatoirement en gardant uniquement les meilleures combinaisons (fonction ***les_meilleures***)
  + mettre dans une matrice M carrée de taille len(inst) **2 les points rapportés en moyenne par une carte appartenant a cette instance en position j pour la premiere carte et i la carte suivant celle ci dans l'instance (fonction ***cartes_suiv***)
  + harmoniser le tout pour que chaque carte puisse être choisie et pouvoir utiliser random.sample(qui n'accepte pas des floattant ou 0 comme valeur (fonction ***harmonie()***)
  + créer une nouvelle instance grâce à la matrice précédante 
  + faire tourner plusieurs fois les trois dernières étapes 
