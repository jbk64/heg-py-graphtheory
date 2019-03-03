import sys

impression=0

if len(sys.argv)<3:
    print("Veuillez fournir un fichier graphe et un fichier contenant la coloration en argument")
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

print("Nombre de sommets:",n)
print("Nomber d'arêtes:",m)
print("Matrice d'adjacence:")
for i in range(n):
    print(A[i])

fichierColoration=sys.argv[2]
f_certif=open(fichierColoration,'r')
coloration=f_certif.readline().split()
for i in range(n):
    coloration[i]=int(coloration[i])
print("Coloration proposée: ",coloration)
couleursUtilisees=[0 for x in range(n)]

for i in range(n):
    if coloration[i]<1 or coloration[i]>n and not isinstance(coloration[i], int):
        print("Attention: la coloration doit utiliser uniquement des couleurs entières entre 1 et",n,".")
        exit(0)
    couleursUtilisees[coloration[i]]=1
    for j in range(i+1,n):
        #print(i,j,A[i-1][j-1],coloration[i],coloration[j])
        if A[i][j]==1 and coloration[i]==coloration[j]:
            print("\nColoration NON ADMISSIBLE: les sommets",i+1,"et",j+1,"sont adjacents et ont la même couleur")
            exit(0)

nbCouleurUtilisees=0
for i in range(n):
    if couleursUtilisees[i]==1:
        nbCouleurUtilisees=nbCouleurUtilisees+1

print("\nColoration ADMISSIBLE en",nbCouleurUtilisees,"couleurs.")