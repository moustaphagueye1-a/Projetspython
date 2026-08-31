import numpy as np

A = np.array([[1, -1, 2],
                    [-1, 2, 3],
                    
                    [0, -1, 1]])
B = np.array([[3],
                    [-7],
                    
                    [1]])
print(A)
print(B)
x = np.linalg.solve(A,B)
print ( " le resultat de l equation  est egal a \n")
print(x)



