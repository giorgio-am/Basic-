numero = float(input("Proporciona un valor entre 0 y 10: "))
calificacion = None

if 9 <= numero <= 10:
    calificacion = "A"
elif 8 <= numero < 9:
    calificacion = "B"
elif 7 <= numero < 8:
    calificacion = "C"
elif 6 <= numero < 7:
    calificacion = "D"
elif 0 <= numero < 6:
    calificacion = "F"
else:
    calificacion = "Valor desconocido"

print(calificacion)