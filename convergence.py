import numpy as np

def calcul_vecteur_invariant(P, nb_iteration):
    """
    Calcule le vecteur invariant d'une matrice stochastique P.
    
    P : Matrice carrée (numpy array) où la somme de chaque ligne vaut 1.
    nb_iteration : Nombre de fois que l'on multiplie le vecteur par la matrice.
    """
    # 1. [li, col] = size(P)
    li = P.shape[0]
    
    # 2. Pi_0 = rand(1, li) 
    # On génère un vecteur aléatoire de taille (1, li)
    pi_0 = np.random.rand(li)
    
    # 3. Normalisation pour que Pi_0 soit stochastique (la somme = 1)
    # sum_li = Σ Pi_0[i]
    pi_0 = pi_0 / np.sum(pi_0)
    
    # 4. X = Pi_0
    X = pi_0
    
    # 5. Boucle de convergence : X = X * P
    for i in range(nb_iteration):
        X = np.dot(X, P)
        
    return X

# --- EXEMPLE D'UTILISATION ---# Matrice de transition P (stochastique par ligne)
matrice_P = np.array([
    [0.7, 0.3],
    [0.4, 0.6]
])

iterations = 50
vecteur_final = calcul_vecteur_invariant(matrice_P, iterations)

print(f"Vecteur invariant après {iterations} itérations :")
print(vecteur_final)
