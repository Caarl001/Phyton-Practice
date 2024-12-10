print('*** Agenda De Contactos ***')

agenda = {
    'Carlos': {
        'telefono': '+569 62745246',
        'email': 'carlos@email.com',
        'direccion': 'calle principal'
    },
    'Maria': {
        'telefono': '+569 62594536',
        'email': 'maria@email.com',
        'direccion': 'calle falsisima'
    },
    'Pedro': {
     'telefono': '+569 75654158',
     'email': 'pedro@email.com',
     'direccion': 'plaza mayor 879'
    }
}

print(agenda)

# Acceder a la informacion de in contacto en especifico
print(f'''Informacion del contacto de Maria:
    Telefono: {agenda['Maria']['telefono']}
    Email: {agenda['Maria']['email']}
    Direccion: {agenda['Maria']['direccion']}
''')
# Agregar nuevo contacto
agenda['Ana'] = {
    'telefono': '+569 65842565',
    'email': 'ana@email.com',
    'direccion': 'calle la falcedad'
}
print(agenda)

for nombre , detalles in agenda.items():
        print(f'\n')
        for clave, valor in detalles.items():
            print(f'- {nombre} - {clave}:{valor}', end= ' ')

# Eliminar un contacto existente
agenda.pop('Pedro')

for nombre , detalles in agenda.items():
    for clave, valor in detalles.items(): # Mostramos los contactos de agendas
        print(f'\n- {nombre} - {clave}:{valor}', end= ' ')

# Mostramos los contactos de agendas pero mas detallada
print(f'\nContacto en la Agenda')
for nombre, detalles in agenda.items():
    print(f'''Nombre: {nombre}
    Telefono: {detalles.get('telefono')}
    Email: {detalles.get('email')}
    Direccion: {detalles.get('direccion')}

''')
