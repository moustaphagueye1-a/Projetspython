import numpy as np
import matplotlib.pyplot as plt

def d2():
    x = np.linspace(0.1, 10, 500)  # Éviter x=0 à cause de ln(x)
    y = x * np.sin(x) + np.log(x)

    plt.plot(x, y, label="f(x) = x·sin(x) + ln(x)", color="red")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Tracé 2D de f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()

# tracer_fonction_2d()
from mpl_toolkits.mplot3d import Axes3D

def d3():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X) * np.cos(Y)

    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("f(x, y)")
    ax.set_title("Tracé 3D de f(x, y) = sin(x)·cos(y)")
    plt.show()

# tracer_fonction_3d()
