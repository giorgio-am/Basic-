class Persona:
    #iniciador init agregar atributos e inicializar, agregar objetos (__ double underscore o dunder)
    def __init__(self, nombre, apellido, edad, *valores, **terminos): # atributos de instancia
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos
    #definiendo un metodo para la clase
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre}, {self.valores}, {self.terminos}') #como estoy dentro de la definicion de la clase uso self, si estoy fuera uso Persona.nombre




persona1 = Persona("juan", "perez", 28, "asdasdasd",2,3, M = "Manzana")
persona1.mostrar_detalle() # llama a la funcion q cree dentro de la clase (metodo)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona('Karla','Gomez',30)
print(f'Persona 2: {persona2.nombre}, {persona2.apellido}, {persona2.edad}')

#puede tener atributos y metodos

#modificar un atributo
persona1.nombre = "ramiro"
persona2.edad = 40
print(f'Persona 2: {persona2.nombre}, {persona2.apellido}, {persona2.edad}')

#crear un nuevo atributo para un objeto (no a toda la clase)
persona1.telefono = "12345"
print(f'Persona 1: {persona1.nombre}, {persona1.apellido}, {persona1.edad}, {persona1.telefono}')
print(f'Persona 1: {persona1.nombre}, {persona1.apellido}, {persona1.edad}, {persona1.telefono}, {persona1.valores}, {persona1.telefono}')