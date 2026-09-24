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


class VanneGoutteAGoutte(Vanne):
    def __init__(self, emplacement):
        super().__init__(emplacement)

    def debit_max(self):
        return 10


class VanneAspersion(Vanne):
    def __init__(self, emplacement):
        super().__init__(emplacement)

    def debit_max(self):
        return 50

    def etat(self):
        return super().etat() + " Fort débit"


v1 = VanneGoutteAGoutte("parcelle A")
v2 = VanneAspersion("parcelle B")
print(v1.debit_max())
print(v2.debit_max())
print(v1.etat())
print(v2.etat())
          
        
    
