# metodo para ejecutar un metodo o mas
from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalle(objeto):
    print(type(objeto))
    print(objeto)
    if isinstance(objeto, Gerente):
        print(objeto.departamento)    # pregunto si es q el objeto es de clase Gerente entonces ahi imprimo


empleado = Empleado('juan', 5000)

gerente = Gerente('eduardo', 10000, "mkt")
imprimir_detalle(gerente)
imprimir_detalle(empleado)

