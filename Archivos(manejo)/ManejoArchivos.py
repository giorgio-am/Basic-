class ManejoArchivos: #context manager
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        print('obtenemos el recurso'.center(50,'-'))
        self.nombre = open(self.nombre, 'r', encoding='utf8')
        return self.nombre

    def __exit__(self, tipo_excepcion, valor_excepcion, traza_error):
        print('cerramos el recurso'.center(50, '-'))
        if self.nombre: #si self.nombre esta apuntando a algun objeto, se va a devolver True, y ejecutara la siguiente linea
            self.nombre.close()
