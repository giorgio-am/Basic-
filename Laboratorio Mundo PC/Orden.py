from Teclado import Teclado
from Raton import Raton
from Monitor import Monitor
from Computador import Computador


class Orden:
    contador_orden = 0

    def __init__(self, computadores):
        Orden.contador_orden += 1
        self._id_orden = Orden.contador_orden
        self._computadores = computadores

    def agregar_computador(self, computador):
        self._computadores.append(computador)

    # #def __str__(self):
    #     return f'''
    # Id Orden: {self._id_orden}
    # Detalle: {self._computadores} si lo hago asi, se imprimirá la direccion de los objetos de la lista, debo
    # definir una variable que vaya almacenando como string cada uno de los elementos de la lista

    def __str__(self):
        computadores_str = '' #la inicio vacía
        for computador in self._computadores: #debe ser esa variable, porque ahi es donde voy guardando los append
            computadores_str += computador.__str__()

        return f'''
        Id Orden: {self._id_orden}
        Computadores: {computadores_str}
        '''


teclado1 = Teclado('usb', 'log')
raton1 = Raton('usb', 'hp')
monitor1 = Monitor('sony', 24)
computador1 = Computador('Gamer', monitor1, teclado1, raton1)
computador2 = Computador('asd', monitor1, teclado1, raton1)
computadoreslista = [computador1]
orden1 = Orden(computadoreslista)
orden1.agregar_computador(computador2)
orden1.agregar_computador(computador1)
orden1.agregar_computador(computador1)

print(orden1)



