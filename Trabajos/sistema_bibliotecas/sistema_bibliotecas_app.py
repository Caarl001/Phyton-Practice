from Trabajos.sistema_bibliotecas.biblioteca import Biblioteca
from Trabajos.sistema_bibliotecas.libro import Libro

bibliotecaNacional = Biblioteca('Biblioteca Nacional')
print(f' *** Bienvenido a la {bibliotecaNacional.nombre} *** ')

# Definir libros
libro1 = Libro('Cien años de soledad', 'Gabriel Garcia Marquez', 'Ficción')
libro2 = Libro('Don Quijote de la Mancha','Miguel de Cervantes','Comedia')
libro3 = Libro('El amor en los tiempos de colera','Gabriel Castellón','Ficción')

# Agregar los libros a la biblioteca
bibliotecaNacional.agregar_libro(libro1)
bibliotecaNacional.agregar_libro(libro2)
bibliotecaNacional.agregar_libro(libro3)

# Buscar libro por autor
autor = 'Gabriel Garcia Marquez'
print(f'\nLibros de {autor}')
bibliotecaNacional.buscar_libro_por_autor(autor)

# Buscar libros por el genero
genero = 'Comedia'
print(f'\nlibros de { genero}')
bibliotecaNacional.buscar_libros_por_genero(genero)
bibliotecaNacional.mostrar_todo_los_libros()
