from Persona import Persona

persona1 = Persona('Karla','Gomez',30)
persona1.mostrar_detalle()
print(__name__) #devuelve Persona en la ejecucion de las primeras lineas, pq se ejecuto ahi el codigo anterior, el main aqui es desde karla
# para evitar que se ejecute el codigo de prueba de otro modulo o clase, debe usarse un if __name__ == '__main__'
# en el modulo que se va a importar, sobre las funciones que no queremos ejecutar en otro archivo.

