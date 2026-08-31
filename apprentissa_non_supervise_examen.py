import pandas as pd
import numpy as np
import sklearn.metrics as sm
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# ===== Chargement des données climatiques =====
file_path = r"C:\Users\Admin\Downloads\humiditetemperaturepowerlac.csv"
df_raw = pd.read_csv(file_path, skiprows=10)
df_raw = df_raw.replace(-999, np.nan)

months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
df_plot = df_raw.set_index('PARAMETER')[months].T  # mois en lignes, RH2M/TS en colonnes

# affichage des données (optionnel)
print(df_plot)

# Stocker les données en tant que DataFrame Pandas (équivalent de x dans le code iris)
x = df_plot[['RH2M', 'TS']].copy()

# Standardisation (obligatoire ici : RH2M ~30-86, TS ~23-33, échelles différentes,
# contrairement à iris où les 4 mesures sont déjà dans des échelles proches en cm)
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# ===== Méthode du coude (Elbow method) =====
inerties = []
k_range = range(1, 11)
for k in k_range:
    model_k = KMeans(n_clusters=k, n_init=10)
    model_k.fit(x_scaled)
    inerties.append(model_k.inertia_)

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
model.fit(x_scaled)

# afficher le clustering fait par l'algorithme K-Means
print(model.labels_)

# Visualisez les résultats du classificateur
plt.scatter(x.RH2M, x.TS)

# Pour tracer en fonction de RH2M et TS
colormap = np.array(['yellow','green','blue','red','purple','orange','cyan','magenta','brown','grey'])

plt.scatter(x.RH2M, x.TS, c=colormap[model.labels_], s=60)

# Annoter chaque point avec le mois correspondant
for mois, row in x.iterrows():
    plt.annotate(mois, (row['RH2M'], row['TS']), textcoords="offset points", xytext=(6,4))

plt.xlabel('RH2M (%)')
plt.ylabel('TS (°C)')
plt.title(f'Clustering K-means sur RH2M et TS (k={n_clusters})')
plt.show()
