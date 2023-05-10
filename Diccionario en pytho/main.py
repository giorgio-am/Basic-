# Datos ordenados con una "key" asociada a un "valor" (como una tabla de 2 columnas key|valor
diccionario = {
    "IDE":"Integrated Development Environment","OOP":"Object Oriented Programming","DBMS":"Database Management System"
}
print(diccionario)
print(len(diccionario)) #largo

#diccionario no tiene indices
#acceder a un elemento, proporcionar key

print(diccionario["IDE"])
# otra forma

print(diccionario.get("OOP"))
# modificar elemento del diccionario
diccionario["IDE"] = "cualquier cosa"
print(diccionario)

#recorrer los elementos
for termino in diccionario:
    print(termino)

#recorrer por elemento y valor

for termino, valor in diccionario.items():
    print(f"{termino}", f":{valor}")
#recuperar solo llaves

for termino in diccionario.keys():
    print(termino)
#comprobar existencia de algun elemento con True o False

print("IDE" in diccionario)

#agregar un elemento
diccionario["PK"] = "primary key"
print(diccionario)

#remover un elemento
diccionario.pop("PK")
print(diccionario)
#limpiar
diccionario.clear()
print(diccionario)
#eliminar diccionario
del diccionario
print(diccionario)