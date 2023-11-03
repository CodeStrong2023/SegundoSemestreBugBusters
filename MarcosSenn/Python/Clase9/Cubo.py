class Cubo:
    def __init__(self):
        self.ancho = 0
        self.alto = 0
        self.profundidad = 0

    def ingresar_valores(self):
        self.ancho = float(input("Ingresa el ancho del cubo: "))
        self.alto = float(input("Ingresa la altura del cubo: "))
        self.profundidad = float(input("Ingresa la profundidad del cubo: "))

    def calcular_volumen(self):
        volumen = self.ancho * self.alto * self.profundidad
        return volumen

# Ejemplo de uso:
cubo = Cubo()
cubo.ingresar_valores()
volumen = cubo.calcular_volumen()
print(f"El volumen del cubo es: {volumen}")
