import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import load_iris
iris=load_iris()
x=iris.data
y=iris.target
nom=list(iris.target_names)
plt.scatter(x[:,0],x[:,1])
plt.xlabel('longueur sépal')
plt.ylabel('Largeur sépal')
ax=plt.axes(projection='3d')
ax.scatter(x[:,0],x[:,1],x[:,2],c=y)
plt.show()
