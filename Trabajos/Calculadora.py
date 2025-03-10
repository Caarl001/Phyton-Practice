
def pedir_valores():
    operador1 = float(input('Dame el valor 1: '))
    operador2 = float(input('Dame el valor 2: '))
    return operador1, operador2

def ejecutar_operacion(opcion, salir):
    if 1 <= opcion <= 4:
        operador1, operador2 = pedir_valores()
    resultado = 0
    if opcion == 1:
        resultado = operador1 + operador2
        print(f'\n--- Resultado --- \n {operador1} + {operador2} = {resultado}')
    elif opcion == 2:
        resultado = operador1 - operador2
        print(f'\n--- Resultado --- \n {operador1} - {operador2} = {resultado}')
    elif opcion == 3:
        resultado = operador1 * operador2
        print(f'\n--- Resultado --- \n {operador1} * {operador2} = {resultado}')
    elif opcion == 4:
        resultado = operador1 / operador2
        print(f'\n--- Resultado --- \n {operador1} / {operador2} = {resultado}')
    elif opcion == 5 :
        print('Saliendo del programa de calculadora, hasta pronto!')
        salir = True
    else:
        print('\nOpcion invalida, proporciona una opcion valida')
    return salir

def mostrar_menu():
        print(''' --- Calculadora ---
        1. Sumar
        2. Restar
        3. Mulpiplicar
        4. Dividir
        5. Salir ''')
        return  int (input('\t\tProporcione una opción: '))

# Programa principal
if __name__ == '__main__':
    salir = False
    while not salir:
        opcion = mostrar_menu()
        salir = ejecutar_operacion(opcion, salir)


