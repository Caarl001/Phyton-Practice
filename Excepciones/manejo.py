from Excepciones.numeros_identicos import Numeros
resultado = None

try:
    a = int(input('Primer Numero: '))
    b = int(input('Segundo Numero: '))
    if a == b:
        raise Numeros('Numeros identicos')
    resultado = a/b
except ZeroDivisionError as e:
    print(f'Ocurrio un error: {e} , {type(e)}')
except TypeError as e:
    print(f'Ocurrio un error: {e}')
except Exception as e:
    print(f'Exception - Ocurrio un error: {e}, {type(e)}')
else:
    print('No se arrojo ninguna excepcion ')
finally: # Siempre se ejecuta
    print('Ejecucion del bloque finally')
print(f'Siguiente'.center(50, '-'))

print(f'Resultado: {resultado}')
print('Continuemos...')