class PersonaSecundario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'''Persona:
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')
        print(f'\t\tDirreción, De Memoria Desde Self:{id(self)}')
        print(f'\t\tDirreción, De Meroria Extra Decimal Desde Self {hex(id(self))}')

    # Creacion de un primer objeto

if __name__ == '__main__':
        # Creacion de un primer objeto
        persona1 = PersonaSecundario('Layla', 'Acosta') # Crear un objeto vacio en memoria
        persona1.mostrar_persona()
        print(f'\t\tDirreción,De Memoria De Persona1: {id(persona1)}')
        print(f'\t\tDirreción,De Memoria Extra Decimal De Persona1: {hex(id(persona1))}')

        # Crearemos un segundo objeto
        persona2 = PersonaSecundario('Ian', 'Sanchez')  # Crea un objeto vacio en memoria
        persona2.mostrar_persona()
        print(f'\t\tDirreción,De Memoria De Persona2: {id(persona2)}')
        print(f'\t\tDirreción,De Memoria Extra Decimal De Persona1: {hex(id(persona2))}')