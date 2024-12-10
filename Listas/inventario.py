print('*** Sistema de Inventario ***')

inventario = []

numero_productos = int(input('Cuantos productos deseas agregar al inventario? '))

for indice  in range(numero_productos):
    print(f'Proporciona los valores del producto {indice + 1 }')
    nombre = input(f'Nombre:')
    precio = float(input('Precio: '))
    cantiadad = int(input('Cantidad: '))

    producto = { 'id': indice +1 ,
        'Nombre': nombre,
        'Precio': precio,
        'Cantidad': cantiadad
    }
 # Agregamos el nuevo producto al inventario
    inventario.append(producto)

# mostramos el inventario inicial
print(f'Inventario inicial: {inventario}')

# Buscar un producto por id
id_buscar = int(input('Ingresa el id del producto a buscar: '))
producto_encontrado = None
for producto in inventario:
    if  producto.get('id') == id_buscar:
        producto_encontrado = producto
        break

if producto_encontrado is not None:
    print('Informacion de producto encontrado: ')
    print(f'''Id: {producto_encontrado.get('id')}
    Nombre: {producto_encontrado.get('Nombre')}
    Precio: {producto_encontrado.get('Precio')}
    Cantidad: {producto_encontrado.get('Cantidad')}''')
else:
    print(f'produjcto con id {id_buscar} No encontraso')

# Mostrar el inventario detallado
print(f'\n--- Inventario detallado ---')
for producto in inventario:
    print(f'''Id: {producto.get('id')}
    Nombre: {producto_encontrado.get('Nombre')}
    Percio: {producto_encontrado.get('Precio')}
    Cantidad: {producto_encontrado.get('Cantidad')}
''')

