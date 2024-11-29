print(f'*** Diccionarios en Python ***')

# Creamos un diccionario de persona

persona ={
    'nombre': 'Leonardo',
    'edad' : 26,
    'ciudad' : 'Chile'
}

print(f'Diccionario de persona: {persona}')

# Acceder a los elementos del diccionario
print(f'Nombre: {persona['nombre']}')
print(f'Edad: {persona.get('edad')}')
print(f'Ciudad: {persona.get('ciudad')}')

# Modificar un valor del diccionario
persona['edad'] = 25
print(f'\nDiccionario de persona: {persona}')

# Agregar un nuevo elemento
persona['profesion'] = 'Ingeniero'
print(f'\nDiccionario de persona: {persona}')

# Eliminae un elemento
del persona['ciudad']
persona.pop('profesion')
print(f'\nDiccionario de persona: {persona}')

# Iterar los elementos de un dict (llave, valor)
for llave, valor in persona.items():
    print(f'Llave: {llave}, Valor: {valor}')

# Obtener los valores
for valor in persona.values():
    print(f'- Valor: {valor}')

for llave in persona.keys():
    print(f'-- {llave}')

for p in persona.keys():
    print(f'--- {p}')

for pe in persona.values():
    print(f'---- {pe}')
