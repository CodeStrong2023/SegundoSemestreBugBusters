
# Método con listas llamado PILAS

pila = [1,2,3]

# Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# Sacar elementos desde el final (retorna ese elemento)
elemento_borrado = pila.pop()
print(pila)
print(f"Sacamos el elemento {elemento_borrado}")
print(f"La pila ahora queda asi: {pila}")

# Método con listas llamado COLA

# Estructuras de datos de tipo fifo (first input / first output)

cola = ["Ariel", "Osvaldo", "Liliana", "Natalia"]

# Agregamos elementos al final de la cola
cola.append("Pilar")
cola.append("Jose")
print(cola)

# Sacamos los elementos de la cola

se_retira = cola.pop(0)
print(f"Atendido: {se_retira}")
print(cola)

se_retira = cola.pop(0)
print(f"Atendido: {se_retira}")
print(cola)

se_retira = cola.pop(0)
print(f"Atendido: {se_retira}")
print(cola)

se_retira = cola.pop(0)
print(f"Atendido: {se_retira}")
print(cola)

se_retira = cola.pop(0)
print(f"Atendido: {se_retira}")
print(cola)

se_retira = cola.pop(0)
print(f"Atendido: {se_retira}")
print(cola)