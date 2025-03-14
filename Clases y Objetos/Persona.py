# Definicion de una clase

class PersonaPrincipal:
    # Constructor

    def inicializar_persona(self, nombre, apellido):
        # Crearemos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'''Persona:
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')

# Creacion de un primer objeto

if __name__ == '__main__':
    # Creacion de un primer objeto
    persona1 = PersonaPrincipal() # Crear un objeto vacio en memoria
    persona1.inicializar_persona ('Layla', 'Acosta')
    persona1.mostrar_persona()

# Crearemos un segundo objeto
    persona2 = PersonaPrincipal() # Crea un objeto vacio en memoria
    persona2.inicializar_persona('Ian', 'Sanchez')
    persona2.mostrar_persona()