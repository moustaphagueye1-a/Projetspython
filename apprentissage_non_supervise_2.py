import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

# ===== Les 8 points de l'exercice =====
points = np.array([
    [2, 10],  # A1
    [2, 5],   # A2
    [8, 4],   # A3
    [5, 8],   # A4
    [7, 5],   # A5
    [6, 4],   # A6
    [1, 2],   # A7
    [4, 9]    # A8
])
noms = ['A1','A2','A3','A4','A5','A6','A7','A8']

# ===== 1. Matrice de distances euclidiennes =====
matrice_distances = cdist(points, points, metric='euclidean')

print("Matrice de distances euclidiennes :")
print("      " + "   ".join(f"{n:>5}" for n in noms))
for i, n in enumerate(noms):
    ligne = "  ".join(f"{matrice_distances[i][j]:5.2f}" for j in range(8))
    print(f"{n:>4}  {ligne}")

# ===== 2. K-means avec centres initiaux imposés : A1, A4, A7 =====
centres_initiaux = np.array([
    [2, 10],  # A1
    [5, 8],   # A4
    [1, 2]    # A7
])

# n_init=1 car on impose l'initialisation (pas de tirage aléatoire)
model = KMeans(n_clusters=3, init=centres_initiaux, n_init=1, random_state=0)
model.fit(points)

print("\nClusters finaux (après convergence) :")
for i, n in enumerate(noms):
    print(f"{n} {tuple(points[i])} -> Cluster {model.labels_[i]}")

print("\nCentres finaux :")
for i, c in enumerate(model.cluster_centers_):
    print(f"Cluster {i} : ({c[0]:.2f}, {c[1]:.2f})")

print(f"\nNombre d'itérations effectuées : {model.n_iter_}")

# ===== 3. Représentation graphique =====
couleurs = np.array(['purple', 'teal', 'orange'])

plt.figure(figsize=(7, 6))
plt.scatter(points[:, 0], points[:, 1], c=couleurs[model.labels_], s=100)

# étiqueter chaque point
for i, n in enumerate(noms):
    plt.annotate(n, (points[i, 0], points[i, 1]), textcoords="offset points", xytext=(8, 5))

# afficher les centres finaux
plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1],
            c='black', marker='X', s=200, label='Centres')

plt.xlabel("x")
plt.ylabel("y")
plt.title("K-means : 8 points en 3 clusters")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.4)
plt.show()
