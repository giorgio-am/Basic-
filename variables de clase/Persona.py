class Persona:
    contador_personas = 0

    # posible mejora crear un metodo de clase para generar el siguiente valor
    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas #puedo quitar lo q puse en init, accediendo ahora de forma indirecta

    def __init__(self, nombre, edad): # self se refiere al objeto, al crear un objeto parte el init, o sea al init le entra el self, q es el objeto
        #Persona.contador_personas += 1 reemplazado por el metodo de clase
        #self.id_persona = Persona.contador_personas#
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona: {self.id_persona} Nombre: {self.nombre} Edad: {self.edad}'

persona1 = Persona("juan", 28)
print(persona1)

persona2 = Persona('karla', 30)
print(persona2)
personanueva = Persona("arturo", 5)
print(f'Numero de personas: {Persona.contador_personas}')

# el problema es q podria llamar al metodo sin crear un objeto y aumentaria el numero
#Persona.generar_siguiente_valor()#