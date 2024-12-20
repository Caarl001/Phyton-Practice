# *args - argumentos - tupla
# **kwargs - keyword arguments (key, value) como un edict
print('\n*** Argumentos variables en forma de dict ***')

def superheroe_superpoderes( nombre, *args, **kwargs):
    print(f'Superheroe: {nombre} - {args} - Mas info: {kwargs}')

# Llamamos la funcion
superheroe_superpoderes('Spiderman','instinto Arácnido' , edad=16 , empresa='Marvel')
superheroe_superpoderes('Ironman', 'Multimillonario' , 'PlayBoy' , edad=45)

# Es opcional enviar argumentos variables
superheroe_superpoderes('Mi vecino', 'Luis Muñoz', personalidad= 'Curao Drogadicto')