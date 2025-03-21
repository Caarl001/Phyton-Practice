from Programación_POO.Leccion.cuadrado import Cuadrado
from Programación_POO.Leccion.rectangulo import Rectangulo

print(' Creacion Objeto Cuadrado '.center(50,'-'))
cuadrado1 = Cuadrado(5,'Rojo')
print(cuadrado1._ancho)
print(cuadrado1._alto)
print(cuadrado1._color)
print(cuadrado1.calcular_area())

cuadrado2 = Cuadrado(4,'Morado')
# MRO - Method Resolution Order
print(Cuadrado.mro())

cuadrado3 = Cuadrado(3,'Verde')
print(f'Calculo área cuadrado {cuadrado3.calcular_area()}')
print(cuadrado3)

print(' Creacion Objeto Triangulo '.center(50,'-'))
rectangulo1 = Rectangulo(3,8,'Verde')
print(f'Calculo area rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)