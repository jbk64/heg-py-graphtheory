
# Algorithme de coloration de graphe

Ce dépôt contient du code Python de [coloration de graphe](https://fr.wikipedia.org/wiki/Coloration_de_graphe) réalisé lors d'un travail pratique de recherche opérationelle (RO).

Les fichiers `.col` dans le répertoire `graphes` contiennent les descriptions de graphes dont il faut trouver le nombre chromatique.

Les fichiers `.txt` dans le répertoire `solutions` contiennent la coloration proposée dans le format “couleur_sommet_1 couleur_sommet_2 (...) couleur_sommet_n”.

Le code réalisé se trouve dans le fichier `LectureGrapheFormeCol.py` à partir de la ligne 33.

## Algorithme utilisé
Soit matrix la matrice d’adjacence stockée en mémoire d’après le fichier .col.

Soit n le nombre de sommets dans le graphe.

 1. On crée un tableau de taille n qui stocke les couleurs attribuées dans l’ordre des sommets dans matrix. Toutes les couleurs sont initialisées à 0 (absence de couleur). 
 1. On attribue la première couleur (1) au premier sommet dans matrix.
1. Tant qu’il reste des sommets non-traités dans matrix: 
	1. On choisit le prochain sommet.
	2.  On récupère les couleurs des sommets du voisinage dans une liste.
	3. On attribue la plus petite couleur non-présente dans la liste de couleurs du voisinage.

## Example d'exécution

### Commande

    python3 VerifCertificatColoration.py graphes/G1.col solutions/G1_certificat.txt

### Résultat

    Coloration proposée: [...]
    Coloration ADMISSIBLE en 8 couleurs.
