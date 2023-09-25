'''
Ejercicio 3: Tabla de multiplicar
Hacer un programa que pida un numero por teclado y guarde en una lista
su tabla de multiplicar hasta el 10. Por ejemplo: si digita el 5, la lista
tendrá: 5,10,15,20,25,30,35,40,45,50
'''

num = int((input("Ingrese un numero para conocer su tabla de multiplicacion: ")))
tabla = list()

for i in range(1,11):
    multiplicacion = num * i
    tabla.append(multiplicacion)

print(f"La tabla del {num} es: ")
print(tabla)