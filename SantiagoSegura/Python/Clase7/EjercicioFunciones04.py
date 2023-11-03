# Ejercicio 4: Calculadora de Impuestos
# Crear una funcion para crear el total de un pago incluyendo
# un inpuesto aplicado. (IVA)
# Formula: pago_total = pago sin impuesto + pago sin inpuesto * (inpuesto/100)
# Proporcione el pago sin impuesto: 1000
# Proporcione el monto del impuesto: 21%
# Pago con impuesto: xxxxxx


def calcular_pago_con_impuesto(pago_sin_impuesto, porcentaje_impuesto):
    pago_total = pago_sin_impuesto + (pago_sin_impuesto * (porcentaje_impuesto / 100))
    return pago_total


pago_sin_impuesto = float(input("Proporcione el pago sin impuesto: "))
porcentaje_impuesto = float(input("Proporcione el monto del impuesto (en porcentaje): "))

# Calcular
pago_con_impuesto = calcular_pago_con_impuesto(pago_sin_impuesto, porcentaje_impuesto)

# resultado
print(f"Pago con impuesto: {pago_con_impuesto}")
