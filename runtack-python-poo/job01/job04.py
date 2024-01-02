class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def se_presenter(self):
        return (f"Je suis {self.nom} {self.prenom}.")

# Instanciation de plusieurs personnes avec des valeurs de construction
personne1 = Personne("Doe", "John")
personne2 = Personne("Dupont", "jean")

# Appel de la méthode SePresenter pour chaque personne
print(personne1.se_presenter())

print(personne2.se_presenter())
