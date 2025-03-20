class Monitor:
    contador_monitores = 0

    def __init__(self, marca, tamanio):
        Monitor.contador_monitores += 1
        self.id_monitor = Monitor.contador_monitores
        self.tamanio = tamanio
        self.marca = marca

    def __str__(self):
        return f'Id: {self.id_monitor}, Marca: {self.marca}, Tamaño: {self.tamanio}'

if __name__ == '__main__':
    monitor1 = Monitor('HP',15)
    print(monitor1)
    monitor2 = Monitor('Dell','27')
