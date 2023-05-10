class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return f'Color: {self.color} Ruedas: {self.ruedas}'

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
    def __str__(self):
        return f'{super().__str__()} Velocidad: {self.velocidad}'

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def __str__(self): #string va solo con self, en el init se pusieron los atributos
        return f'{super().__str__()} Tipo: {self.tipo}'

vehiculo = Vehiculo("rojo", 4)
print(vehiculo)

coche = Coche("rojo", 4, 200)
print(coche)

bicicleta = Bicicleta("blanca", 2, "urbana")
print(bicicleta)