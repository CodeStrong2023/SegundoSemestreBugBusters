class Cubo:
    '''Crear la clase cubo con los atributos, ancho, alto y profundidad, con
    un método calcular_volumen que tendrá la formula:
    volumen = ancho * altura * profundidad
    que el ususario ingrese los valores
    '''
    def __init__(self, ancho, altura, prof):
        self.ancho = ancho
        self.altura = altura
        self.prof = prof

    def calcular_volumen(self):
        return self.ancho * self.altura * self.prof

ancho= int(input('Digite el ancho del cubo: '))
altura = int(input('Digite la altura del cubo: '))
prof = int(input('Digite la profundidad del cubo: '))

cubo1 = Cubo(ancho, altura, prof)
print(f'El volumen del cubo es: {cubo1.calcular_volumen()}')
