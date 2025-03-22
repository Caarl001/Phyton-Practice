#with open('Prueba.txt', 'r', encoding='utf8') as archivo:
from Archivos.manejo_archivos import ManejoArchivos

with ManejoArchivos('Prueba.txt') as archivo:
    print(archivo.read())

