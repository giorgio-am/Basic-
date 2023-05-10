from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado


class Computador:
    contador_computadores = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computador.contador_computadores += 1
        self._id_monitor = Computador.contador_computadores
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'''
        {self._nombre}: {self._id_monitor}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}
        '''



