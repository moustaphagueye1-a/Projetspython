import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

X, y = make_blobs(n_samples=100, centers=4, cluster_std=0.5, random_state=0)
plt.scatter(X[:,0], X[:, 1])

# Création du modèle K-Means avec 4 clusters
kmeans = KMeans(n_clusters=4, random_state=0)

# Entraînement du modèle sur les données
kmeans.fit(X)

# Prédiction du cluster pour chaque point
y_kmeans = kmeans.predict(X)

# Visualisation des données colorées selon leur cluster
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')

# Récupération et affichage des centres des clusters
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)

plt.show()
