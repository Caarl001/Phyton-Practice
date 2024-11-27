print(f'*** Lista de Suscritores ***')

#Definir nuestro set inicial

#suscriptores = {} # aqui se define un diccionario vacio
suscriptores = set() # Definimos un set vacio

numero_suscriptores = int(input('Proporciona el número de suscriptores iniciales: '))
for _ in range(numero_suscriptores):
    suscriptores.add(input('Nuevo suscriptor (email)'))

print(f'Lista de suscriptores incial: {suscriptores}')

# Verificar si un nuevo suscriptor ya esta en la lista
nuevo_suscriptor = input(f'proporciona el nuevo suscriptor: ')
if nuevo_suscriptor in suscriptores:
    print(f'El nuevo suscriptor ya esta en la lista {nuevo_suscriptor}')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'\nEl nuevo suscriptor se ha agregado a la lista: {nuevo_suscriptor}')
    print(f'Lista de suscriptores {suscriptores}')

    #for numerar in suscritores:
    #    print (numerar , end= '\nCorreo: ' )

# Eliminamos un suscriptor
suscriptores_eliminar = input('Proporciona el suscriptor a eliminar')
suscriptores.remove(suscriptores_eliminar)
print(f'\nEl suscriptor se ha eliminado de la lista: {suscriptores_eliminar}')
print(f'Lista de suscriptores {suscriptores}')

# Verificamos la cantidad total de suscriptores
print(f'\nCantidad total suscriptores : {len(suscriptores)}')

# Mostrar todos los suscriptores
print(f'----- Lista de Suscriptores ------')
for suscriptor in suscriptores:
    print(f'- {suscriptor}')