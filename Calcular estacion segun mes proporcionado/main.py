mes = int(input("Proporciona el mes del año (1-12): "))
estacion = None #declaracion anticipada
if mes == 1 or mes == 2 or mes == 3:
    estacion = "verano"
elif mes == 4 or mes == 5 or mes == 6:
    estacion = "otoño"
elif mes == 7 or mes == 8 or mes == 9:
    estacion = "invierno"
elif mes == 10 or mes == 11 or mes == 12:
    estacion = "Primavera"
else:
    print("Mes no válido")
if estacion:
    print(f"En el mes proporcionado es: {estacion}")
