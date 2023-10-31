class Persona: # Creamos una clase
    def __init__(self, nombre, apellido, edad): # Metodo especial, se lo llama Init Dunder
        self.nombre = nombre # Atributos y el otro variables
        self.apellido = apellido
        self.edad = edad
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

persona1 = Persona("Belén", "Limachi", 30) # Necesitamos enviar argumentos
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} su edad es: {persona1.edad}')

persona2 = Persona("Ariel", "Betancud", 40)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} su edad es: {persona2.edad}')

persona1.nombre = "Martín"
persona1.apellido = "Olivares"
persona1.edad = 8
print(f'El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} su edad es: {persona1.edad}')

# Los atributos son: caracteristicas
# Los métodos son: el comportamiento que van a tener los objetos (las acciones)
persona1.mostrar_detalle()
persona2.mostrar_detalle()