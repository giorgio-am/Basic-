from Persona import *
persona1 = Persona('juan', 28) # en el archivo persona definir un metodo __str__() para mostrar aqui otra impresion
#y que no muestre la posicion en memoria
print(persona1) #imprime lo q defini en __str__ en la clase padre

empleado1 = Empleado('Karla', 30, 5000)
print(empleado1) # no muestra el sueldo por que está definido en la clase hija, y ahi no he redefinido __str__()
# debo redifinir __str__ en la clase hija empleado agregando el sueldo, ya que solo heredó nombre y edad

