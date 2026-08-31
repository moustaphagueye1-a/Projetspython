from datetime import datetime
moisnaiss = int(input("Donner votre mois de naissance "))
journaiss = int(input("Donner votre jour naissance "))
anneenaiss = int(input("Donner votre annee de naissance "))
aujourdhui = datetime.now()
age=aujourdhui.year - anneenaiss
if (aujourdhui.month, aujourdhui.day) < (moisnaiss,journaiss ):
    age=age-1
print("Tu as", age, "ans.")
