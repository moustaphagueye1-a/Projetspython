import numpy as n

matrice = n.array([[1,2,3],[4,5,6],[7,8,9]] 

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
def principal():
    while True:
        choix = int(input("Taper 1 pour extraire une ligne  \n2 pour extraire une colonne  \n3 pour afficher la valeur maximale de la matrice \n 4 pour quitter : "))
        if choix == 1:
            extraire_ligne()
            
            
        elif choix == 2:
            extraire_colonne()
            
        elif choix == 3:
            maximal()
        elif choix == 4:
            break
        else:
            print("Choix invalide, veuillez réessayer.")

# Lancer le programme
principal()
