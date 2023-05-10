from Orden import Orden
from Producto import Producto

producto1 = Producto('Camisa', 100.00)
producto2 = Producto('Pantalon', 150.00)
producto3 = Producto('Calcetines', 50.00)
producto4 = Producto('Blusa', 70.00)
productos1 = [producto1, producto2]
productos2 = [producto3, producto4]
orden1 = Orden(productos1)
orden2 = Orden(productos2)
print(orden1)
print(orden2)
print(f'Total orden2: {orden2.calcular_total()}')
print(orden1.calcular_total())
# probando agregar producto
orden1.agregar_producto(producto3)
orden1.agregar_producto(producto4)
print(orden1)
print(f'Total orden1: {orden1.calcular_total()}')