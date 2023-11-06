class Persona2:
    def __init__(self, nomnre, apellido, edad): #Esta encapsulado
    self._nombre = nombre
    self._apellido = apellido
    self._ead = edad

    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}'):


    @property #Decorador
    def nombre(self): #Metodo Getter
        print('Estamos usando el metodo get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre): #Metodo Setter
        print('Estamso usando el metodo set')
        self._nombre = nombre

    @property
    def apellido(self):
        return self._nombre

    @apellido.setter
    def apellido(self, apellido):
            self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __del__(self):
        print(f'Persona2: {self.nombre} {self.apellido} {self.edad}')



if __name__ == '__main__':

persona1 = Persona2('Ariel', 'Betancud', 41)
print(persona1.nombre) #Llamamos al metodo Getter
persona1.nombre = 'Juan Pedro' #Llamamos al metodo Setter
print(persona1.nombre) #Otra vez con el metodo getter
print(persona1.mostrar_detalles()) #LLamamos el metodo mostrar detalles
# Atributo e}read-only seria la edad porque no tiene el metodo set (solo lectura)
print(persona1.edad)

#Tarea crear tres objetos más, utilizando los metodos getter and setter
# para modificar, mostrar los cambios


#Objeto numero uno de la tarea

persona2 = Persona2('Santi', 'Segura', 20)
persona2.nombre = 'Santiago'
persona2.apellido = 'Segura'
persona2.edad = 20
print(persona2.nombre)
print(persona2.apellido)
print(persona2.edad)
print(persona2.mostrar_detalles())

#Objeto numero dos de la tarea

persona3 = Persona2('Mili', 'Mercau', 20)
persona3.nombre = 'Milagoros'
persona3.apellido = 'Mercau'
persona3.edad = 19
print(persona3.nombre)
print(persona3.apellido)
print(persona3.edad)
print(persona3.mostrar_detalles())

#Objeto numero tres de la tarea

persona4 = persona2('Khaty', 'Bertoldi', 20)
persona4.nombre = 'Katharina'
persona4.apellido = 'Bertoldi'
persona4.edad = 31
print(persona4.nombre)
print(persona4.apellido)
print(persona4.edad)
print(persona4.mostrar_detalles())


print(__name__)


