class Persona: # Creamos una clase
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs): # Se lo llama método init dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni # este atributo esta encapsulado, de manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostar_detalle(self): #self es igual a this
        print(f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self.apellido}{self.edad}, la direccion es: {self.args}, los datos importantes son: {self.kwargs}')


persona1 = Persona('Ariel', 'Betancud', 4561234846, 40) #Necesitamos enviar argumentos
'''print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)'''

print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}')

persona2 = Persona('Osvaldo', 'Giordanini', 451234684, 45)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
persona1.edad = 40
print(f'El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}')

'''
Los atributps son caracterisiticas
Los métodos son el comportamiento que van a tener los objetos (accioens)
'''
persona1.mostar_detalle() # La referencia en este caso se pasa de manera automatica
persona2.mostar_detalle()

# Persona.mostar_detalle(persona1) #Debemos pasarle una referencia para el self o dará error
persona1.telefono = '43434323234'
print(f'Este es el telefono de: {persona1.nombre} {persona1.telefono}') # Hemos creado un atributo  de un objeto

# print(persona2.telefono) # El objeto persona2 no tiene este atributo, da error
persona3 = Persona('Rogelio', 'Romero', 456486565, 22, 'Telefono', '267745478', 'Calle Lopez', 823, 'Manzana', 77, 'Casa', 18, Altura=1.83, Peso = 105, ColorFav ='Azul', Auto='Citroen', Modelo = 2021)
persona3.mostar_detalle()
# print(persona3._dni) # Esto no se Debe utilizar (esta encapsulado), esto dice que lo desconocemos python
# persona3.__nombre # Esta totalmente encapsulado