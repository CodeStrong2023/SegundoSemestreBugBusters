class Persona:  # Esta clase hereda de la clase Object
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    # Getters
    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    # Setters
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __str__(self):  # Override = Sobreescribir
        return f"Persona: [Nombre: {self.nombre}, Edad: {self.edad}]"


class Empleado(Persona):  # Esta clase es hija de la clase persona
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self._sueldo = sueldo

    # Getter
    @property
    def sueldo(self):
        return self._sueldo

    # Setter
    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    def __str__(self):
        return f"Empleado: [Sueldo: {self.sueldo}] {super().__str__()}"

empleado1 = Empleado("Nicolas", 21, 75000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)

print(" ")

empleado2 = Empleado("Pedro", 32, 178000)
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)

print(" ")

empleado2.nombre = "Natalia"
empleado2.edad = 35
empleado2.sueldo = 125000
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)
