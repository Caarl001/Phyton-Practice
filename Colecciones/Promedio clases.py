from traceback import print_tb

print('*** Promedio de Calificaciones ***')

total_calificaciones = int(input(f'Proporciona el numero. de calificaciiones a evaluar: '))
calificaciones = []

# Interar las calificaciones
for indice in range(total_calificaciones):
    calificacion = float(input(f'Calificacion [{indice}] = '))
    calificaciones.append(calificacion)

# Impirmimos las calificaciones proporcionadas
print(f'\nLas calificaciones proporcionadas son: {calificaciones}')

# Calculamos el promedio de las calificaciones

suma_calificaciones = sum(calificaciones)
promedio = suma_calificaciones / total_calificaciones
print(f'\nPromedio de las calificaciones: {promedio}')