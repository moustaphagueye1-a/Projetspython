from datetime import datetime

# Demander la date de naissance à l’utilisateur
date_str = input("Entre ta date de naissance (format AAAA-MM-JJ) : ")

# Convertir la chaîne en objet datetime
date_naissance = datetime.strptime(date_str, "%Y-%m-%d")

# Date actuelle
aujourdhui = datetime.now()

# Calcul de l’âge
age = aujourdhui.year - date_naissance.year
if (aujourdhui.month, aujourdhui.day) < (date_naissance.month, date_naissance.day):
    age -= 1

print("Tu as", age, "ans.")
