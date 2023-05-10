edad = int(input("Introduce tu edad: "))
veintes = edad >= 20 and edad < 30
print(veintes)
treintas = edad >= 30 and edad < 40
print(treintas)

if veintes or treintas :
    print('Dentro de los 20s o 30s')
    if veintes:
        print("Dentro de los 20s")
    elif treintas:
        print("Dentro de los 30s")
    else: #esta nunca se va a correr, pq si no esta entre los 20 ni 30 va a pasar para abajo
        print("Fuera de Rango")
else:
    print('No está dentro de los 20s ni 30s')
