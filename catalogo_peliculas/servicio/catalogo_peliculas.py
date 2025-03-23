import os
class CatalogoPeliculas:

    ruta_archivo = 'peliculas.txt'

    @classmethod
    def agregar_peliculas(cls, pelicula):
        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write((f'{pelicula._nombre}\n'))

    @classmethod
    def lista_peliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf8') as archivo:
            print(' Catalogo de peliculas '.center(50,'-'))
            print(archivo.read())

    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f'Se elimino la wea: {cls.ruta_archivo}')
