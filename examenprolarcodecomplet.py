# ============================================================
# Exercice 2 - Question 2 : Étude des paramètres climatiques Sing Sing
# ============================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# --- CONFIGURATION ---
file_path = r"C:\Users\Admin\Downloads\huitparametrespowerlac.csv"

try:
    # ===== 1. CHARGEMENT ET PRÉPARATION =====
    df_raw = pd.read_csv(file_path, skiprows=16)
    df_raw = df_raw.replace(-999, np.nan)

    months = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    df_plot = df_raw.set_index('PARAMETER')[months].T  # mois en lignes, paramètres en colonnes

    print("Aperçu des données :")
    print(df_plot)

    # ============================================================
    # PARTIE B : COURBES D'ÉVOLUTION MENSUELLE (une par paramètre)
    # ============================================================
    for colonne in df_plot.columns:
        plt.figure(figsize=(10, 5))
        plt.plot(df_plot.index, df_plot[colonne], marker='o', linestyle='-',
                  label=colonne, linewidth=2)
        plt.title(f'Évolution mensuelle : {colonne}')
        plt.xlabel('Mois')
        plt.ylabel('Valeur / Unité')
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.show()

    # Heatmap globale des valeurs brutes (vue d'ensemble)
    plt.figure(figsize=(12, 8))
    sns.heatmap(df_plot.T, annot=True, cmap='RdYlBu_r', fmt=".2f",
                cbar_kws={'label': 'Échelle des valeurs'})
    plt.title('Heatmap globale des 8 paramètres agroclimatiques')
    plt.tight_layout()
    plt.show()

    # ============================================================
    # PARTIE A : MATRICE DE CORRÉLATION ENTRE LES 8 PARAMÈTRES
    # ============================================================
    matrice_correlation = df_plot.corr()

    print("\nMatrice de corrélation :")
    print(matrice_correlation.round(2))

    plt.figure(figsize=(10, 8))
    sns.heatmap(matrice_correlation, annot=True, cmap='coolwarm', fmt=".2f",
                vmin=-1, vmax=1, center=0, cbar_kws={'label': 'Coefficient de corrélation'})
    plt.title('Matrice de corrélation entre les 8 paramètres climatiques')
    plt.tight_layout()
    plt.show()

    # Scatter plot illustrant la relation la plus significative
    plt.figure(figsize=(7, 5))
    plt.scatter(df_plot['RH2M'], df_plot['PRECTOTCORR'], s=60, alpha=0.7)
    for mois, row in df_plot.iterrows():
        plt.annotate(mois, (row['RH2M'], row['PRECTOTCORR']), textcoords="offset points", xytext=(6,4))
    plt.xlabel('Humidité relative RH2M (%)')
    plt.ylabel('Précipitations PRECTOTCORR (mm/day)')
    plt.title('Relation entre humidité et précipitations')
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.show()

    # ============================================================
    # PARTIE C : APPRENTISSAGE NON-SUPERVISÉ (K-means)
    # Paramètres choisis : RH2M et TS (peu corrélés, voir interprétation)
    # ============================================================
    x = df_plot[['RH2M', 'TS']].copy()

    # Standardisation (obligatoire : RH2M ~30-86, TS ~23-33, échelles différentes)
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)

    # ----- Méthode du coude -----
    inerties = []
    k_range = range(1, 11)
    for k in k_range:
        model_k = KMeans(n_clusters=k, n_init=10, random_state=0)
        model_k.fit(x_scaled)
        inerties.append(model_k.inertia_)

    plt.figure(figsize=(6, 4))
    plt.plot(k_range, inerties, marker='o')
    plt.xlabel("Nombre de clusters (k)")
    plt.ylabel("Inertie")
    plt.title("Méthode du coude")
    plt.xticks(k_range)
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.show()

    # ----- Saisie du nombre de clusters -----
    n_clusters = int(input("Entrez le nombre de clusters choisi (d'après le graphe du coude) : "))

    model = KMeans(n_clusters=n_clusters, n_init=10, random_state=0)
    model.fit(x_scaled)

    x['cluster'] = model.labels_
    print("\nRésultat du clustering :")
    print(x)

    # ----- Visualisation -----
    plt.figure(figsize=(8, 6))
    colormap = np.array(['yellow','green','blue','red','purple','orange','cyan','magenta','brown','grey'])
    plt.scatter(x['RH2M'], x['TS'], c=colormap[model.labels_], s=80)
    for mois, row in x.iterrows():
        plt.annotate(mois, (row['RH2M'], row['TS']), textcoords="offset points", xytext=(6,4))
    plt.xlabel('RH2M (%)')
    plt.ylabel('TS (°C)')
    plt.title(f'Clustering K-means sur RH2M et TS (k={n_clusters})')
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.show()

    # ----- Centres des clusters (valeurs réelles) -----
    centres_reels = scaler.inverse_transform(model.cluster_centers_)
    df_centres = pd.DataFrame(centres_reels, columns=['RH2M', 'TS'])
    print("\nCentres des clusters (valeurs réelles) :")
    print(df_centres.round(2))

except Exception as e:
    print(f"Erreur lors de l'exécution : {e}")
