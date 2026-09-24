class Capteur:
    def __init__(self, type_capteur, valeur_seuil, unite="%"):
        self.type_capteur = type_capteur
        self.valeur_seuil = valeur_seuil
        self.unite = unite


class StationIrrigation:
    def __init__(self):
        self.capteurs = []

    def ajouter_capteur(self, capteur):
        self.capteurs.append(capteur)


class Vanne:
    def __init__(self, ouverte=False):
        self.ouverte = ouverte

    def ouvrir(self):
        self.ouverte = True

    def fermer(self):
        self.ouverte = False
