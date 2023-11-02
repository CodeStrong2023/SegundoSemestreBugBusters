class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property # decorador
    def nombre(self): #Metodo getter
        print('Estamos utilizando el método get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        print('Estamos utilizando el método set')
        self._nombre = nombre

    @property
    def apellido(self):
        print('Estamos utilizando el método get para el apellido')
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        print('Estamos utilizando el método set para el apellido')
        self._apellido = apellido

    @property
    def edad(self):
        print('Estamos utilizando el método get para la edad')
        return self._edad

    @edad.setter
    def apellido(self, edad):
        print('Estamos utilizando el método set para la edad')
        self._edad = edad

    def __del__(self):
        print(f'Persona2 : {self._nombre} {self._apellido} {self._edad}')

if __name__ == '__main__':
    persona1 = Persona2('Ariel', 'Bentacud', 41)
    print(persona1._nombre) #Llamamos al método getter
    persona1._nombre = 'Juan Pedro'
    print(persona1._nombre)
    print(persona1.mostrar_detalles())
    # Atributo read-only seía la edad porque no se puede modificar, no tiene el meodo set
    print(persona1.edad)

    # Tarea crear tres objetos más, utilizando los métodos getter and setter para modificar
    # y mostrar los cambios con el método mostar_detalles

    # Objeto numero 1
    persona2 = Persona2('Sebastian', 'Guzman', 19)
    persona2.nombre = 'Seba'
    persona2.apellido = 'Guz'
    persona2._edad = 20
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2._edad)
    print(persona2.mostrar_detalles())

    #Objeto numero 2
    persona3 = Persona2('Juan Cruz', 'Cogo', 19)
    persona3.nombre = 'Juan'
    persona3.apellido = 'Cogito'
    persona3._edad = 20
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3._edad)
    print(persona3.mostrar_detalles())

    # Objeto numero 3
    persona4 = Persona2('Felipe', 'Gonzalez', 18)
    persona4.nombre = 'Feli'
    persona4.apellido = 'Gonzalito'
    persona4._edad = 19
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4._edad)
    print(persona4.mostrar_detalles())

    print(__name__)
