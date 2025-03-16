class Aritmetica:

    def __init__(self, operando1 , operando2):
        self._operando1 = operando1
        self._operando2 = operando2

    def sumer(self):
        resultado = self._operando1 + self._operando2
        print(f'Resultado de la suma: {resultado}')

    def resta(self):
        resultado = self._operando1 - self._operando2
        print(f'Resultado de la resta: {resultado}')

    def multiplicar(self):
        resultado = self._operando1 * self._operando2
        print(f'Resultado de la multiplicación: {resultado}')

    def division(self):
        resultado = self._operando1 / self._operando2
        print(f'Resultado de la division: {resultado}')

    @property
    def operando1(self):
        return self._operando1

    @operando1.setter
    def operando1(self, operando1):
        self._operando1 = operando1

    @property
    def operando2(self):
        return self._operando2

    @operando2.setter
    def operando2(self, operando2):
        self._operando2 = operando2


# Programa principal
if __name__ == '__main__':
    print(' --- Ejemplo Clase Aritmetica ---')
    aritmetica1 = Aritmetica(5 , 7)
    print('Primer objeto')
    print(f'Valor operando1 del objeto aritmetica1: {aritmetica1.operando1}')
    print(f'Valor operando2 del objeto aritmetica2: {aritmetica1.operando2}')
    aritmetica1.sumer()
    aritmetica1.resta()
    aritmetica1.multiplicar()
    aritmetica1.division()

    # Otro objeto
    aritmetica2 = Aritmetica(12, 16)
    print(f'Valor operando1 del objeto aritmetica1: {aritmetica2.operando1}')
    print(f'Valor operando2 del objeto aritmetica2: {aritmetica2.operando2}')
    aritmetica2.sumer()
    aritmetica2.resta()
    aritmetica2.multiplicar()
    aritmetica2.division()

