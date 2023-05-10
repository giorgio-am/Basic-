valor = int(input("Escribe el valor: "))
valorMinimo = 0
valorMaximo = 5
dentroRango = valor <= valorMaximo and valor >= valorMinimo
if dentroRango:
    print(f"El valor está dentro del Rango")
else:
    print(f"El valor no está dentro del Rango")