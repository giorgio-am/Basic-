# definir una tupla con parentesis, lista con corchetes (solo al declarar)

frutas = ("naranja","platano","guayaba")
print(frutas)

print(len(frutas))

#acceder a un elemento con corchetes
print(frutas[0])

print(frutas[-1])

#acceder a un rango
print(frutas[0:1])

# tupla debe tener una coma al final si tiene solo un valor
#recorrer tupla
for fruta in frutas:
    print(fruta)
# modificar el salto de linea al final por cualquier caracter

for fruta in frutas:
    print(fruta, end="/")
# la tupla no puede modificarse
# PARA MODIFICAR LA TUPLA PRIMERO CONVERTIRLA EN LISTA, LUEGO MODIFICARLA Y DESPUES VOLVER A TRANSFORMARLA EN TUPLA
frutaLista = list(frutas)
frutaLista[0] = "manzana"
frutas = tuple(frutaLista)
print('\n',frutas)
#eliminar tupla
del(frutas)