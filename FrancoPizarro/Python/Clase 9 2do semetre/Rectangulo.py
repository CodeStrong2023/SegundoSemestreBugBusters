class Rectangulo:
    '''Crear una clase llamada Rectangulo, debe tener 2 atributos: altura y base
    el nombre del método sera calcular_area utlizando la formula:
    area * base * altura. Pero la base y la altura deben ser ingresados por el usuario
    y los objetos deben ser tres.
    '''
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return self.altura * self.base

base = int(input('Digite el número para la base del rectangulo: '))
altura = int(input('Digite un número para la altura del rectangunlo: '))
rectangulo1 = Rectangulo(base, altura)
print(f'El area del rectangulo es: {rectangulo1.calcular_area()}')
