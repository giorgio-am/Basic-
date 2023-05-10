from Persona import Persona

print('Creacion de objetos'.center(50,'-')) #con center centro el mensaje, le doy un largo de 50 caracteres, y
#la diferencia entre los caracteres del mensaje y 50 se rellenan con -
persona1 = Persona('Karla', 'Gomez', 30)
persona1.mostrar_detalle()

print('Eliminacion de objetos'.center(50,'-')) #en la definicion de la clase (Archivo Persona.py
                                               #debo definir un metodo destructor para eliminar objetos

del persona1 # es raro hacer esto directamente, suele usarse el "recolector de basura"