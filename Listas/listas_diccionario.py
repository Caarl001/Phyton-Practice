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
print(f'''      Nombre: {persona[0].get('nombre')}
           Apellido: {persona[0].get('apellido')}
           Edad: {persona[0].get('edad')}''')

# Recorrer los elementos de la lista
print()
for contador, persona in enumerate(persona):
    print(f'{contador} - Persona: {persona}')
    print(f'Detalle: nombre: {persona.get('nombre')}, apellido: {persona.get('apellido')}')