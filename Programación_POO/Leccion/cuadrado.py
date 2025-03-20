from color import Color
from figura_geometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        #super().__init__(lado)
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.get_alto() * self.get_ancho()