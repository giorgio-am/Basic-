# profundizando tipo str

#help(str.capitalize)

mensaje1 = 'hola mundo'
mensaje2 = mensaje1.capitalize() #no se modifica el str original, queda igual, se crea una distinta y modificada

print(f'mensaje1: {mensaje1}, id: {hex(id(mensaje1))}')
print(f'mensaje2: {mensaje2}, id: {hex(id(mensaje2))}')



