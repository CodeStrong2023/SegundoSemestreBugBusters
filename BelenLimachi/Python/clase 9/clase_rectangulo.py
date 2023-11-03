class Rectangulo:
    '''
    Crear una clase llamada Rectangulo, debe tenér 2 atributos: altura y base el
    nombre del método será calcular el área utilizando la formula:
    area = base * altura. Pero la base y la altura deben ser ingresadas por el
    usuario y los objetos deben ser tres.

    '''
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return self.base * self.altura

base = int(input("Digite el número de la base del rectangulo: "))
altura = int(input("Digite el número de la altura del rectangulo: "))
rectangulo1 = Rectangulo(base, altura)
print(f'El área del rectangulo es: {rectangulo1.calcular_area()}')