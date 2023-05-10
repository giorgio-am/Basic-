# funcion para agregar terminos a un diccionario
diccionario = {
    "IDE":"Integrated Development Environment","OOP":"Object Oriented Programming","DBMS":"Database Management System"
}

print(diccionario)
#** le entrego mas de un argumento variable
def agregarTerminos(**terminos):

    for llave, valor in terminos.items():
        diccionario[llave] = [valor]

agregarTerminos(ASD="asdasd",loro="jaime")
print(diccionario)

