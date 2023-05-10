class Persona:

    def __init__(self, nombre, apellido, edad):
        #atributo con _ o __ son atributos encapsulados (no deberia tener acceso desde fuera de la clase
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad
    #definiendo metodo para get (recuperar) el valor del atributo el primer metodo es por defecto get
    @property #hace que se puedo acceder a este metodo como si fuera un atributo (persona1.nombre)
    def nombre(self):
        return self._nombre
    #para modificar el atributo
    @nombre.setter # debo ponerle el argumento nombre, q va a ser el q va a reemplazarse (modificarse)
    # Si quito el metodo set, la variable no puede ser modificada y queda como de "solo lectura"
    def nombre(self, nombre):
        self._nombre = nombre
    #definiendo un metodo para la clase
    def mostrar_detalle(self):
        print(f'Persona: {self._nombre}')
    def __del__(self): #metodo destructor
        print(f'Persona: {self._nombre}')

if __name__ == '__main__': #esto hace que si importo este modulo desde otro archivo, lo siguiente no se ejecute ahi, solo puedo ejecutarlo desde aqui
    persona1 = Persona("juan","perez",28)
    print(persona1.nombre)
    Persona.mostrar_detalle(persona1)
    persona1.nombre = "meca"
    print(persona1.nombre)

#para conocer el nombre del modulo q se esta ejecutando
    print(__name__)
# si devuelve __main__ es pq el modulo se ejecuta desde el mismo archivo


