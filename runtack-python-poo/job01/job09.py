class Produit:
    def __init__(self, nom, prix_ht, tva):
        self.nom = nom
        self.prix_ht = prix_ht
        self.tva = tva

    def calculer_prix_ttc(self):
        return self.prix_ht * (1 + self.tva / 100)

    def afficher(self):
        infos = f"Nom: {self.nom}, Prix HT: {self.prix_ht}€, TVA: {self.tva}%"
        print(infos)

    def modifier_nom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifier_prix_ht(self, nouveau_prix_ht):
        self.prix_ht = nouveau_prix_ht

    def obtenir_nom(self):
        return self.nom

    def obtenir_prix_ht(self):
        return self.prix_ht

    def obtenir_tva(self):
        return self.tva


# Création de plusieurs produits
produit1 = Produit("Produit A", 20, 10)
produit2 = Produit("Produit B", 30, 15)
produit3 = Produit("Produit C", 15, 5)
produit4 = Produit("Produit d", 20, 8)
# Calcul de la TVA pour chaque produit et affichage
print("Calcul de la TVA pour chaque produit:")
print(f"{produit1.obtenir_nom()} - Prix TTC: {produit1.calculer_prix_ttc()}€")
print(f"{produit2.obtenir_nom()} - Prix TTC: {produit2.calculer_prix_ttc()}€")
print(f"{produit3.obtenir_nom()} - Prix TTC: {produit3.calculer_prix_ttc()}€")
print(f"{produit4.obtenir_nom()} - Prix TTC: {produit4.calculer_prix_ttc()}€")
# Modification du nom et du prix de chaque produit
produit1.modifier_nom("Nouveau Produit A")
produit1.modifier_prix_ht(25)

produit2.modifier_nom("Nouveau Produit B")
produit2.modifier_prix_ht(40)

produit3.modifier_nom("Nouveau Produit C")
produit3.modifier_prix_ht(18)

produit4.modifier_nom("Nouveau Produit D")
produit4.modifier_prix_ht(16)
# Affichage des nouveaux prix des produits
print("\nNouveaux prix des produits après modification:")
produit1.afficher()
produit2.afficher()
produit3.afficher()
produit4.afficher()