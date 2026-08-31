import numpy as np

A = np.array([
    [1, 2, 3],   # matrice 2x3
    [4, 5, 6]
])

B = np.array([
    [7, 8],      # matrice 3x2
    [9, 10],
    [11, 12]
])

# A a 3 colonnes, B a 3 lignes ⇒ produit possible
produit = np.dot(A, B)
print("Produit A × B :\n", produit)
