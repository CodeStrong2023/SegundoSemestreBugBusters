class Aritmetica:
     """
     El nombre de este tipo de comentario es: DocString
     esto es documentacion de la clase de python
     Vamos a hacer en esta clase algunas operaciones de: suma, resta, multiplicacion y más
     """
     def __int__(self, operandoA, operandoB):
         self.operandoA = operandoA
         self.operandoB = operandoB
     #Metodo para sumar
     def sumar(self):
         return self.operandoA + self.operandoB

     def resta(self):
         return self.operandoA - self.operandoB

     def multiplicar(self):
         return self.operandoA * self.operandoB

     def dividir(self):
         return self.operandoA / self.operandoB

aritmetica = Aritmetica(7,9) # Le pasamos los argumentos para los operandos
print(artmetica1.sumar()
print(f'La resta de los numeros es: {aritmetica.resta()}')
print(f'La multiplicacion de los numeros es: {aritmetica.multiplicar()}')
print(f'La division de los numeros es: {aritmetica.dividir():2f}')





