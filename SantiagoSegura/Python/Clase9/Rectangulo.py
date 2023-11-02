class Rectangulo:
    """
    Crear una clase llamada Rectangulo, debe tener 2 atributos: altura y base
    el nombre del metodo sera calcular area utilizando la formula:
    area = base * altura. Pero la base y la altura deben ser ingresadas por
    el usuario y los objetos deben ser tres.
    """

        def __init__(self, base, altura):
            self.base = base
            self.altura = altura

        def calcular_area(self):
            return self.base * self.altura

    # Pedir al usuario que ingrese los datos
    base1 = float(input("Ingrese la base del Rectángulo 1: "))
    altura1 = float(input("Ingrese la altura del Rectángulo 1: "))

    base2 = float(input("Ingrese la base del Rectángulo 2: "))
    altura2 = float(input("Ingrese la altura del Rectángulo 2: "))

    base3 = float(input("Ingrese la base del Rectángulo 3: "))
    altura3 = float(input("Ingrese la altura del Rectángulo 3: "))

    rectangulo1 = Rectangulo(base1,
