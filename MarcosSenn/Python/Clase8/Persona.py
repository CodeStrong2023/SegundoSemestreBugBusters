class Persona:
    def __init__(self, nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

persona1 = Persona('Marcos',"Senn", 29)

print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

#Modificar atributos

persona1.nombre = "Antonio"
persona1.edad = 21

print(persona1.nombre)
print(persona1.edad)