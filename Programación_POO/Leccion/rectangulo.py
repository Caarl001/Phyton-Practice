from Programación_POO.Leccion.color import Color
from Programación_POO.Leccion.figura_geometrica import FiguraGeometrica


class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, ancho ,alto, color):
        FiguraGeometrica.__init__(self, ancho , alto)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'
