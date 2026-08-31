import matplotlib.pyplot as plt
import numpy as np

# Fonction pour tracer un cercle
def tracer_cercle():
    rayon = float(input("Entrez le rayon du cercle : "))
    theta = np.linspace(0, 2 * np.pi, 100)
    x = rayon * np.cos(theta)
    y = rayon * np.sin(theta)
    plt.plot(x, y)
    plt.gca().set_aspect('equal')
    plt.title(f"Cercle de rayon {rayon}")
    plt.grid(True)
    plt.show()

# Fonction pour tracer un rectangle
def tracer_rectangle():
    longueur = float(input("Entrez la longueur du rectangle : "))
    largeur = float(input("Entrez la largeur du rectangle : "))
    x = [0, longueur, longueur, 0, 0]
    y = [0, 0, largeur, largeur, 0]
    plt.plot(x, y)
    plt.title(f"Rectangle {longueur} x {largeur}")
    plt.axis('equal')
    plt.grid(True)
    plt.show()

# Fonction pour tracer un carré
def tracer_carre():
    cote = float(input("Entrez le côté du carré : "))
    
    plt.title(f"Carré de côté {cote}")
    plt.grid(True)
    plt.show()

# Fonction pour tracer une courbe personnalisée
def tracer_courbe():
    xmin = float(input("Entrez xmin : "))
    xmax = float(input("Entrez xmax : "))
    print("Exemple de fonction : y = x^2")
    x = np.linspace(xmin, xmax, 300)
    y = x ** 2  # Par exemple y = x^2
    plt.plot(x, y)
    plt.title("Courbe personnalisée y = x^2")
    plt.grid(True)
    plt.show()

# Fonction principale (main)
def principal():
    print("=== MENU ===")
    print("1. Tracer un cercle")
    print("2. Tracer un rectangle")
    print("3. Tracer un carré")
    print("4. Tracer une courbe personnalisée")
    
    choix = input("Choisissez une option (1-4) : ")

    if choix == "1":
        tracer_cercle()
    elif choix == "2":
        tracer_rectangle()
    elif choix == "3":
        tracer_carre()
    elif choix == "4":
        tracer_courbe()
    else:
        print("Choix invalide, veuillez choisir entre 1 et 4.")

