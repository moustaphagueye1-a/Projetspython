from ultralytics import YOLO

# Charger le modèle pré-entraîné
model = YOLO("yolov8n.pt")

# Détecter sur l'image
results = model("C:/Users/Admin/OneDrive/Images/carotte.jpeg")

# Afficher le résultat du premier (et unique) élément
results[0].show()
