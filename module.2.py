from module1 import afficher_menu, dire_bonjour, dire_au_revoir

afficher_menu()

choix = input("Fais un choix (1 ou 2) : ")

if choix == "1":
    dire_bonjour()
elif choix == "2":
    dire_au_revoir()
else:
    print("Choix invalide.")
