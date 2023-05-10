class Persona: #tarea encapsular
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return f'Persona : {self.nombre} edad: {self.edad}'

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo): #debo poner los atributos de la clase padre}
        super().__init__(nombre, edad) #manda a llamar el iniciador de la clase padre con sus atributos
        self.sueldo = sueldo
    def __str__(self):
        return f'{super().__str__()} Sueldo: {self.sueldo}' #super() manda a llamar el str definido en la clase padre
                                                            # asi no escribo todo el codigo de nuevo

