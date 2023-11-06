'''
Ejercicio 4: Calculadora de impuestos
crear una funcion para calcular el total de un pago incluyendo:
un impuesto aplicado (iva)
Formula: pago_total = pago_sin_impuesto + pago_sin impuesto * (impuesto/100)
proporcione el pago sin impuestos: 1000
proporcione el monto del impuesto: 21%
pago con impuesto: xxxxx
'''
# Creamos la función que calcula el total
def calcular_total_pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/ 100)
    return pago_total

#Ejecutamos la funcion
pago_sin_impuestos = float(input('Digite el pago sin impuestos: '))
impuesto = float(input('Digite el monto del impuesto a aplicar: '))
pago_con_impuestos = calcular_total_pago(pago_sin_impuestos, impuesto)
print(f'El pago con impuesto es: {pago_con_impuestos}')
