#calculo total de un pago con IVA aplicado

def totalPago(importeSinImpuesto):
    impuesto = 21
    total = importeSinImpuesto + importeSinImpuesto * (impuesto/100)
    print(total)

totalPago(1000)
