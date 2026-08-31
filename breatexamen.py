# Importation des modules nécessaires
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import metrics

# -----------------------------
# Importation du dataset
# -----------------------------
features = [
    'radius_mean','texture_mean','perimeter_mean','area_mean','smoothness_mean',
    'compactness_mean','concavity_mean','concave_points_mean','symmetry_mean','fractal_dim_mean',
    'radius_se','texture_se','perimeter_se','area_se','smoothness_se',
    'compactness_se','concavity_se','concave_points_se','symmetry_se','fractal_dim_se',
    'radius_worst','texture_worst','perimeter_worst','area_worst','smoothness_worst',
    'compactness_worst','concavity_worst','concave_points_worst','symmetry_worst','fractal_dim_worst'
]

# skiprows=1 : on saute la ligne d'en-tête brute (569,30,malignant,benign)
# header=None + names=... : on donne nous-mêmes les vrais noms de colonnes
inputData = pd.read_csv("breast_cancer.csv", skiprows=1, header=None, names=features + ['class'])

print(inputData.columns.tolist())
print(inputData.head())
print(f"\nNombre d'instances : {len(inputData)}")
print(f"Répartition des classes :\n{inputData['class'].value_counts()}")
print("(0 = malignant / malin, 1 = benign / bénin)\n")

# -----------------------------
# Déclaration de l'arbre de décision
# -----------------------------
model = DecisionTreeClassifier(max_depth=2)

# -----------------------------
# Entraînement de l'arbre de décision
# -----------------------------
X = inputData[features]
X.values
Y = inputData['class'].values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

print('train set', X_train.shape, Y_train.shape)
print('test set', X_test.shape, Y_test.shape)

model.fit(X_train, Y_train)

print("Précision", model.score(X_test, Y_test))
print("Evaluation test", model.predict(X_test))

# -----------------------------
# Afficher la matrice de confusion
# -----------------------------
confusion_matrix = metrics.confusion_matrix(Y_test, model.predict(X_test))
print("\nMatrice de confusion :")
print(confusion_matrix)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix,
                                             display_labels=["malignant", "benign"])
cm_display.plot()
plt.show()

# -----------------------------
# Affichage de l'arbre de décision obtenue après entraînement
# -----------------------------
plt.figure(figsize=(20, 10))
plot_tree(model, feature_names=features,
          class_names=["malignant", "benign"], filled=True)
plt.show()
