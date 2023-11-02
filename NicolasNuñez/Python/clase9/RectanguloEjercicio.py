class Rectangulo:
    '''
    Crear una clase llamada Rectangulo, debe tener 2 atributos:
    altura y base. El nombre del método será calcularArea utilizando
    la formula area = base * altura. Pero la base y la altura deben ser ingresadas por el
    usuario y los objetos deben ser tres.
    '''

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura


base = int(input("Digite la base del rectangulo: "))
altura = int(input("Digite la altura del rectangulo: "))

rect1 = Rectangulo(base, altura)
print(f"El area del primer rectangulo es: {rect1.calcularArea()}")

base = int(input("Digite la base del rectangulo: "))
altura = int(input("Digite la altura del rectangulo: "))

rect2 = Rectangulo(base, altura)
print(f"El area del segundo rectangulo es: {rect2.calcularArea()}")

base = int(input("Digite la base del rectangulo: "))
altura = int(input("Digite la altura del rectangulo: "))

rect3 = Rectangulo(base, altura)
print(f"El area del tercer rectangulo es: {rect3.calcularArea()}")

