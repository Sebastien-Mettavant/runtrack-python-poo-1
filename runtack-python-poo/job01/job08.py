class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changer_rayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def afficher_infos(self):
        print(f"Informations du cercle - Rayon : {self.rayon}")

    def circonference(self):
        return 2 * 3 * self.rayon  # Utilisation d'une valeur approximative de pi

    def aire(self):
        return 3 * (self.rayon ** 2)  # Utilisation d'une valeur approximative de pi
#on peut aussi se servir de la valeur appoximative de pi
    def diametre(self):
        return 2 * self.rayon

# Création de deux cercles avec des rayons 4 et 7
cercle1 = Cercle(9)
cercle2 = Cercle(6)

# Affichage des informations pour chaque cercle
cercle1.afficher_infos()
cercle2.afficher_infos()

# Affichage de la circonférence pour chaque cercle
print(f"Circonférence du cercle1 : {cercle1.circonference()}")
print(f"Circonférence du cercle2 : {cercle2.circonference()}")

# Affichage de l'aire pour chaque cercle
print(f"Aire du cercle1 : {cercle1.aire()}")
print(f"Aire du cercle2 : {cercle2.aire()}")

# Affichage du diamètre pour chaque cercle
print(f"Diamètre du cercle1 : {cercle1.diametre()}")
print(f"Diamètre du cercle2 : {cercle2.diametre()}")
