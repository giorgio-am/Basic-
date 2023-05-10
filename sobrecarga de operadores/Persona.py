class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def __add__(self, other):
        return self.nombre + other.nombre
                                    #other es el otro objeto,
                              # ejemplo obj1 + obj2, el objeto inicial es obj1 y ahi se manda a llamar la funcion __add__
                            # sería como hacer: obj1.__add__(obj2)

persona1 = Persona('juan')

persona2 = Persona('carlos')



print(persona1 + persona2)

print(abs(3-5))
abs() #valor absoluto
