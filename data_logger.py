import serial
import json
import csv
import os
from datetime import datetime

PORT         = "COM7"
BAUD         = 9600
FICHIER_CSV  = "data.csv"
FICHIER_JSON = "data.json"

def initialiser_fichiers():
    if not os.path.exists(FICHIER_CSV):
        with open(FICHIER_CSV, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "hum_air", "temperature", "lumiere"])
        print("Fichier data.csv créé ")

    if not os.path.exists(FICHIER_JSON):
        with open(FICHIER_JSON, "w") as f:
            json.dump([], f)
        print("Fichier data.json créé ")

def enregistrer(data):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data["timestamp"] = timestamp

    # Écriture CSV
    with open(FICHIER_CSV, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            timestamp,
            data["hum_air"],
            data["temperature"],
            data["lumiere"]
        ])

    # Écriture JSON
    with open(FICHIER_JSON, "r") as f:
        liste = json.load(f)
    liste.append(data)
    with open(FICHIER_JSON, "w") as f:
        json.dump(liste, f, indent=2)

    print(f"[{timestamp}] Air:{data['hum_air']}% | Temp:{data['temperature']}°C | Lum:{data['lumiere']}")

# Programme principal
initialiser_fichiers()
print(f"Connexion sur {PORT}...")
ser = serial.Serial(PORT, BAUD, timeout=2)
print("En attente des données...\n")

while True:
    try:
        ligne = ser.readline().decode("utf-8").strip()
        if ligne.startswith("{"):
            data = json.loads(ligne)
            enregistrer(data)
    except json.JSONDecodeError:
        pass
    except KeyboardInterrupt:
        print("\nArrêt du programme.")
        ser.close()
        break
