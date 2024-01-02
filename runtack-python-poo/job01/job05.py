class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficher_les_points(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")

    def afficher_x(self):
        print(f"La coordonnée horizontale x : {self.x}")

    def afficher_y(self):
        print(f"La coordonnée verticale y : {self.y}")

    def changer_x(self, nouvelle_valeur_x):
        self.x = nouvelle_valeur_x

    def changer_y(self, nouvelle_valeur_y):
        self.y = nouvelle_valeur_y

# Exemple d'utilisation de la classe Point
point1 = Point(8, 12)

# Affichage des coordonnées initiales
point1.afficher_les_points()

# Affichage des coordonnées x et y
point1.afficher_x()
point1.afficher_y()

# Changement des coordonnées
point1.changer_x(7)
point1.changer_y(10)

# Affichage des nouvelles coordonnées
point1.afficher_les_points()
