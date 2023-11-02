class Persona: # Creamos una clase
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs): # Se lo llama metodo Init Dunder
        self.__nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self_dni = dni # Este atributo esta encapsulado de una manera sugerida
        self.args = args
        self.kwargs = kwargs
    def mostrar_detalle(self):
        print(f' La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self.edad}, la direccion es: {self.args}, los datos importantes son: {self.kwargs}')

persona1 = Persona('Santiago', 'Segura', 45359732, '19') #Necesitamos enviar argumentos
#print(persona1.nombre) #Tarea
#print(persona1.apellido)
#print(persona1.edad)
print(f'El objeto2 de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}')


persona2 = Persona('Ariel', 'Betancud', 30321456, '40')
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}')


persona1.nombre = 'Lliliana'
persona1.apellido = 'Buccella'
persona1.edad = '40'
print(f'El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona2.edad}')


# Los atributos son: caracteristicas
# Los metodos son: el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle()
persona2.mostrar_detalle()

persona1.mostrar_detalle() #La referencia en este caso se pasa de manera automatica
persona2.mostrar_detalle()

#Persona.mostrar_detalle(persona1) # Debemos posarle una referencia para el self o dara error
persona1.telefono = "22233355567"
print(f'Este es el telefono de: {persona1.nombre} {persona1.telefono}')  # Hemos creado un atributo de un objeto

#print(persona2.telefono) el objeto persona2 no tiene este atributo, da error.
persona3 = Persona('Lucas', 'Gomez', 50395932,  '26', 'Telefono', '2604678903', 'Calle Yrigoyen', 697, 'Manzana', 88, 'Casa', 19, Altura=1.78, Peso=76, CFavorito='Azul', Auto='Chevrolet', Modelo=2023)
persona3.mostrar_detalle()
#persona3.__nombre #Esta totalmente encapsulado