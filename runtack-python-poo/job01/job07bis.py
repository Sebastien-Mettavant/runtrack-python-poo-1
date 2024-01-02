class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficher_position(self):
        print(f"Position du personnage : ({self.x}, {self.y})")


class Jeu:
    def __init__(self, taille_plateau):
        self.taille_plateau = taille_plateau
        self.plateau = [[0] * taille_plateau for _ in range(taille_plateau)]
        self.mon_personnage = Personnage(0.4, 0.5)

    def afficher_plateau(self):
        for ligne in self.plateau:
            print(ligne)

    def deplacer_personnage(self, nouvelle_x, nouvelle_y):
        if 0 <= nouvelle_x < self.taille_plateau and 0 <= nouvelle_y < self.taille_plateau:
            self.mon_personnage.x, self.mon_personnage.y = nouvelle_x, nouvelle_y
            self.plateau[nouvelle_x][nouvelle_y] = 1
            self.afficher_plateau()
            self.mon_personnage.afficher_position()
        else:
            print("Déplacement en dehors des limites du plateau.")


# Exemple d'utilisation
taille_plateau_jeu = 20

jeu = Jeu(taille_plateau_jeu)

# Afficher l'état initial du plateau
jeu.afficher_plateau()

# Afficher la position initiale du personnage
jeu.mon_personnage.afficher_position()

# Déplacer le personnage vers une nouvelle position (4, 1)
jeu.deplacer_personnage(4, 1)

# Tentative de déplacement en dehors des limites du plateau (6, 2)
jeu.deplacer_personnage(6, 2)
