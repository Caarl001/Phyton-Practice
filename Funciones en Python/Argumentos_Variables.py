from os.path import supports_unicode_filenames

print('*** Argumentos Variables ***')

def superheroe_superpoderes(superheroe, nombre, *args):
    print(f'Superheroe: {superheroe} - {nombre} - {args}')

    # Iteramos los superpoderes
    for superpoder in args:
        print(f'\tSuperpoder: {superpoder}')

# Llamar la funcion
superheroe_superpoderes('Spiderman' , 'Peter Parker' , 'Instinto Aracnido' , 'Telaraña')
superheroe_superpoderes('Iron Man' , 'Tony Stark' , 'Armadura' , 'Play Boy', 'Millonario')

# Es opcional enviar argumentos variables
superheroe_superpoderes('mi veciono', 'Luis Muñoz')
