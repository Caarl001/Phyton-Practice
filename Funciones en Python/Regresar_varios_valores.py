from idlelib.colorizer import prog_group_name_to_tag

print('*** Regresar una tupla de valores desde una funciom ***')

# Definicion de la funcion
def persona_mayusculas(nombre, apellido, edad) :
    print(f'Esta funcion regresa varios valores (Tupla)')
    return nombre.upper(), apellido.upper(), edad
# Programa principal
nombre, apellido, edad = persona_mayusculas('Sandra', 'Gonzalez', 45)
print(f'Resultado persona: nombre= {nombre}, apellido = {apellido}, edad = {edad}')