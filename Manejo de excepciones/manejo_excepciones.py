from NumerosIdenticosException import NumerosIdenticosException
resultado = None # si pongo esta variable dentro del try, no puedo imprimirla fuera de ese bloque

a = 10
b = 10
# "raise" permite llamar una excepcion personalizada o cualquier excepción
try:
    if a == b:
        raise NumerosIdenticosException('Números Idénticos')
    resultado = a/b
except Exception as e:
    print(f'Ocurrió un error: {e}')
else:
    print('no se arrojó ninguna excepción')
finally: #lo que va aqui se ejecutará siempre, habiendo o no excepción
    print('Ejecución finalizada')

print(f'Resultado: {resultado}')
print('continuamos...')

