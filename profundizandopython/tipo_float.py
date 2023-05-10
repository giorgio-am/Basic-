# profundizando en tipo float
a = 3.0
print(f'a: {a}')
#interpolado/ cuantos decimales quiero ver
print(f'a: {a:.2f}')
# Constructor float puede recibir int y str
a = float(10)
a = float('10')
print(f'a: {a:.2f}')
# notación exponencial (valores positivos o negativos)
a = 3e5 # por 10 elevado a 5
print(f'a: {a:.2f}')

a = 3e-5
print(f'a: {a:.5f}')



