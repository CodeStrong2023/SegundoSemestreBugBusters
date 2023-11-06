
'''
Ejercicio 2: Agenda telefonica
Hacer un pragrama que simule una agenda de contactos. Crear un diccionario donde la clave
sea el nombre del usuario y el valor sea el telefono, el programa tendrá el siguiente menú de opciones:

1. Nuevo contacto
2. Borrar contacto
3. Ver contactos existentes
4 . Salir
'''



def menu():
    while(True):
            print("\t\tMENÚ:")
            print("""
        1. Nuevo contacto
        2. Borrar contacto
        3. Ver contactos existentes
        4. Salir
        """)
            opc = int(input("Elige una opción del menú: "))

            if opc == 1:
                nuevo_contacto()

            elif opc == 2:
                borrar_contacto()

            elif opc == 3:
                ver_contactos()

            elif opc == 4:
                print("Gracias por usar la agenda telefonica virtual")
                break


def nuevo_contacto():
    nombre = input("Ingrese el nombre del usuario: ")
    telefono = int(input("Ingrese el numero de telefono: "))
    if nombre not in agenda:
        agenda[nombre] = telefono
        print("Contacto agendado!")
        print(" ")
    else:
        print("Ese usuario ya está agendado")
        print(" ")


def borrar_contacto():
     nombre = input("Ingrese el nombre del contacto que desea borrar: ")
     if nombre in agenda:
         del(agenda[nombre])
         print(f"Se ha eliminado el contacto {nombre}")
     else:
        print("Ese contacto no está agendado.")

def ver_contactos():
    print("\t\tAGENDA: ")
    for key, value in agenda.items():
        print(key, value)
    print(" ")




# Ejecutamos el menu principal
agenda = {}
menu()