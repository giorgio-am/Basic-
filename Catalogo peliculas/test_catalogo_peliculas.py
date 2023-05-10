from dominio.Pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas as cp

opcion = None
while opcion != 4:
    try:
        print('Opciones: ')
        print('1. Agregar Pelicula')
        print('2. Listar Peliculas')
        print('3. Eliminar Catalogo de Peliculas')
        print('4. Salir')
        opcion = int(input('Escribe tu opcion (1-4): '))

        if opcion == 1:
            nombre_pelicula = input('Proporciona el nombre de la Pelicula: ') #entrego un nombre
            pelicula = Pelicula(nombre_pelicula) #se crea un objeto pelicula con ese nombre
            cp.agregar_pelicula(pelicula) #llama al metodo agregar pelicula en catalogo_peliculas, haicnedo un append al archivo
        elif opcion == 2:
            cp.listar_peliculas() # con ctl + click voy a donde esta definida la funcion
        elif opcion == 3:
            cp.eliminar_peliculas()


    except Exception as e:
        print(f'Ocurrió un error: {e}')
        opcion = None
else:
    print('Salimos del programa'.center(50, '-'))