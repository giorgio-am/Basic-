# para convertir a abstracta uso ABC = Abstract Base Class y el decorador abstractmethod y hacer q FiguraGeometrica
# herede desde ABC
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        #validaciones (es necesario tambien ponerlas en los metodos)
        #if 0 < ancho < 10:
        if self._validar_valor(ancho): #va sin self dentro, pq ya tiene self.
            self._ancho = ancho
        else:
            self._ancho = 0
        #if 0 < alto <10:
        if self._validar_valor(alto):
            self._alto = alto #sin encapsulamiento para q sea mas corto
        else:
            self._alto = 0
    @property
    def ancho(self):
        return self._ancho
    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto
    @alto.setter
    def alto(self, alto):
        self._alto = alto
# aqui pongo el metodo abstracto
    @abstractmethod #estoy diciendo q este es un metodo abstracto, es decir, que en las clases hijas se debe definir
    #este metodo. Al tener solo "pass" el metodo en si no hace nada, pero obliga a hacer un def calcular_area
    # en la clase hija
    def calcular_area(self):
        pass
    def __str__(self):
        return f'FiguraGeometrica [Ancho: {self._ancho}] [Alto: {self._alto}'

    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False
