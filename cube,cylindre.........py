import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# ➤ Cylindre (3D)
def tracer_cylindre():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    z = np.linspace(0, 5, 100)
    theta = np.linspace(0, 2 * np.pi, 100)
    theta_grid, z_grid = np.meshgrid(theta, z)
    x = np.cos(theta_grid)
    y = np.sin(theta_grid)
    ax.plot_surface(x, y, z_grid, color='skyblue')
    plt.title("Cylindre")
    plt.show()

# ➤ Parallélépipède (3D)
def tracer_parallelepipede():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = [0, 1, 1, 0, 0, 1, 1, 0]
    y = [0, 0, 1, 1, 0, 0, 1, 1]
    z = [0, 0, 0, 0, 1, 1, 1, 1]
    vertices = [[0,1,2,3],[4,5,6,7],[0,1,5,4],[2,3,7,6],[1,2,6,5],[0,3,7,4]]

    for face in vertices:
        ax.plot([x[i] for i in face + [face[0]]],
                [y[i] for i in face + [face[0]]],
                [z[i] for i in face + [face[0]]], color='green')
    plt.title("Parallélépipède")
    plt.show()

# ➤ Cube (3D)
def tracer_cube():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    r = [0, 1]
    for s, e in combinations(np.array(list(product(r, r, r))), 2):
        if np.sum(np.abs(s - e)) == 1:
            ax.plot3D(*zip(s, e), color="blue")
    plt.title("Cube")
    plt.show()

# ➤ Losange (2D)
def tracer_losange():
    x = [0, 1, 0, -1, 0]
    y = [0, 1, 2, 1, 0]
    plt.plot(x, y, color='purple')
    plt.title("Losange")
    plt.grid(True)
    plt.axis("equal")
    plt.show()

# ➤ Parallélogramme (2D)
def tracer_parallelogramme():
    x = [0, 2, 3, 1, 0]
    y = [0, 0, 2, 2, 0]
    plt.plot(x, y, color='orange')
    plt.title("Parallélogramme")
    plt.grid(True)
    plt.axis("equal")
    plt.show()

# ➤ Trapèze (2D)
def tracer_trapeze():
    x = [0, 3, 2.5, 0.5, 0]
    y = [0, 0, 2, 2, 0]
    plt.plot(x, y, color='brown')
    plt.title("Trapèze")
    plt.grid(True)
    plt.axis("equal")
    plt.show()

# ➤ Menu principal
from itertools import product, combinations

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Tracer un cylindre")
        print("2. Tracer un parallélépipède")
        print("3. Tracer un cube")
        print("4. Tracer un losange")
        print("5. Tracer un parallélogramme")
        print("6. Tracer un trapèze")
        print("7. Quitter")

        choix = input("Entrez votre choix : ")
        if choix == "1":
            tracer_cylindre()
        elif choix == "2":
            tracer_parallelepipede()
        elif choix == "3":
            tracer_cube()
        elif choix == "4":
            tracer_losange()
        elif choix == "5":
            tracer_parallelogramme()
        elif choix == "6":
            tracer_trapeze()
        elif choix == "7":
            break
        else:
            print("Choix invalide.")

# ➤ Lancer le programme
menu()
