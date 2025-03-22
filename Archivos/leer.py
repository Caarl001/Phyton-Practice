try:
    archivo = open('prueba.txt', 'r', encoding='utf8')
    print(archivo.read(5))
    # Leer algunos caracteres
    #print(archivo.read(5))

    # Leer lineas completas
    print(archivo.readline())

    for linea in archivo:
        print(linea)
    # Abrimos un nuevo archivo
    # a - anexar informacion

    archivo2 = open('copia.txt', 'a')
    archivo2.write(archivo.read())

except Exception as e:
    print(e)
finally:
    archivo.close()
    archivo2.close()
    print('Se termino el proceso')