class Parcelle:
    def __init__(self, culture, superficie, rendement=0):
        self.culture = culture
        self.superficie = superficie
        self.rendement = rendement

    def production_totale(self):
        return self.superficie * self.rendement

    def est_grande_parcelle(self):
        if self.superficie > 5:
            return True
        else:
            return False


parcelle1 = Parcelle('mil', 8, 1.2)   # ← plus du tout indenté, en dehors de la classe

    


