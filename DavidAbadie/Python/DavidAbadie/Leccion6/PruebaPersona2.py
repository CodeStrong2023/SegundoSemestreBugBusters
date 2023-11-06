from Persona2 import Persona2
print('Creación de objetos'.center(50, '-'))
if __name__ == "__main__":
    persona4 = Persona2("Lionel", "Messi", 35)
    persona4.mostrar_detalles()

    print(__name__)

print('Eliminación de objetos'.center(50, '-'))
del persona4