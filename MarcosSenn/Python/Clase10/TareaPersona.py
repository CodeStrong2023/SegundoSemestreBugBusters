class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


    def get_nombre(self):
        return self.nombre


    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre


    def get_apellido(self):
        return self.apellido


    def set_apellido(self, nuevo_apellido):
        self.apellido = nuevo_apellido


    def get_edad(self):
        return self.edad


    def set_edad(self, nueva_edad):
        self.edad = nueva_edad

    def mostrar_detalles(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad}")


persona = Persona("Juan", "Perez", 30)


print("Detalles iniciales:")
persona.mostrar_detalles()


persona.set_nombre("Pedro")
persona.set_apellido("Gomez")
persona.set_edad(35)


print("\nDetalles después de la modificación:")
persona.mostrar_detalles()
