import numpy as n
import matplotlib.pyplot as mp
import datetime

# Liste pour stocker les étudiants
etudiants = []

# Fonction pour saisir un étudiant
def ajouter_etudiant():
    print("\n Saisie d'un etudiant ")
    nom = input("Nom : ")
    prenom = input("Prenom : ")
    genre = input("Genre (M/F) : ").upper()
    naissance = input("Date de naissance (JJ/MM/AAAA) : ")
    niveau = input("Niveau d'etude : ")
    filiere = input("Filiere : ")
    groupe = input("Groupe d'arrosage : ")
    date_arrosage = input("Date d'arrosage (JJ/MM/AAAA) : ")

    etudiant = {
        "nom\n": nom,
        "prenom\n": prenom,
        "genre\n": genre,
        "naissance\n": naissance,
        "niveau\n": niveau,
        "filiere\n": filiere,
        "groupe\n": groupe,
        "arrosage\n": date_arrosage
    }
    etudiants.append(etudiant)
    print("Etudiant ajoute avec succes !")

# Fonction pour afficher tous les étudiants
def afficher_tous():
    print("\n Liste des etudiants ")
    for e in etudiants:
        print(e)

# Filtrer par un critère générique
def afficher_par_critere(cle, valeur):
    print(f"\n  etudiants avec {cle} = {valeur}  ")
    for e in etudiants:
        if e[cle].lower() == valeur.lower():
            print(e)

# Fonction pour trier par nom
def trier_alphabetique():
    print("\n Etudiants triés par nom ")
    sorted_list = sorted(etudiants, key=lambda x: (x["nom"].lower(), x["prenom"].lower()))
    for e in sorted_list:
        print(e)
#fonction de la coubre de la loi normale
def cln():
    x=n.random.normal(loc=5,scale=6,size=100)#pour que l abcisse x suit la loi loi normale de moyenne = 5 , d ecart-type=6 , et de taille =100
    y=n.random.normal(loc=5,scale=6,size=100)#pour que l ordonnee y  suit la loi loi normale de moyenne = 5 , d ecart-type=6 , et de taille =100
    
    mp.plot(x,y ,c="blue")#pour tracer la courbe en 
    
    mp.xlabel("abscisse")#pour ettiqueter l abcisse 
    mp.ylabel("ordonnee")#pour ettiqueter l ordonnee 
    print(y)
    mp.legend()#pour legender la courbe
    mp.grid(True)#pour mettre des la grillage
    mp.show()#pour afficher la courbe 



   

# Menu principal
def menu():
    print("BIENVENUE DANS NOTRE PROGRAMME DE GESTION DES ETUDIANT \n")
    print(" NB , il faut toujours saisir avant d utuliser les autres fonctionnalites")
    while True:
        print("\n===== Menu de l'application =====")
        print("1. Ajouter un étudiant")
        print("2. Afficher tous les étudiants")
        print("3. Afficher par genre")
        print("4. Afficher par niveau d'étude")
        print("5. Afficher par filière")
        print("6. Afficher par groupe d'arrosage")
        print("7. Trier les étudiants par nom")
        print("8. pour afficher la courbe de la loi normale")
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
            cln()
        elif choix == "0":
            print("Fermeture de l'application.")
            print("AU REVOIR")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

# Lancer le programme
menu()
