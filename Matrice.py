import numpy as n

matrice = n.array([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 16]])

def extraire_ligne(index):
    
    if 0 <= index < matrice.shape[0]:  # Vérifier si l'index est valide
        print("Ligne extraite :", matrice[index, :])
    else:
        print("Index hors limites !")
      


def extraire_colonne(index):
     if 0 <= index < matrice.shape[1]:  # Vérifier si l'index est valide
        print("Colonne extraite :", matrice[:, index])
    else:
        print("Index hors limites !")


def modifier_valeur():
     matrice[2, 3] = 0  
    print("Matrice après modification :\n", matrice)
 


def principal():
    while True:
        choix=int(input("Taper 1 pour extraire une ligne\n, 2 pour extraire une colonne \n 3 pour modifier"))
        if(choix==1):
            extraire_ligne(index)
        if(choix==2):
            extraire_colonne(index)
        if(choix==3):
            modifier_valeur()
        if(choix==4):
            break
        
        
        
