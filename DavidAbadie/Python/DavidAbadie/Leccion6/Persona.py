class Persona:

    def __init__(self, nombre, apellido,dni, edad, *args, **kwargs):  # Se lo llama método Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni # Este atributo esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self): # self es igual a this
        print(f"La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad}, la direccion es: {self.args}, los datos importantes son: {self.kwargs}")


persona1 = Persona("Ariel", "Betancud", 32456987, 40)  # Necesitamos enviar argumentos
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
print(f"El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido}. Su edad es: {persona1.edad}")

persona2 = Persona("David", "Abadie", 43635847, 22)
print(f"El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido}. Su edad es: {persona2.edad}")

persona1.nombre = "Natalia"
persona1.apellido = "Buccella"
persona1.edad = 40
print(f"El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido}. Su edad es: {persona1.edad}")

persona1.mostrar_detalle() # La referencia en este caso se pasa de manera automatica.
persona2.mostrar_detalle()

# Persona.mostrar_detalle() # Debemos pasarle una referencia para el self o dará error

persona1.telefono = '123456787989' # Hemos creado un atributo de un objeto. Este atributo solo puede
# ser llamado por el objeto persona1.
print(persona1.telefono)

# print(persona2.telefono) # El objeto persona2 no tiene este atributo, da error.

persona3 = Persona("Rogelio", "Romero", 45123567, 22, "Telefono", "2604556677", "Calle Lopez", 823, "Manzana", 77, "Casa", 18, Altura = 1.88, Peso = 105, CFavorito = "Azul", Auto = "Citroen", Modelo = 2021)
print(persona3.mostrar_detalle())
# print(persona3._dni) # Esto no se debe utilizar en python, esto dice que lo desconocemos

persona4 = Persona("Saul", "Hudson", 12567432, 54, "Telefono", "2604120934", "Calle Libertador", 145, "Manzana", 56, "Casa", 3, Altura = 1.85, Peso = 86, CFavorito = "Negro", Auto = "Ford", Modelo = 2018)
print(persona4.mostrar_detalle())
# print(persona4.__nombre) # Esto esta totalmente encapsulado