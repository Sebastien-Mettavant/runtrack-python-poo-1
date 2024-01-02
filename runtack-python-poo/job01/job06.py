class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def afficher_age(self):
        print(f"L'âge de l'animal est de {self.age} ans.")

# Instanciation d'un objet Animal
mon_animal = Animal()

# Affichage de l'âge initial
mon_animal.afficher_age()

# Faire vieillir l'animal
mon_animal.vieillir()

# Affichage de l'âge après avoir fait vieillir l'animal
mon_animal.afficher_age()  # L'âge de l'animal est maintenant de 1 an.
