import os
from ultralytics import YOLO

# ============================================================
# CONFIGURATION
# ============================================================
# Charger le modèle (se télécharge automatiquement au premier lancement)
model = YOLO("yolov8n.pt")

def detecter_tomate(chemin_image):
    """
    Analyse une image et détermine si c'est une tomate ou non.
    """
    if not os.path.exists(chemin_image):
        print(f"Erreur : Le fichier '{chemin_image}' est introuvable.")
        return

    # Lancer la détection
    # classes=[47] : On ne cherche que la tomate
    # conf=0.25    : Seuil de certitude minimum
    results = model.predict(source=chemin_image, classes=[47], conf=0.25, verbose=False)

    # Analyser les résultats
    for r in results:
        nb_tomates = len(r.boxes)
        
        if nb_tomates > 0:
            print("-" * 30)
            print(f"RÉSULTAT :  C'est une tomate !")
            print(f"Détails : {nb_tomates} tomate(s) détectée(s).")
            # Afficher la confiance de la meilleure détection
            conf_max = float(r.boxes.conf.max())
            print(f"Confiance : {conf_max:.1%}")
            print("-" * 30)
            
            # Sauvegarder l'image avec le cadre de détection pour vérifier
            r.save(filename="resultat_tomate.jpg")
            print("L'image avec la détection a été sauvée sous 'resultat_tomate.jpg'")
        else:
            print("-" * 30)
            print("RÉSULTAT :  Ce n'est pas une tomate.")
            print("Détails : Aucun objet correspondant n'a été trouvé.")
            print("-" * 30)

# ============================================================
# LANCEMENT
# ============================================================
if __name__ == "__main__":
    # Remplace par ton chemin d'image exact
    mon_image = r"c:\Users\Admin\OneDrive\Mes python\téléchargement (5).jpg"
    
    print("Analyse en cours...")
    detecter_tomate(mon_image)