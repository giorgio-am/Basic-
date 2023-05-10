class MiClase:
    # dejo una variable fuera de un metodo y queda como variable de clase
    variable_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
# Metodo estatico, se asocia con la clase en si misma
    @staticmethod
        #Contexto estatico es cuando solo he definido mi clase en memoria y no se puede acceder a los valores de objetos
        #Contexto dinamico es cuando ya puedo crear objetos
    def metodo_estatico():#no usa self, no accede a las variables de instancia (objetos)(self se usa con objetos)
        print(MiClase.variable_clase)
    #definiendo un metodo de clase

    @classmethod # el metodo de clase recibe o hace referencia a la clase misma como cls, en el estatico tengo q que hacer
    #referencia explicita a la clase
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self): #desde la instancia (self) en (contexto dinamico) puedo acceder a metodos de clase
                                        self.metodo_clase()
        self.metodo_estatico()


print(MiClase.variable_clase)
miClase = MiClase('Valor variable instancia')
print(miClase.variable_instancia)
# las variables de instancia son para cada objeto q se crea, las variables de clase son comunes para todos los objetos de la clase
miClase2 = MiClase('Meca')

print(miClase2.variable_instancia)

# crear variable de clase al vuelo
MiClase.variable_clase2 = 'Valor de clase 2'

print(miClase.variable_clase2)

# usando el metodo estatico
MiClase.metodo_estatico()
MiClase.metodo_clase()

miObjeto1 = MiClase('variable instancia')
miObjeto1.metodo_clase() # desde el contexto dinamico puedo acceder a los metodos y varaibles del contexto estatico
print(miObjeto1.variable_clase2)
# el miObjeto1 se creo con las variables de clase e instancia

miObjeto1.metodo_instancia()

