from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
import pandas as pd
import matplotlib.pyplot as plt

inputData = pd.read_csv(r"C:\Users\Admin\OneDrive\Mes python\logement.csv")

# Vérifier s'il y a des contradictions dans les données (mêmes attributs, résultats différents)
doublons = inputData.duplicated(subset=['Emplacement','Type de maison','Revenu','Client anterieur'], keep=False)
print("Lignes en conflit :")
print(inputData[doublons])

X = inputData[['Emplacement','Type de maison','Revenu','Client anterieur']]
X = pd.get_dummies(X)
Y = inputData['Resultat'].values

# Dataset trop petit (14 lignes) pour un split train/test fiable -> entraînement sur tout
model = DecisionTreeClassifier(max_depth=None)
model.fit(X, Y)

print("Précision sur les données d'entraînement", model.score(X, Y))

print(export_text(model, feature_names=X.columns.tolist()))

plot_tree(model, feature_names=X.columns.tolist(),
          class_names=model.classes_, filled=True)
plt.show()
