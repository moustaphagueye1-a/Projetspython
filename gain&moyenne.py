import random

# Variable globale pour stocker le gain
dernier_gain = 0

def gain():
    global dernier_gain  # on déclare qu'on veut modifier la variable globale
    tirage = random.randint(1, 15)
    if tirage <= 5:
        dernier_gain = 1000
    else:
        dernier_gain = -5000

def moyenne():
    global dernier_gain
    n = int(input("Combien de simulations voulez-vous faire ? "))
    total = 0
    for _ in range(n):
        gain()  # met à jour dernier_gain
        total += dernier_gain
    m = total / n
    print("Le gain moyen est égal à", m)

def principal():
    while True:
        choix = int(input("Taper 1 pour trouver le gain \n2 pour trouver le gain moyen \n3 pour quitter : "))
        if choix == 1:
            gain()
            print("Le gain est de", dernier_gain)
        elif choix == 2:
            moyenne()
        elif choix == 3:
            break
        else:
            print("Choix invalide, veuillez réessayer.")

# Lancer le programme
principal()
