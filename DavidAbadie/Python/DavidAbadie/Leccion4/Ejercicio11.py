# Ejercicio 11: Agenda telefonica
# Hacer un programa que simule una agenda de contactos. Crear un
# diccionario donde la clave sea el nombre del usuario y el valor
# sea el telefono, el programa tendrá el siguiente menú de opciones.
#   1. Nuevo contacto
#   2. Borrar contacto
#   3. Ver contactos existentes
#   4. Salir


agenda = {}
while True:
    print('\t** Menu **')
    print('1. Nuevo contacto')
    print('2. Borrar contacto')
    print('3. Ver contactos existentes')
    print('4. Salir')
    opcion = int(input('Seleccione una opcion: '))
    if opcion == 1:
        nombre = input('Nombre del contacto: ')
        telefono = input('Número de teléfono: ')
        if nombre not in agenda:
            agenda[nombre] = telefono
            print('Contacto añadido')
        else:
            print('Ese contacto ya existe')
    elif opcion == 2:
        nombre = input('Nombre del contacto: ')
        if nombre in agenda:
            del (agenda[nombre])
            print('Contacto borrado')
        else:
            print('El contacto no existe')
    elif opcion == 3:
        print('AGENDA DE CONTACTOS')
        for clave, valor in agenda.items():
            print(f'Nombre: {clave}\n Telefóno: {valor}\n')
    elif opcion == 4:
        print('Saliendo de la agenda de contactos')
        break
    else:
        print('Opcion incorrecta')
