#contactos

contactos = []
def agregar(name,number):
    contactos.append({"nombre":name, "numero":number
                      });
def borrar(name):
    for i in contactos:
        if i["nombre"] == name:
            contactos.remove(i)

def mostrar():
    print(contactos)

def agenda():
    while True:
        opcion = int(input("1 para agregar, 2 para eliminar 3 para ver 4 para salir"))

        if opcion == 1:
            name = str(input("ingrese un nombre"))
            number = int(input("ingrese un numero"))
            agregar(name, number)
        elif opcion == 2:
            name = input("ingrese un nombre")
            borrar(name)
        elif opcion == 3:
            mostrar()
        elif opcion==4:
            print("Programa finalizado aguante voka")
            break


agenda()