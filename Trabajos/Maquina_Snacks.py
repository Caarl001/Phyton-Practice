# Inventario
snacks = [
    {'Id' : 1,  'Nombre' : 'Papas', 'Precio' : 30 },
    {'Id' : 2,  'Nombre' : 'Refresco', 'Precio' : 50 },
    {'Id' : 3,  'Nombre' : 'Sandwich', 'Precio' : 120 }
]

# Lista de productos (Vacia). Snacks ya comprados
productos = []

# Funciones para el inventario
def mostrar_snacks():
    print('\n--- Snacks Disponibles ---')
    for snack in snacks:
        print(f'Id: {snack.get('Id')} -> {snack.get('Nombre')}'
              f' - ${snack.get('Precio')}')

def buscar_snack_por_id(id_buscar):
    for snack in snacks:
        if snack.get('Id') == id_buscar:
            return snack
# Si llegamos al final y no se encontro el snack regresa el valor None
    return None

def comprar_snack():
    id_snack = int(input('Que snack quieres comprar (Id): '))
    snack_encontrado = buscar_snack_por_id (id_snack)
    if snack_encontrado is not None :
        productos.append(snack_encontrado)
        print('\n--- Compra de Snacks ---')
        print(f'Snack agregado: {snack_encontrado}')
    else:
        print(f'\nSnack no encontrado con el id: {id_snack}')

def mostrar_ticket():
    ticket = f'\t --- Ticket de venta ---'
    total = 0
    for producto in productos:
        ticket += f'\n\t - {producto.get('Nombre')} - ${producto.get('Precio')}'
        total += producto.get('Precio')
    ticket += f'\n\t TOTAL -> ${total}'
    print(ticket)

# Programa principal

if __name__ == '__main__':
    while True:
        print('''\n--- Maquina De Snacks ---
            1. Mostrar Snacks
            2. Comprar Snack
            3. Mostrar Ticket
            4. Salir''')
        opcion = int(input('Proporciona una opción: '))

# Opciones

        if opcion == 1:
            mostrar_snacks()
        elif opcion == 2:
            comprar_snack()
        elif opcion == 3:
            mostrar_ticket()
        elif opcion == 4:
            print('See you later! | Hasta luego!')
            break
        else:
            print('\nOpcion invalida, proporciona una opcion valida')