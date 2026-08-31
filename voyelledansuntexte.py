texte = "Bonjour je suis étudiant en Agrotic"
voyelles = "aeiouyAEIOUY"
compteur = 0

for lettre in texte:
    if lettre in voyelles:
        compteur += 1

print("Nombre de voyelles :", compteur)