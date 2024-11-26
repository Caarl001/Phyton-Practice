print("***  Desempaquetado de Tuplas***")

producto = ('P001', 'Camisa', 20.000,)

# Desempaquetado
id, descripcion, precio, = producto

#imprimir los valores
print(f'Tupla completa: {producto}')
# Valores independientes ya desempaquetados
print(f'Producto id = {id}\nDescripcion = {descripcion}\nPrecio = {precio}\n')

productos = [
    ('P001', 'Camiseta', 15.000),
    ('P002', 'Jeans', 20.000),
    ('P003', 'Sudadera', 30.000),
]
# Imprimir la informacion de cada producto y ademas calculamos el precio total

precio_total = 0
print(f'\n Informacion de los productos: ')
for producto in productos :
    id, descripcion, precio = producto
    print(f'Producto id = {id}\nDescripcion = {descripcion}\nPrecio = {precio}\n')
    precio_total += precio
    print(f'Precio total de los productos: ${precio_total}')