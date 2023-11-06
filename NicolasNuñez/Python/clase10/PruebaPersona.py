from Persona import Persona
print('Creación de objetos'.center(50, '-'))
if __name__ == "__main__":
    persona4 = Persona("Lionel", "Messi", 35)
    persona4.mostrar_detalles()

    print(__name__)

print('Eliminación de objetos'.center(50, '-'))
del persona4