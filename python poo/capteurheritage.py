class Capteur:
    
    def __init__(self,type_capteur,valeur_seuil,unite="%"):
        self.type_capteur=type_capteur
        self.valeur_seuil=valeur_seuil
        self.unite=unite
class CapteurPluviometrie(Capteur):
    
    def __init__(self,valeur_seuil):
        self.type_capteur="pluviométrie" 
        self.valeur_seuil=valeur_seuil
        self.unite="mm"
    def alerte_inondation(self):
        if self.valeur_seuil > 50:
            return True
        else:
            return False
capteur_pluie = CapteurPluviometrie(60)
print(capteur_pluie.type_capteur)
print(capteur_pluie.alerte_inondation())

    
     
    
   
    
    
