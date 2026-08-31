import numpy as n

matrice = n.array([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 16]] 

)
def extraire_ligne():
    print("nb les indices commencent par 0\n")
    L = int(input("Donner la ligne à extraire : "))
    if 0 <= L < len(matrice):
        ligne = matrice[L]
        print("Ligne extraite :", ligne)
    else:
        print("Indice de ligne invalide.")
def extraire_colonne():
    print("nb les indices commencent par 0\n")
    c = int(input("Donner la colonne à extraire : "))
    if 0 <= c < len(matrice[0]):
        colonne = matrice[: , c]
        print("Colonne extraite :", colonne)
    else:
        print("Indice de colonne invalide.")
def maximal() :
    ma=n.max(matrice)
    print("La valeur maximale de la matrice est egale a ",ma)
def minimal() :
    mi=n.min(matrice)
    print("La valeur minimale  de la matrice est egale a ",mi)
def somyenne():
    somme = n.sum(matrice)
    moyenne = n.mean(matrice)
    print("la sommme  de la matrice est \n", somme)
    print("la moyenne de la matrice est \n", moyenne)
def diago():
    diago=n.diagonal(matrice)
    print("La diogonale d une matrice est :",diago)
def secon():#diagonale secondaire 
    ds=n.fliplr(matrice).diagonal()
    print("La diogonale d une matrice est :",ds)



      
# 1. Transposer la matrice
M_transposee = matrice.T
print("\nTransposée de M :\n", M_transposee)

# 2. Vérifier si la matrice est symétrique
# Une matrice est symétrique si M = M.T
if n.array_equal(matrice, M_transposee):
    print("\nLa matrice est symétrique.")
else:
    print("\nLa matrice n'est pas symétrique.")

# 3. Créer une matrice identité de même taille
identite = n.identity(matrice.shape[0])
print("\nMatrice identité de même taille :\n", identite)

# 4. Calculer le produit matriciel entre M et sa transposée
produit = n.dot(matrice, M_transposee)
print("\nProduit matriciel M x Mᵀ :\n", produit)

    




    
