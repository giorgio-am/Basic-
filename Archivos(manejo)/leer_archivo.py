archivo = open('prueba.txt', 'r', encoding='utf8')
# print(archivo.read())
# print(archivo.read(5)) #asi leo los primeros 5
# print(archivo.read(3)) #los 3 primeros de los restantes
#
# print(archivo.readline())
# print(archivo.readline())


# iterar el archivo por linea
# for linea in archivo:
#     print(linea)

#print(archivo.readlines()) # entrega una lista con las lineas (formato lista)

# cada linea de manera individual
# print(archivo.readlines()[0]) # indice 0, primera linea

# a - append, aneza informacion

archivo2 = open('copia.txt', 'a', encoding='utf8')
archivo2.write(archivo.read())
archivo.close()
archivo2.close()


