from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print('Creacion objeto cuadrado'.center(50,"-"))
cuadrado1 =  Cuadrado(3,'verde')
rectangulo = Rectangulo(2,2,'rojo')
print(cuadrado1)
cuadrado2 = Cuadrado(10, 'rojo')
print(cuadrado2)
cuadrado2.ancho = 3
print(cuadrado2)

#no se puede instancias una clase abstracta
# figura = FiguraGeometrica()
