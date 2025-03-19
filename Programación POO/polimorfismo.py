
class Animal:
    def hacer_sonido(self):
        print('Hago un sonido')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')

class Gato(Animal):
    def hacer_sonido(self):
        print('Puedo wear')

print('Ejemplo')
animal1 = Animal()
animal1.hacer_sonido()
perro1 = Perro()
perro1.hacer_sonido()