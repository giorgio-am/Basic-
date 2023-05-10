# operador + puede comportarse de formas distintas dependiendo del tipo de datos con los q trabaja

a = 2
b = 3
print(a+b)
# se usó para sumar

a = 'Hola'
b = 'Mundo'

print(a+b) #aqui devuelve una concatenacion

a = [1,2,3]
b = [6,7,8]
print(a+b) # aqui entrega una lista con los elementos de las 2 listas
# en una clase, si quiero sobrecargar un operador debo definirlo modificando su metodo
# por ejemplo para sobrecargar el operador + debo modificar el metodo __add__(self,other)

