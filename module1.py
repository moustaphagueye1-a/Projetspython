def afficher_menu():
    print("=== MENU ===")
    print("1. Dire bonjour")
    print("2. Dire au revoir")

def dire_bonjour():
    print("Bonjour, comment vas-tu ?")

def dire_au_revoir():
    print("À la prochaine !")
from module1 import afficher_menu, dire_bonjour, dire_au_revoir

afficher_menu()

choix = input("Fais un choix (1 ou 2) : ")

if choix == "1":
    dire_bonjour()
elif choix == "2":
    dire_au_revoir()
else:
    print("Choix invalide.")
