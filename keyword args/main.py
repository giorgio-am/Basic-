# funcion q maneja una lista de terminos
def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')

listarTerminos(IDE= 'Integrated Development Enviroment')