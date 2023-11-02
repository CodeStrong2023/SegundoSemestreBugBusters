'''
Ejercicio 4: Calculadora de Impuestos
Crear una función para calcular el total de un pago incluyendo un impuesto aplicado (IVA).
Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
Proporcione el pago sin impuesto: 1000
Proporcione el monto del impuesto: 21%
Pago con impuesto: xxxxx
'''

# Creamos la funcion que calcular el total del pago incluyendo el impuesto
def pago_con_iva(pago_sin_inpuesto, impuesto):
    pago_total = pago_sin_inpuesto + (pago_sin_inpuesto * (impuesto/100))
    return pago_total

# Ejercutamos la función
pago_sin_impuesto = float(input("Ingrese el valor del pago sin impuesto: "))
pago_total = pago_con_iva(pago_sin_impuesto,35)
print(f"El pago total incluyendo IVA es de: ${pago_total}")