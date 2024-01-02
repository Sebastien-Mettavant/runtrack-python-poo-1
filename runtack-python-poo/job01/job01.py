class Operation:
    def __init__(self, nombre1=0.0, nombre2=0.0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def multiplication(self):
        resultat = self.nombre1 * self.nombre2
        return resultat

# Instanciation de la classe avec des valeurs en virgule flottante
operation_instance = Operation(3.5, 2.0)

# Impression de l'objet lui-même en console
print(operation_instance)
