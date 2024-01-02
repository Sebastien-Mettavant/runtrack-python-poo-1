class Point:
    def __init__(self, x, y, latitude, longitude):
        self.x = x
        self.y = y
        self.latitude = latitude
        self.longitude = longitude

    def afficher_les_points(self):
        print(f"Coordonnées du point : ({self.x}, {self.y}), Coordonnées géographiques : ({self.latitude}, {self.longitude})")

    def afficher_x(self):
        print(f"La coordonnée horizontale x : {self.x}")

    def afficher_y(self):
        print(f"La coordonnée verticale y : {self.y}")

    def afficher_latitude(self):
        print(f"La latitude : {self.latitude}")

    def afficher_longitude(self):
        print(f"La longitude : {self.longitude}")

    def changer_x(self, nouvelle_valeur_x):
        self.x = nouvelle_valeur_x

    def changer_y(self, nouvelle_valeur_y):
        self.y = nouvelle_valeur_y

    def changer_latitude(self, nouvelle_latitude):
        self.latitude = nouvelle_latitude

    def changer_longitude(self, nouvelle_longitude):
        self.longitude = nouvelle_longitude

# Exemple d'utilisation de la classe Point
point1 = Point(3, 5, 37.7749, -122.4194)

# Affichage des coordonnées initiales
point1.afficher_les_points()

# Affichage des coordonnées x, y, latitude et longitude
point1.afficher_x()
point1.afficher_y()
point1.afficher_latitude()
point1.afficher_longitude()

# Changement des coordonnées et des coordonnées géographiques
point1.changer_x(7)
point1.changer_y(10)
point1.changer_latitude(40.7128)
point1.changer_longitude(-74.0060)

# Affichage des nouvelles coordonnées
point1.afficher_les_points()
