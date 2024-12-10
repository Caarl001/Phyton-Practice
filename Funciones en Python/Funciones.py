print('*** Funciones en Python ***')

# Definir una funcion para mandar a saludar
def saludar(): # Firma del metodo
    # Cuerpo de la funcion
     print('Saludos desde una función...')

# Programa principal, llamamos a la funcion
saludar()
#=====================================================
# Definir una funcion para mandar a saludar
def saludar( mensaje : str ): # Firma del metodo
    # Cuerpo de la funcion
     print(f'Mensaje recibido: {mensaje}')

# Programa principal, llamamos a la funcion
saludar('Hola a todos')

#=======================================================
print('\n*** Funcion Sumar ***')
# Definimos las funciones
def sumar( a, b ):
    resultado = a + b
    return resultado

# Llamamos a la funcion
resultado = sumar(8, 5)
print(f'Resultado función sumar: {resultado}')
resultado = sumar(20,5)
print(f'Resultado función sumar: {resultado}')


