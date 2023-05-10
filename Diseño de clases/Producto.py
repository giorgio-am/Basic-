class Producto:
    contador_productos = 0

    def __init__(self, nombre, precio): #estoy en el contexto dinamico, entonces para acceder a la variable
        # de clase debo poner el nombre antes Persona
        Producto.contador_productos += 1
        self._id_producto = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio
        #deberia encapsular #t#odo con get y set
    @property
    def precio(self):
        return self._precio

    def __str__(self):
        return f'Id producto: {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio}'

if __name__ == '__main__':
#para q las pruebas se ejecuten solo aqui
    producto1 = Producto('Camisa', 100.00)
    print(producto1)
    producto2 = Producto('Pantalon', 150.00)
    print(producto2)

