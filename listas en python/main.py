nombres = ["Juan","Karla","Ricardo","Maria"]

print(nombres)

# indice

print(nombres[1])
print(nombres[-3])

# imprimir rango

print(nombres[0:2]) # sin incluir el 2

# ir del inicio al indice sin incluirlo
print(nombres[:3])
# del indicado hasta el final
print(nombres[1:])
# cambiar un valor de la lista
nombres[3] = "CACA"

print(nombres)

for nombre in nombres: #nombre almacena cada indice de la lista nombre
    print(nombre)
#preguntar largo

print(len(nombres))
#agregar elemento funcion append poner . despues de la lista ejemplo: nombres.funcion
nombres.append("Giorgio")
print(nombres)
#insertar un elemento en un indice en especifico
nombres.insert(1,"Fofo")
print(nombres)
#remover un elemento
nombres.remove("CACA")
print(nombres)
#remover ultimo valor
nombres.pop()
print(nombres)
# remover un indice indicado
nombres.pop(0)  # tambien sirve del nombres[0]
print(nombres)
del nombres[1]
print(nombres)
# eliminar todos los elementos de la lista
nombres.clear()
print(nombres)
# borrar la lista por completo
del nombres
print(nombres)
