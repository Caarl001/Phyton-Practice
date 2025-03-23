from catalogo_peliculas.servicio.catalogo_peliculas import CatalogoPeliculas
from dominio.pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas

opcion = None
while opcion != 4:
    try:

        print(' Opciones '.center(50,'-'))
        print('1. Agregar Película')
        print('2. Listar Películas')
        print('3. Eliminar  Catálogo Películas')
        print('4. Salir')
        opcion = int(input('Escribir tu opción (1-4): '))



        if opcion == 1:
            nombre_pelicula = input('Proporciona el nombre de la pelicula:')
            pelicula = Pelicula(nombre_pelicula)
            CatalogoPeliculas.agregar_peliculas()

        elif opcion == 2:
            CatalogoPeliculas.lista_peliculas()

        elif opcion == 3:
            CatalogoPeliculas.eliminar_peliculas()

    except Exception as e:
        print(f'Ocurrio un error {e}')
        opcion = None

else:
    print('Salinedo del programa....')