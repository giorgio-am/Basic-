def sumarTodo(*args) -> float:
    i = 0
    suma = 0
    while i < len(args):
        suma = suma + args[i]
        i += 1
    print(suma)

sumarTodo(1,2,8)

# forma del profesor

def sumar_valores(*args):
    resultado = 0
    for valor in args:
        resultado += valor
    return resultado

print(sumar_valores(3,2,1))

#multiplicar todo

def multiplicar(*factores):
    multiplicacion = 1
    for factor in factores:
        multiplicacion *= factor

    print(multiplicacion)

multiplicar(1,2,3)