'''
Ejercicio 6: Mostrar una frase sin espacios y contar su longitud.
Hacer un programa donde el usuario ingrese una frase, se le devolverá la misma frase
pero sin espacios en blanco y además, un contador de cuantos caracteres tiene la frase
(sin contar los espacios en blanco)
'''

frase = input("Ingrese una frase: ")

frase_final = ""

for i in frase:
    if i == " ":
        continue
    else:
        frase_final += i

print(f"Frase = {frase}")
print(f"Frase final = {frase_final}")
print(f"N° de caracteres = {len(frase_final)}")
