#factorial
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero -1)
resultado = factorial(2)
print(resultado)

# si ingreso 5, el programa entiende que es distinto de 1 asi que la funcion devuelve 5 * factorial(4)
# y factorial(4) hace lo mismo devolviendo 4 factorial (3), quedando la expresion inicial como:
# 5 * 4 * facotrial(3)
#despuies factorial(3) es 3 * factorial(2)
# 5 * 4 * 3 * factorial(2)
#y factorial(2) es 2 * factorial(1) y factorial(1) = 1 (linea 3)
# quedando asi la expresion 5*4*3*2*1
