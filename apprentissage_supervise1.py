# Importation des modules nécessaires
from sklearn.tree import DecisionTreeClassifier, plot_tree
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import metrics

# Importation du dataset
inputData = pd.read_csv("diabetes.csv")

# Déclaration de l'arbre de décision
model = DecisionTreeClassifier(max_depth=2)

# Entraînement de l'arbre de décision
X = inputData[['preg','plas','pres','skin','insu','mass','pedi','age']]
X.values
Y = inputData['class'].values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.01, random_state=2)

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
plot_tree(model, feature_names=['preg','plas','pres','skin','insu','mass','pedi','age'],
          class_names=["tested_positive","tested_negative"], filled=True)

plt.show()
