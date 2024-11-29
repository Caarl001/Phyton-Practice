from AgendaDeContactos import nombre

print(f'*** Lista & Diccionario ***')

persona = [
    {
        'nombre': 'Regina',
        'apellido': 'Flores',
        'edad': 21
    },
    {
        'nombre': 'Alejandro',
        'apellido': 'Reyes',
        'edad': 32
    },
    {
        'nombre': 'Leonardo',
        'apellido': 'Venegas',
        'edad': 26
    }
]
for persona_dict in persona:
    for clave, valor in persona_dict.items():
        print(f'{clave}: {valor} ' , end= '\n')
# Aceder a un diccionario desde una lista
print(f' Nombre: {persona[0].get('nombre')}')
