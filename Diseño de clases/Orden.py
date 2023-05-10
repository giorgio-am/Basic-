from Producto import Producto


class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes +=1
        self._id_orden = Orden.contador_ordenes
        self._productos = list(productos) #si no es lista tira error

    # metodo para agregar un producto a una orden posteriormente, despues de la lista inicial
    def agregar_producto(self, producto):
        self._productos.append(producto)
    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio #sin el _ pq defini el get en property
        return total
    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__() + '\n'
        return f'Orden: {self._id_orden}\nProductos:\n{productos_str}'

if __name__ == '__main__':
    producto1 = Producto('Camisa', 100.00)
    producto2 = Producto('Pantalon', 150.00)
    productos1 = [producto1, producto2] #defino una lista
    orden1 = Orden(productos1)#debo entregarle una lista de productos
    orden2 = Orden(productos1)
    print(orden1)
    print(Orden.calcular_total(orden1))
    #directamente desde el objeto
    print(orden1.calcular_total())
    print(orden2)