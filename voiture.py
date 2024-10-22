from dataclasses import dataclass

@dataclass
class Voiture:
    essence: int = 100

    def afficher_reservoir(self):
        print(f"La voiture contient {self.essence} litres d'essence")

    def roule(self, km):
        conso = km * 5 / 100
        if self.essence == 0:
            print("Vous n'avez plus d'essence, faites le plein !")
        else:
            self.essence -= conso
            if self.essence < 0:
                self.essence = 0
            if self.essence < 10:
                print("Vous n'avez bientôt plus d'essence !")
            self.afficher_reservoir()

    def faire_le_plein(self):
        self.essence = 100
        print("Vous pouvez repartir !")


