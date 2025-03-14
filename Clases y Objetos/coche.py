# Definimod la clase coche
class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca # Atributo publico
        self._modelo = modelo # Atributo protegido
        self.__color = color # Atributo privado

    def conducir(self):
        print(f'''Conduciendo el coche:
        Marca: {self.marca}
        Modelo: {self._modelo}
        Color: {self.__color}''')

# Programa principal
if __name__ == '__main__':
    coche1 = Coche('Toyota', 'Yaris', 'Azul')
    coche1.conducir()