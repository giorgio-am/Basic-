from DispositivoEntrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contador_teclados = 0
    def __init__(self, tipoEntrada, marca):
        Teclado.contador_teclados += 1
        self._id_teclado = Teclado.contador_teclados
        super().__init__(tipoEntrada, marca)

    def __str__(self):
        return f'Id: {self._id_teclado}, {DispositivoEntrada.__str__(self)}'

