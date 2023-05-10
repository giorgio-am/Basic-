vacaciones = False
diaDescanso = False

if vacaciones or diaDescanso:
    print("Puede asistir")
else:
    print("No puede asistir")

#Operador not

if not(vacaciones or diaDescanso):
    print("No Puede asistir")
else:
    print("Puede asistir")