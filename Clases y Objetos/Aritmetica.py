class Aritmetica:

    def __init__(self, operando1 , operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumer(self):
        resultado = self.operando1 + self.operando2
        print(f'Resultado de la suma: {resultado}')

    def resta(self):
        resultado = self.operando1 - self.operando2
        print(f'Resultado de la resta: {resultado}')

    def multiplicar(self):
        resultado = self.operando1 * self.operando2
        print(f'Resultado de la multiplicación: {resultado}')

    def division(self):
        resultado = self.operando1 / self.operando2
        print(f'Resultado de la division: {resultado}')

# Programa principal
if __name__ == '__main__':
    print(' --- Ejemplo Clase Aritmetica ---')
    aritmetica1 = Aritmetica(5 , 7)
    aritmetica1.sumer()
    aritmetica1.resta()
    aritmetica1.multiplicar()
    aritmetica1.division()

    # Otro objeto
    aritmetica2 = Aritmetica(12, 16)
    aritmetica2.sumer()
    aritmetica2.resta()
    aritmetica2.multiplicar()
    aritmetica2.division()

