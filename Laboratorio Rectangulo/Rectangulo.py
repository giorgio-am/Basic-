class Rectangulo:
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base
    def calcularArea(self):
        return self.base * self.altura
base = int(input("Ingresar base: "))
altura = int(input("Ingresar altura: "))
# Es necesario crear una variable para que haga referencia al objeto creado
rectangulo1 = Rectangulo(base, altura)
print(rectangulo1.calcularArea())