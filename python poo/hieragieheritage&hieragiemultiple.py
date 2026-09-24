from abc import ABC, abstractmethod


class Vanne(ABC):
    def __init__(self, emplacement):
        self.emplacement = emplacement
        self.ouverte = False

    def etat(self):
        return f"Vanne à {self.emplacement} : {'ouverte' if self.ouverte else 'fermée'}"

    @abstractmethod
    def debit_max(self):
        pass


class VanneAspersion(Vanne):
    def __init__(self, emplacement):
        super().__init__(emplacement)

    def debit_max(self):
        return 50

    def etat(self):
        return super().etat() + " Fort débit"


class VanneAspersionRotative(VanneAspersion):
    def angle_rotation(self):
        return 360


class Connectee:
    def envoyer_alerte(self, message):
        print(f"📡 Alerte envoyée : {message}")


class VanneIoT(Vanne, Connectee):
    def debit_max(self):
        return 50


v = VanneIoT("parcelle C")
print(v.etat())
v.envoyer_alerte("Vanne connectée activée")
