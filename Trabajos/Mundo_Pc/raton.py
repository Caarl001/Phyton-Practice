from Trabajos.Mundo_Pc.dispositivo_entrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contador_ratones = 0

    def __init__(self, marca, tipo_entrada):
        Raton.contador_ratones += 1
        self._id_raton = Raton.contador_ratones
        #self.marca = marca
        #self.tipo_entrada = tipo_entrada
        super().__init__(marca, tipo_entrada)
    def __str__(self):
        return f'Id: {self._id_raton}, Marca: {self._marca}, Tipo Entrada: {self._tipo_entrada}'

# Codigo Principal
if __name__ == '__main__':
    raton1 = Raton('HP', 'USB')
    print(raton1)
    raton2 = Raton ('Acer','Bluetooth')
    print(raton2)