parcelle = {
    "nom": "Parcelle A",
    "culture": "riz",
    "superficie_ha": 2.5,
    "irriguee": True
}
print(parcelle["culture"])       # "riz"
parcelle["superficie_ha"] = 3.0  # met à jour la valeur
for x, y in parcelle.items():
    print(x, "->", y)
