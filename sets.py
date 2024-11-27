print('*** -manejo de sets ***')
# Crer un conjunto
mi_set = {1, 2, 3, 4, 5, 6, 4,}
print(f'Mi set: {mi_set}')

# Agregar elementos al set
mi_set.add(7)
mi_set.add(2)

# No agrega numeros repetidos
print(f'Mi set actualizado: {mi_set}')

# Eliminar un elemento del conjunto
mi_set.remove(4)
print(f'Mi set borrando un numero: {mi_set}')

# Iterar los elementos del set
for elemento in mi_set:
    print(elemento, end= " ")

# Comprobar si existe un elemento en el set
print(f'\n Existe el valor de 4 en el set ? {4 in mi_set}')
print(f' Existe el valor de 1 en el set ? {1 in mi_set}')

# Obtener la longitud del set
print(f' Longitud del conjunto: {len(mi_set)}')

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Unir dos set
union = a | b
print(f'\nUnion de A & B : {union}')
#Los que se repiten entre a y b eso seria.
interseccion = a & b
print(f'Interseccion A & B : {interseccion}')

diferencia =  b - a
print(f'Diferencia A & B : {diferencia}')