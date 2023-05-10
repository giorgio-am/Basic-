# bool contiene valores true o false
# Tipos numericos, Falso para 0 y True para los demás

valor = 0.0
resultado = bool(valor)
print(resultado)

valor = 15.0
resultado = bool(valor)
print(resultado)

# tipo string (str), Falso para cadenas vacías, cualquier valor dinstinto de vacío True

valor = ''
resultado = bool(valor)
print(resultado)

valor = 'asd'
resultado = bool(valor)
print(resultado)

# Tipo colecciones, False para colecciones vacías, True para las demás
#lista: []
valor = []
resultado = bool(valor)
print(resultado)

valor = [2,3,4]
resultado = bool(valor)
print(resultado)
#tupla ()
valor = ()
resultado = bool(valor)
print(resultado)

valor = (2,3,4)
resultado = bool(valor)
print(resultado)

#Diccionario {}
valor = {}
resultado = bool(valor)
print(resultado)

valor = {'nombre':'Juan', 'apellido':'perez'}
resultado = bool(valor)
print(resultado)

a = 'asd'
bool(a==0)
print(bool(a=='asd'))
