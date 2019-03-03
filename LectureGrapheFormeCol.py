import sys, random, os

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

f.close()

# Mon code :
matrix = A
print(matrix)

# array of attributed colors in order of vertex
colors = [0]*n

# we attribute the fiest color to the virst vertex
colors[0] = 1

# returns the colors of neighbor vertices
def get_neighbor_colors(index):
    neighbor_colors = []
    i = 0
    for adjacency in matrix[index]:
        print("checking adjacency")
        if adjacency is 1:
            print("Found adjacency")
            neighbor_colors.append(colors[i])
            i = i + 1
    return neighbor_colors


def color_graph():
    # while number of colors attributed < number of vertices
    vertex_index = 1
    while vertex_index < n:
        neighbor_colors = get_neighbor_colors(vertex_index)
        color_attributed = False
        color_index = 1
        while color_attributed is False:
            if color_index not in neighbor_colors:
                colors[vertex_index] = color_index
                color_attributed = True
            else:
                color_index = color_index + 1

        vertex_index = vertex_index + 1
    return colors


def create_solution_file(solution):
    solution_filename = sys.argv[1].split("/")[1].split(".")[0] + "_certificat.txt"
    solution_file_path = os.path.join("solutions/", solution_filename)
    solution_file = open(solution_file_path, "w")
    for color in solution:
        solution_file.write(str(color) + " ")

    solution_file.close()


# flux principal
color_graph()
create_solution_file(colors)

