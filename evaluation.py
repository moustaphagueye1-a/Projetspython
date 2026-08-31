import numpy as np
import matplotlib.pyplot as plt


etudiants = []


def ajouter_etudiant():
    print("\n--- Saisie d'un étudiant ---")
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    genre = input("Genre (M/F) : ").upper()
    naissance = input("Date de naissance (JJ/MM/AAAA) : ")
    niveau = input("Niveau d'étude : ")
    filiere = input("Filière : ")
    groupe = input("Groupe d'arrosage : ")
    date_arrosage = input("Date d'arrosage (JJ/MM/AAAA) : ")

    etudiant = {
        "nom": nom,
        "prenom": prenom,
        "genre": genre,
        "naissance": naissance,
        "niveau": niveau,
        "filiere": filiere,
        "groupe": groupe,
        "arrosage": date_arrosage
    }
    etudiants.append(etudiant)
    print("Étudiant ajouté avec succès !")


def afficher_tous():
    print("\n Liste des étudiants ")
    for e in etudiants:
        print(e)

#  fonction pour choisir le critere a afficher
def afficher_par_critere(cle, valeur):
    print(f"\n--- Étudiants avec {cle} = {valeur} ---")
    trouve = False
    for e in etudiants:
        if cle in e and e[cle].lower() == valeur.lower():
            print(e)
            trouve = True
    if not trouve:
        print("Aucun étudiant trouvé.")

# Fonction pour trier par nom
def trier_alphabetique():
    print("\n--- Étudiants triés par nom ---")
    sorted_list = sorted(etudiants, key=lambda x: (x["nom"].lower(), x["prenom"].lower()))
    for e in sorted_list:
        print(e)

# Fonction pour afficher la courbe de la loi normale
def courln():
    x=n.random.normal(loc=5,scale=6,size=100)#pour que l abcisse x suit la loi loi normale de moyenne = 5 , d ecart-type=6 , et de taille =100
    y=n.random.normal(loc=5,scale=6,size=100)#pour que l ordonnee y  suit la loi loi normale de moyenne = 5 , d ecart-type=6 , et de taille =100
    
    mp.plot(x,y ,c="black")#pour tracer la courbe en noir
    
    mp.xlabel("abscisse")#pour ettiqueter l abcisse 
    mp.ylabel("ordonnee")#pour ettiqueter l ordonnee 
    print(y)
    mp.legend()#pour legender la courbe
    mp.grid(True)#pour mettre des la grillage
    mp.show()#pour afficher la courbe 


# Menu principal
def menu():
    print("BIENVENUE DANS NOTRE PROGRAMME DE GESTION DES ÉTUDIANTS\n")
    print("NB : Il faut toujours saisir avant d'utiliser les autres fonctionnalités.")
    while True:
        print("\n===== Menu de l'application =====")
        print("1. Ajouter un étudiant")
        print("2. Afficher tous les étudiants")
        print("3. Afficher par genre")
        print("4. Afficher par niveau d'étude")
        print("5. Afficher par filière")
        print("6. Afficher par groupe d'arrosage")
        print("7. Trier les étudiants par nom")
        print("8. Afficher la courbe de la loi normale")
        print("0. Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            ajouter_etudiant()
        elif choix == "2":
            afficher_tous()
        elif choix == "3":
            genre = input("Genre (M/F) : ")
            afficher_par_critere("genre", genre)
        elif choix == "4":
            niveau = input("Niveau d'étude : ")
            afficher_par_critere("niveau", niveau)
        elif choix == "5":
            filiere = input("Filière : ")
            afficher_par_critere("filiere", filiere)
        elif choix == "6":
            groupe = input("Groupe d'arrosage : ")
            afficher_par_critere("groupe", groupe)
        elif choix == "7":
            trier_alphabetique()
        elif choix == "8":
            courln()
            
        elif choix == "0":
            print("Fermeture de l'application.")
            print("AU REVOIR")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

# Lancer le programme
menu()
