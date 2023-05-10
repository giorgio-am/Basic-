def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
#Definiendo la lista :(igual puede pasarse directamente desde la funcion
nombres = ["Juan", "Karla", "Guillermo"]

desplegarNombres(nombres)
desplegarNombres("Carlos") #itera las letras del nombre Carlos, interpreta como q es un string
#Poniendo dos cosas entre parentesis para q sea tupla
desplegarNombres(nombres)