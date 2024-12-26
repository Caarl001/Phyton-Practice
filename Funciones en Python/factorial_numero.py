from idlelib.colorizer import prog_group_name_to_tag
from turtledemo.rosette import mn_eck

print('*** Factorial del numero 5 ***')

# Definimos la funcion factorial recursiva
def factorial_recursiva(numero):
# caso base, factorial 0! = 1, 1! = 1}
    if numero == 0 or numero == 1 :
        print(f'Resultado factorial parcial {numero} es: 1')
        return 1
    else: # Caso recursivo
        factorial_principal = numero * factorial_recursiva((numero - 1))
        print(f'Resultado factorial parcial {numero} es: {factorial_principal}')
        return factorial_principal

numero = 5
resultado = factorial_recursiva(numero)
print(f'El factorial del numero {numero} es:  {resultado}')