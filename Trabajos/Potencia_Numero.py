print('*** Potencia de un numero usando funciones recursivas ***')

def potencia(base, exponente):
    # Caso base
    if exponente == 0:
        return 1
    else: # Caso recursivo
        return base * potencia(base, exponente - 1)

print(f'2 Elevado a la 3: {potencia(2, 3)}')
print(f'5 Elevado a la 9: {potencia(5, 9)}')