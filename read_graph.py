import sys

if len(sys.argv) < 2:
    print("Please provide a file as argument")
    exit(0)

file = sys.argv[1]
f = open(file, 'r')

matrix = [[]]
m = None
n = None

for line in f:
    tokens = line.split()
    if tokens[0] == "p":
        n = int(tokens[2])
        m = int(tokens[3])
        matrix = [[0 for x in range(n)] for y in range(n)]
    if tokens[0] == "e":
        matrix[int(tokens[1])-1][int(tokens[2])-1] = 1
        matrix[int(tokens[2])-1][int(tokens[1])-1] = 1

print("Number of vertexes: {}".format(n))
print("Number of edges: {}".format(m))
print("Adjacency matrix:")
print(matrix)
