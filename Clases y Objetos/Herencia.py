class Animal:
    def comer(self):
        print('Como muchas veces al dia')

    def dormir(self):
        print('Duermo muchas veces al dia')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')
# Programa principal
print('Ejemplo')
animal1 = Animal()
animal1.comer()
animal1.dormir()

animal2 = Perro()
animal2.hacer_sonido()