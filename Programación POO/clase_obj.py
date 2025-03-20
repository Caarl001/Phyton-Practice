class Persona:
    def __init__(self, nombre , apellido):
        self.nombre = nombre
        self.apellido = apellido

# Sobre escribir el __str__
    def __str__(self):
        return f'''Persona:
        nombre = {self.nombre}
        apellido = {self.apellido}
        Dir. men. {super.__str__(self)}'''

# Codigo principal
persona1 = Persona('Leonardo','Venegas')
print(persona1)
persona2 = Persona('','')
print(persona2)
