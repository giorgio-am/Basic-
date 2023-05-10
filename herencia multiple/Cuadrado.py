from Color import Color
from FiguraGeometrica import FiguraGeometrica


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color): #no pongo ancho y alto pq cuadrado es lado por lado
        # super().__init__(self) podria confundirse con que clase inicializar primero
        FiguraGeometrica.__init__(self, lado, lado)
        # en este paso defino q el ancho y alto es igual en el cuadrado
        # cuando inicializo cuadrado con "lado", este "lado" se guarda en la posicion de ancho y alto de FiguraGeometrica
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)} Area: {Cuadrado.calcular_area(self)}'

