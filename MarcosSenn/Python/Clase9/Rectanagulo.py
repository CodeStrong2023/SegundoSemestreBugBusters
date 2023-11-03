class Rectangulo:
    def __init__(self, base, altura):

        if base > 0 and altura > 0:
            self.base = base
            self.altura = altura
        else:
            raise ValueError("Tanto la base como la altura deben ser valores positivos")

    def calcular_area(self):
        area = self.base * self.altura
        return area


base = 5
altura = 4
rectangulo = Rectangulo(base, altura)
area = rectangulo.calcular_area()
print(f"El área del rectángulo es: {area}")
