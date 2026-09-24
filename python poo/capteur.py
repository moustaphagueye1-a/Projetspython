class Capteur:
    def __init__(self,type_capteur, valeur_seuil,unite="%"):
        self.type_capteur=type_capteur
        self.valeur_seuil=valeur_seuil
        self.unite=unite
capteur1 = Capteur("humidité_sol", 30)          # unite prend "%" par défaut
capteur2 = Capteur("température", 35, "°C")     # unite précisée explicitement
print(capteur1.unite)
print(capteur2.type_capteur)
