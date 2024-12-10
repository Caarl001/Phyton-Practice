from Funciones import sumar

print('*** Funcion de sumar ***')

# Llamamos a la funcion
resultado = sumar(8, 5)
print(f'Resultado funcion sumar: {resultado}')

#==========================
# Argumetos con nombres
print('\n*** Funcion con argumentos por nombre ***')

def imprimirPersona (nombre, apellido, edad):
    print(f'Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}')

# Primero llamamos la funcion pasando los argumentos de manera posicional
imprimirPersona('Ricardino', 'Ronaldhinno', 28)

# Llamar la funcion usando argumentos por nombre
imprimirPersona( nombre='Carlos' , apellido='Rojas' , edad=25)

# Llamar la funcion usando argumentos por nombre, pero intercambiando el orden
imprimirPersona(edad=25, nombre='juan', apellido='Reyes')

# Definir argumentos por default
imprimirPersona(nombre='Carlos', apellido='' , edad= '' )