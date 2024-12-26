

print('\n==============================================')
print('*** Sistema de Inventario (Con funciones) ***')
print('==============================================')
print('1.- Mostrar inventario')
print('2.- Agregar nuevo producto')
print('3.- Buscar producto por ID')
print('4.- Salir')
print('========================================')
opcion = int(input('Ingrese una opcion: '))

# Inventario del almacen
muestras =[
    {'id': 1, 'nombre':'Camisa','precio': 25.000, 'cantiadad': 50},
    {'id': 2, 'nombre':'Pantalones','precio': 35.500, 'cantiadad': 30},
    {'id': 3, 'nombre':'Zapatos','precio': 60.000, 'cantiadad': 20}
]

# Funcion para mostrar inventatio

def mostrar_inventario():
    print('--- Inventario del Almacén ---')
    for producto in muestras:
        print(f'id: {producto.get('id')}, Nombre: {producto.get('nombre')}, '
              f'Precio: ${producto.get('precio')}, cantiadad: {producto.get('cantidad')}')