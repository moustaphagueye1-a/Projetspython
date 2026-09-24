class Vanne:
    def __init__(self, emplacement, debit):
        self.emplacement = emplacement
        self.debit = debit

    @property
    def debit_eleve(self):
        if self.debit > 30:
            return True
        else:
            return False


def resume_vannes(*args):
    for emplacement in args:
        print(f"Vanne enregistrée à {emplacement}")


v = Vanne("parcelle A", 40)
print(v.debit_eleve)

resume_vannes("parcelle A", "parcelle B", "parcelle C")
resume_vannes("parcelle D")
