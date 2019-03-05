import sys, os

impression=0

if len(sys.argv)<2:
    print("Veuillez fournir un fichier graphe en argument")
    exit(0)

# lecture fichier
fichierGraphe = sys.argv[1]
f = open(fichierGraphe, 'r')

for ligne in f:
    ligneSep=ligne.split()
    if ligneSep[0]=="p":
        n=int(ligneSep[2])
        m=int(ligneSep[3])
        A=[[0 for x in range(n)] for y in range(n)]
    if ligneSep[0]=="e":
        A[int(ligneSep[1])-1][int(ligneSep[2])-1]=1
        A[int(ligneSep[2])-1][int(ligneSep[1])-1]=1

print("Nombre de sommets: ",n)
print("Nomber d'arêtes: ",m)
# print("Matrice d'adjacence:")
# print(A)
f.close()

######################################################
# @author Jack Barker
######################################################

# Retourne les couleurs des sommets du voisinage d'un sommet
# Le paramètre index est l'index dans la matrice du sommet dont on veut les couleurs voisines
def get_neighbor_colors(index):
    neighbor_colors = []
    i = 0
    for adjacency in matrix[index]:
        if adjacency is 1:
            neighbor_colors.append(colors[i])
        i = i + 1
    return neighbor_colors

# Fonction principale de l'algorithme
def color_graph():
    vertex_index = 1
    while vertex_index < n:
        neighbor_colors = get_neighbor_colors(vertex_index)
        color_attributed = False
        color_index = 1
        while color_attributed is False:
            if color_index in neighbor_colors:
                color_index = color_index + 1
            else:
                colors[vertex_index] = color_index
                color_attributed = True

        vertex_index = vertex_index + 1

# Créé le fichier certificat
def create_solution_file(solution):
    solution_filename = sys.argv[1].split("/")[1].split(".")[0] + "_certificat.txt"
    solution_file_path = os.path.join("solutions/", solution_filename)
    solution_file = open(solution_file_path, "w")
    for color in solution:
        solution_file.write(str(color) + " ")

    solution_file.close()

# La matrice d'adjacence
matrix = A

# On donne la couleur 0 à tous les sommets
colors = [0]*n

# On donne la couleur 1 au premier sommet
colors[0] = 1

# Appel des fonctions
color_graph()
create_solution_file(colors)

