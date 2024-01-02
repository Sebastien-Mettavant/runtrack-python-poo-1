class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        self.resultat = None  # Initialize resultat to None

    def getunit(self):
        self.resultat = self.nombre1 + self.nombre2

# Instanciation de la classe avec des valeurs spécifiques
operation_instance = Operation(12, 3)

# Impression des valeurs des attributs en console avant d'appeler la méthode
print("Nombre 1:", operation_instance.nombre1)
print("Nombre 2:", operation_instance.nombre2)
#print("Résultat avant appel de la méthode:", operation_instance.resultat)
# Performing addition without using getunit()
operation_instance.resultat = operation_instance.nombre1 + operation_instance.nombre2

# Impression des valeurs des attributs en console après l'appel de la méthode
print("Résultat après addition:", operation_instance.resultat)
