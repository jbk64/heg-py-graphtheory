# heg-py-graphtheory

Algorithme de coloration de graphe.

## Algorithm

### Précondition
Nous avons une matrice d'adjacence en mémoire, créée d'après un fichier .col décrivant le graphe.

### Postcondition
Nous avons un fichier solutions/*graphe*_sol.txt qui décrit la solution générée.

### Algorithme:

Tant que tous les sommets ne sont pas colorés:
1) Choisir le prochain noeud dans la première dimension de la matrice d'adjacence.
2) Attribuer la plus petite couleur valide non attribuée.

## Exemples de résultats
* Graphe C5 : 3 couleurs
* Graphe C10 : 10 couleurs
* Graphe 