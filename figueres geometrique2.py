import matplotlib.pyplot as plt
import numpy as np

# ➤ Tracer un cercle
def tracer_cercle():
    theta = np.linspace(0, 2 * np.pi, 100)
    x = np.cos(theta)
    y = np.sin(theta)
    plt.plot(x, y, label="Cercle")
    plt.axis("equal")
    plt.title("Cercle")
    plt.grid(True)
    plt.legend()
    plt.show()

# ➤ Tracer un carré
def tracer_carre():
    x = [0, 1, 1, 0, 0]
    y = [0, 0, 1, 1, 0]
    plt.plot(x, y, label="Carré")
    plt.axis("equal")
    plt.title("Carré")
    plt.grid(True)
    plt.legend()
    plt.show()

# ➤ Tracer un rectangle
def tracer_rectangle():
    x = [0, 2, 2, 0, 0]
    y = [0, 0, 1, 1, 0]
    plt.plot(x, y, label="Rectangle")
    plt.axis("equal")
    plt.title("Rectangle")
    plt.grid(True)
    plt.legend()
    plt.show()

# ➤ Tracer un triangle
def tracer_triangle():
    x = [0, 1, 2, 0]
    y = [0, 2, 0, 0]
    plt.plot(x, y, label="Triangle")
    plt.axis("equal")
    plt.title("Triangle")
    plt.grid(True)
    plt.legend()
    plt.show()

# ➤ Tracer une ligne droite
def tracer_ligne():
    x = np.linspace(-5, 5, 100)
    y = 2 * x + 3
    plt.plot(x, y, label="y = 2x + 3")
    plt.title("Ligne droite")
    plt.grid(True)
    plt.legend()
    plt.show()

# ➤ Tracer une fonction mathématique : f(x) = x*sin(x)
def tracer_fonction():
    x = np.linspace(0.1, 10, 100)
    y = x * np.sin(x)
    plt.plot(x, y, label="f(x) = x sin(x)")
    plt.title("Fonction f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()

# ➤ Menu principal
def principal():
    while True:
        print("\nMENU : Choisissez la figure à tracer")
        print("1. Cercle")
        print("2. Carré")
        print("3. Rectangle")
        print("4. Triangle")
        print("5. Ligne droite")
        print("6. f(x) = x sin(x)")
        print("7. Quitter")
        
        choix = input("Entrez votre choix (1-7) : ")
        
        if choix == "1":
            tracer_cercle()
        elif choix == "2":
            tracer_carre()
        elif choix == "3":
            tracer_rectangle()
        elif choix == "4":
            tracer_triangle()
        elif choix == "5":
            tracer_ligne()
        elif choix == "6":
            tracer_fonction()
        elif choix == "7":
            print("Fin du programme.")
            break
        else:
            print("Choix invalide. Veuillez recommencer.")

# ➤ Lancer le programme
principal()
