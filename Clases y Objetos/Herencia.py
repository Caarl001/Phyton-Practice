class Animal:
    def comer(self):
        print('Como muchas veces al dia')

    def dormir(self):
        print('Duermo muchas veces al dia')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')
# Sobreescribir
    def dormir(self):
        print('Duermo 15 horas al dia')

# Programa principal
print('Ejemplo')
animal1 = Animal()
animal1.comer()
animal1.dormir()

animal2 = Perro()
animal2.hacer_sonido()

# Clases en Python
#  __init__() inializar y agregar atributos
#  __str__() estado de nuestro obj
#  __eq__()  comparar si son iguales