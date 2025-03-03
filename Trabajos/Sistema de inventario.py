from traceback import print_tb

print('*** Sistema de Inventario (Con funciones) ***')

# Inventario del almacen
inventario = [
    {'id':1, 'nombre':'Camisa', 'precio': 25.99, 'cantidad': 50},
    {'id':2, 'nombre':'Pantalones', 'precio': 39.99, 'cantidad': 30},
    {'id':3, 'nombre':'Zapatos', 'precio': 49.99, 'cantidad': 20},
]

# Funcion para mostar el inventario
def mostrar_inventario():
    print('\n--- Inventario del Almacén ---')

    for producto in inventario:
        print(f'Id: {producto.get('id')}, Nombre: {producto.get('nombre')}, '
              f'Precio: {producto.get('precio')}, Cantidad: {producto.get('cantidad')}')

def agregar_producto():
    print('--- Agregar Nuevo Producto ---')

    id = int(input('Id: '))
    nombre = input('Nombre: ')
    precio = float(input('Precio $: '))
    cantidad = int(input('Cantidad: '))
    nuevo_producto = {'id' : id, 'nombre':nombre,
                      'precio' : precio, 'cantidad': cantidad}
    inventario.append(nuevo_producto)
    print('Producto agregado al inventario')

def buscar_producto_por_id():
    pass

# Programa principal
if __name__ == '__main__':
    while True:
        print(f'''\n--- Menú ---
              1. Mostrar inventario
              2. Agregar nuevo inventario
              3. Buscar producto por id
              4. Salir''')
        opcion = int(input('Proporciona una opción (1-4): '))

        # Revisamos las opciones del menu
        if opcion == 1: # Mostrar el inventario
            mostrar_inventario()
        elif opcion == 2: # Agregar el inventario
            agregar_producto()
        elif opcion == 3: # Buscamos producto por id
            buscar_producto_por_id()
        elif opcion == 4: # Salir
            print('\nHasta luego!')
            break
        else: print('\nOpcion invalida, proporciona una opcion valida')



