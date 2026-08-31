# Importation des modules nécessaires
from sklearn.tree import DecisionTreeClassifier, plot_tree
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import metrics

# -----------------------------
# Importation du dataset
# -----------------------------
inputData = pd.read_csv(
    "irris.csv",
    skiprows=1, header=None,
    names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
)

print("Colonnes :", inputData.columns.tolist())
print(inputData.head())
print(f"\nNombre d'instances : {len(inputData)}")
print(f"Répartition des classes :\n{inputData['class'].value_counts()}")
print("(0 = setosa, 1 = versicolor, 2 = virginica)\n")

# -----------------------------
# Déclaration de l'arbre de décision
# -----------------------------
model = DecisionTreeClassifier(max_depth=2)

# -----------------------------
# Entraînement de l'arbre de décision
# -----------------------------
X = inputData[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
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
                                             display_labels=["setosa", "versicolor", "virginica"])
cm_display.plot()
plt.show()

# -----------------------------
# Affichage de l'arbre de décision obtenue après entraînement
# -----------------------------
plt.figure(figsize=(24, 14))
plot_tree(model, feature_names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'],
          class_names=["setosa", "versicolor", "virginica"],
          filled=True,
          fontsize=9)
plt.tight_layout()
plt.show()
