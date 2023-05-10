def calcular_total(pago_sin_impuesto, impuesto):
    return pago_sin_impuesto * (1 + impuesto/100)


pago_sin_impuesto = float(input("Ingrese pago sin impuestos: "))
impuesto = float(input("Ingrese % de impuesto: "))
pago_con_impuesto = calcular_total(pago_sin_impuesto, impuesto)
print(pago_con_impuesto)
