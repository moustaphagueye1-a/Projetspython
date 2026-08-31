import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# --- CONFIGURATION ---
file_path = r"C:\Users\Admin\Downloads\huitparametrespowerlac.csv"

try:
    # 1. CHARGEMENT
    df_raw = pd.read_csv(file_path, skiprows=16)

    # Remplacer les valeurs manquantes -999 par NaN si présentes
    df_raw = df_raw.replace(-999, np.nan)

    # 2. PRÉPARATION : mois en lignes, paramètres en colonnes
    months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    df_plot = df_raw.set_index('PARAMETER')[months].T

    print("Données prêtes. Génération des graphiques...")

    # ===== B. COURBES D'ÉVOLUTION MENSUELLE (une par paramètre) =====
    for colonne in df_plot.columns:
        plt.figure(figsize=(10, 5))
        plt.plot(df_plot.index, df_plot[colonne], marker='o', linestyle='-', label=colonne, linewidth=2)
        plt.title(f'Évolution mensuelle : {colonne}')
        plt.xlabel('Mois')
        plt.ylabel('Valeur / Unité')
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.show()

    # Heatmap globale des valeurs brutes (vue d'ensemble)
    plt.figure(figsize=(12, 8))
    sns.heatmap(df_plot.T, annot=True, cmap='RdYlBu_r', fmt=".2f", cbar_kws={'label': 'Échelle des valeurs'})
    plt.title('Heatmap globale des 8 paramètres agroclimatiques')  # 8, pas 6
    plt.tight_layout()
    plt.show()

    # ===== A. MATRICE DE CORRÉLATION ENTRE LES 8 PARAMÈTRES =====
    matrice_correlation = df_plot.corr()

    print("\nMatrice de corrélation :")
    print(matrice_correlation.round(2))

    plt.figure(figsize=(10, 8))
    sns.heatmap(matrice_correlation, annot=True, cmap='coolwarm', fmt=".2f",
                vmin=-1, vmax=1, center=0, cbar_kws={'label': 'Coefficient de corrélation'})
    plt.title('Matrice de corrélation entre les 8 paramètres climatiques')
    plt.tight_layout()
    plt.show()

    # Scatter plot pour visualiser la relation la plus forte (exemple)
    plt.figure(figsize=(7, 5))
    plt.scatter(df_plot['RH2M'], df_plot['PRECTOTCORR'], s=60, alpha=0.7)
    plt.xlabel('Humidité relative (RH2M, %)')
    plt.ylabel('Précipitations (PRECTOTCORR, mm/day)')
    plt.title('Relation entre humidité et précipitations')
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.show()

except Exception as e:
    print(f"Erreur lors de l'exécution : {e}")
