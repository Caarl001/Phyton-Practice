
print('*** Playlist de Canciones ***')

# Creamos la lista vacia

lista_reproduccion = []

numero_canciones = int(input('Cuantas canciones deseas agregar? '))

# Iteramos cada elemento de la lista para agregar un nuevo elemento
for indice in range(numero_canciones):
    cancion = input(f'Proporciona la cancion {indice + 1}: ')
    lista_reproduccion.append(cancion)

# Empexamos a agregar canciones
lista_reproduccion.append('Hotel California - Eagles')
lista_reproduccion.append('Staying Alive - Bee Gees')
lista_reproduccion.append('Dream on - Aerosmith')

# Ordenar la lista en orden alfabetico.  sort
# Para ordenar de manera decendente . reverse=True
lista_reproduccion.sort(reverse=True)

# Mostrar la lista de canciones
print(f'\n Lista de reproducion en orden alfabetico: ')
print(lista_reproduccion)

# Mostar la lista iterando sus elementos
print('\n')
for cancion in lista_reproduccion:
    print(f' - {cancion}')