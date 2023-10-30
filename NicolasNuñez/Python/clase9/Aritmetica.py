class Aritmetica:
    '''
    El nombre de este tipo de comentario es: DocString.
    Vamos a hacer en esta clase algunas operaciones de: suma, resta, multiplicacion y más
    '''

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB


    # Método para sumar
    def sumar(self):
        return self.operandoA + self.operandoB

    # Método para restar
    def restar(self):
        return self.operandoA - self.operandoB

    # Método para multiplicar
    def multiplicar(self):
        return self.operandoA * self.operandoB

    # Método para dividir
    def dividir(self):
        return self.operandoA / self.operandoB

aritmetica1 = Aritmetica(7, 9)

print(f'La suma es: {aritmetica1.sumar()}')
print(f'La resta es: {aritmetica1.restar()}')
print(f'La multiplicacion es: {aritmetica1.multiplicar()}')
print(f'La division es: {aritmetica1.dividir():.2f}')