# Ejercicio 2= Calculadora de impuestos 
# Crear una función para calcular el total de un pago incluyendo un impuesto aplicado. (IVA)
# Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
# Proporcione el pago sin impuesto: 1000
# Proporcione el monto del impuesto: 21%
# Pago con impuesto: xxxxx

# Creamos la función que calcula el total del pago incluyendo el impuesto
def calcular_total_pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

# Ejecutamos funciones
pago_sin_impuesto = float(input("Digite el pago sin el impuesto: "))
impuesto = float(input("Digite el porcentaje del impuesto: "))
pago_total = calcular_total_pago(pago_sin_impuesto, impuesto)
print(f'El pago total con impuesto incluido es de: {pago_total}$')