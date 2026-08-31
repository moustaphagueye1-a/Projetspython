import pandas as pd
import numpy as np
import sklearn.metrics as sm
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets

# chargement de base de données iris
iris = datasets.load_iris()

# affichage des données (optionnel)
print(iris.data)
print(iris.feature_names)
print(iris.target)
print(iris.target_names)

# Stocker les données en tant que DataFrame Pandas
x = pd.DataFrame(iris.data)
# définir les noms de colonnes
x.columns = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_width']

y = pd.DataFrame(iris.target)

# ===== Méthode du coude (Elbow method) =====
# Calcule l'inertie (somme des distances au carré aux centres) pour différents k
inerties = []
k_range = range(1, 11)  # on teste k de 1 à 10

for k in k_range:
    model_k = KMeans(n_clusters=k, n_init=10)
    model_k.fit(x)
    inerties.append(model_k.inertia_)  # inertia_ = somme des distances² intra-cluster

# Affichage du graphe du coude
plt.figure(figsize=(6,4))
plt.plot(k_range, inerties, marker='o')
plt.xlabel("Nombre de clusters (k)")
plt.ylabel("Inertie")
plt.title("Méthode du coude")
plt.xticks(k_range)
plt.show()

# ===== Saisie du nombre de clusters choisi visuellement =====
n_clusters = int(input("Entrez le nombre de clusters choisi (d'après le graphe du coude) : "))

# Cluster K-means
model = KMeans(n_clusters=n_clusters)

# adapter le modèle de données
model.fit(x)

# afficher le clustering fait par l'algorithme K-Means
print(model.labels_)

# Visualisez les résultats du classificateur
plt.scatter(x.Petal_Length, x.Petal_width)

# Pour tracer en fonction de la longueur et de la largeur des pétales
colormap = np.array(['yellow','green','blue','red','purple','orange','cyan','magenta','brown','grey'])

plt.scatter(x.Petal_Length, x.Petal_width, c=y, s=40)

plt.scatter(x.Petal_Length, x.Petal_width, c=colormap[model.labels_], s=40)

plt.legend(iris.target_names, loc="upper left", title="Ranking")

plt.show()
