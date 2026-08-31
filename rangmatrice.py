import numpy as np

matrice = np.array([[1, -1, 2, 1, 2],
                    [-1, 2, 3, -4, 1],
                    
                    [0, -1, 1, 0, 0]])
print(matrice)
rang = np.linalg.matrix_rank(matrice)
print("rang = ",rang)
