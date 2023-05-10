def funcion(numero):
    if numero >= 1:
        print(numero)
        funcion(numero - 1)
funcion(5)
# me salio exactamente igual a la del profe