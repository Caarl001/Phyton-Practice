
class Animal:
    def hacer_sonido(self):
        print('Hago un sonido')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')

class Gato(Animal):
    def hacer_sonido(self):
        print('Puedo wear')
# Funcion polimorfica
def hacer_sonido_animal(animal):
    animal.hacer_sonido()
print('Ejemplo')
animal1 = Animal()
hacer_sonido_animal(animal1)
perro1 = Perro()
perro1.hacer_sonido()
