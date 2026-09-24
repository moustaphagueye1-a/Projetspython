class VanneException(Exception):
    pass


class EmplacementInvalideException(VanneException):
    pass


class DebitInvalideException(VanneException):
    pass


class Vanne:
    def __init__(self, emplacement, debit):
        if len(emplacement) < 3:
            raise EmplacementInvalideException("L'emplacement ne peut pas être inférieur à 3 caractères")
        if debit <= 0:
            raise DebitInvalideException("Le débit ne peut pas être négatif ou nul")

        self.emplacement = emplacement
        self.debit = debit


# --- Tests ---

try:
    vanne1 = Vanne("parcelle A", 10)
    print(f"Vanne créée : {vanne1.emplacement}, débit {vanne1.debit}")
except VanneException as erreur:
    print(f"Un problème est survenu avec cette vanne : {erreur}")

try:
    vanne2 = Vanne("A", 10)
except VanneException as erreur:
    print(f"Un problème est survenu avec cette vanne : {erreur}")

try:
    vanne3 = Vanne("parcelle B", -2)
except VanneException as erreur:
    print(f"Un problème est survenu avec cette vanne : {erreur}")
