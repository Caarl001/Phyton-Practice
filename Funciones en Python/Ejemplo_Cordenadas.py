print('*** Obtener cordenadas x, y , z ***')

def obtener_cordenadas():
    x, y, z = 10, 20, 30
    return (x, y, z)

# Llamar la funcion de obtener cordenadas
resultado = obtener_cordenadas()
print(resultado)

# Unpacking de la Tupla
x1, y1, z1 = resultado
print(f'Cordenada x = {x1}, Cordenanda y = {y1}, Cordenanda z = {z1}')