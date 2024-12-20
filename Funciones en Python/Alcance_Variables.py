print('*** Alcance de variables ***')

contador_global = 0

def incrementar_contador():
    # Declaramos una variable local
    contador_local = 0

    # Usar la variable global
    global contador_global
    # Incrementamos la variable global
    contador_global += 1

    # Incrementamos la variable local
    contador_local += 1

    # Imprimimos ambos contadores
    print(f'Contador local: {contador_local}')
    print(f'Contador global: {contador_global}\n')

# Llamamos varias veces la función
incrementar_contador()
incrementar_contador()
incrementar_contador()

# Terminando el programa
print(f'Valor variable global: {contador_global}')