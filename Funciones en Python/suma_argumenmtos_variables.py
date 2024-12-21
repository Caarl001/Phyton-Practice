print(f'*** Suma con argumentos variables ***')

# Funcion sumar que acepta argumentos variables

def sumar(*args):
    total = 0
    for numero in args:
        total += numero
    return total

# Llamamos la funcion sumar
resultado = sumar(1, 2, 3, 4, 5)
print(f'Resultado de la suma: {resultado}')

#==============================================
print('\n*** Imprimir detalles de una persona usando Kwargs ***')

# Funcion que acepte argumentos variables en forma de llave valor dict

def imprimir_detalle_persona(**kwargs):
    print(f'\nValores recibidos: ')
    for llave, valor in kwargs.items():
        print(f'{llave}: {valor}')

# Llamamos a la funcion
imprimir_detalle_persona(nombre='Karla', edad=30, ciudad='Mexico')
imprimir_detalle_persona(nombre='Carlos', edad=28, ciuduad='Argentina', puesto='Perro Bomba')

#============================================================================
print('*** Funcion par ***')

# Funcion para saber si un numero es par o no
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# Llamamos a la funcion
if __name__ == '__main__':
    numero =int(input('Proporciona un valor numerico: '))
    print(f'Numero par? {es_par(numero)}')