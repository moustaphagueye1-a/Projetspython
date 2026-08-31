# Importation des modules nécessaires
import arff as liac_arff
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import metrics

# ===== Importation du dataset .arff =====
with open(r"C:\Users\Admin\OneDrive\Mes python\choixLogement.arff", 'r', encoding='latin-1') as f:
    dataset = liac_arff.load(f)

inputData = pd.DataFrame(dataset['data'], columns=[attr[0] for attr in dataset['attributes']])

print(inputData.head())
print(inputData.dtypes)

# ===== Déclaration de l'arbre de décision =====
model = DecisionTreeClassifier(max_depth=3)

# ===== Entraînement de l'arbre de décision =====
X = inputData[['emplacement','typeMaison','revenu','clientAntérieur']]
X = pd.get_dummies(X)
Y = inputData['résultat'].values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

print('train set', X_train.shape, Y_train.shape)
print('test set', X_test.shape, Y_test.shape)

model.fit(X_train, Y_train)

print("Précision", model.score(X_test, Y_test))
print("Evaluation test", model.predict(X_test))

# Afficher la matrice de confusion
#confusion_matrix = metrics.confusion_matrix(Y_test, model.predict(X_test))
#cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix, display_labels=[False, True])
#cm_display.plot()

# Affichage de l'arbre de décision obtenue après entraînement
print(export_text(model, feature_names=X.columns.tolist()))
plot_tree(model, feature_names=X.columns.tolist(),
          class_names=model.classes_, filled=True)
plt.show()
