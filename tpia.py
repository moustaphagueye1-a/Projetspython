import pandas as pd # Importe pandas pour gérer les tableaux de données
import matplotlib.pyplot as plt # Importe matplotlib pour les graphiques
import seaborn as sns # Importe seaborn pour la heatmap

# --- CONFIGURATION ---
file_path = r"C:\Users\Admin\Downloads\tpia.csv"

try:
    # 1. CHARGEMENT : On saute les 16 lignes d'en-tête pour arriver aux données
    df_raw = pd.read_csv(file_path, skiprows=16)
    
    # 2. PRÉPARATION : On définit les mois et on pivote le tableau
    # On transforme les lignes (paramètres) en colonnes pour le graphique
    months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    df_plot = df_raw.set_index('PARAMETER')[months].T
    
    print(" Données prêtes. Génération des graphiques...")

    # 3. TRACER LES COURBES : Boucle automatique sur TOUS les paramètres
    for colonne in df_plot.columns:
        plt.figure(figsize=(10, 5)) # Définit la taille de la fenêtre
        
        # On trace la courbe pour la colonne actuelle de la boucle
        plt.plot(df_plot.index, df_plot[colonne], marker='o', linestyle='-', label=colonne, linewidth=2)
        
        # Personnalisation du graphique
        plt.title(f'Évolution mensuelle : {colonne}') # Titre dynamique selon le paramètre
        plt.xlabel('Mois') # Nom de l'axe X
        plt.ylabel('Valeur / Unité') # Nom de l'axe Y
        plt.legend() # Affiche la légende
        plt.grid(True, linestyle='--', alpha=0.6) # Ajoute une grille pointillée
        plt.show() # Affiche le graphique et attend qu'on le ferme pour passer au suivant

    # 4. FAIRE LE HEATMAP : Une vue globale de toutes les données
    plt.figure(figsize=(12, 8))
    # On affiche les paramètres en lignes et les mois en colonnes
    sns.heatmap(df_plot.T, annot=True, cmap='RdYlBu_r', fmt=".2f", cbar_kws={'label': 'Échelle des valeurs'})
    plt.title('Heatmap globale des 6 paramètres agroclimatiques')
    plt.show()

except Exception as e:
    print(f" Erreur lors de l'exécution : {e}")
