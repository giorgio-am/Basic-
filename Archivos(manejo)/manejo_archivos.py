try:
    archivo = open('prueba.txt', 'w', encoding='utf8') #w es write y permite escribir en el archivo
    archivo.write('Agregamos información al archivo')
    archivo.write(('\nadios'))
except Exception as e:
    print(e)
finally:
    archivo.close()
    print('Archivo cerrado')
    # archivo.write('asdasd')