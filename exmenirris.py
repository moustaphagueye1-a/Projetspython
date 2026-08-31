import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets
from scipy.stats import mode

# Chargement des données
iris = datasets.load_iris()
x = pd.DataFrame(iris.data, columns=['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width'])
y = iris.target

# --- Figure 1 : Sepal ---
plt.figure(figsize=(5,5))
plt.scatter(x.Sepal_Length, x.Sepal_Width, c=y, cmap='tab10', s=30)
plt.xlabel("Longueur du sépal (cm)")
plt.ylabel("Largeur du sépal (cm)")
plt.title("Sepal")
plt.show()

# --- Figure 2 : Petal ---
plt.figure(figsize=(5,5))
plt.scatter(x.Petal_Length, x.Petal_Width, c=y, cmap='tab10', s=30)
plt.xlabel("Longueur du pétale (cm)")
plt.ylabel("Largeur du pétale (cm)")
plt.title("Petal")
plt.show()

# --- K-Means ---
model = KMeans(n_clusters=3, n_init=10, random_state=0)
model.fit(x)
labels = model.labels_

# Réalignement des labels K-Means avec les vrais labels
aligned_labels = np.zeros_like(labels)
for i in range(3):
    mask = (labels == i)
    aligned_labels[mask] = mode(y[mask], keepdims=True).mode[0]

colormap = np.array(['gold','green','royalblue'])

# Handles pour la légende (créés une seule fois, réutilisés sur les deux subplots)
handles = [plt.Line2D([0],[0], marker='o', color='w', markerfacecolor=c, markersize=8)
           for c in colormap]

# --- Figure 3 : Comparaison réelle vs K-Means ---
fig, axes = plt.subplots(1, 2, figsize=(10,4))

axes[0].scatter(x.Petal_Length, x.Petal_Width, c=colormap[y], s=40)
axes[0].set_title("Classification réelle")
axes[0].set_xlabel("Longueur du pétale (cm)")
axes[0].set_ylabel("Largeur du pétale (cm)")
axes[0].legend(handles, iris.target_names, title="Espèce")

axes[1].scatter(x.Petal_Length, x.Petal_Width, c=colormap[aligned_labels], s=40)
axes[1].set_title("Classification K-Means")
axes[1].set_xlabel("Longueur du pétale (cm)")
axes[1].set_ylabel("Largeur du pétale (cm)")
axes[1].legend(handles, iris.target_names, title="Espèce")

plt.tight_layout()
plt.show()

# Précision du clustering
accuracy = np.mean(aligned_labels == y)
print("Précision du clustering K-Means:", accuracy)
