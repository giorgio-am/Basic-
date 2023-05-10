# Algoritmo para derterminar si un número es par o impar
a = int(input("Escribe un valor numérico: "))
if a % 2 ==0: #tiene q ser con == para que tenga valor true o false y pueda seguir el if
    print(f"El valor de {a} es un número par")
else:
     print(f"El valor de {a} es un número impar")