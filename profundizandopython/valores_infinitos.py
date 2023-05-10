# manejo de valores infinitos
import math
from decimal import Decimal

#usando MATH
infinito_positivo = float('inf')
print(infinito_positivo)
print(f'Es infinito: {math.isinf(infinito_positivo)}')
# para el negativo es '-inf'

infinito_positivo = math.inf
print(infinito_positivo)
print(f'Es infinito: {math.isinf(infinito_positivo)}')

infinito_negativo = -math.inf
print(infinito_negativo)
print(f'Es infinito: {math.isinf(infinito_negativo)}')

# usando DECIMAL
infinito_positivo = Decimal('Infinity')
print(infinito_positivo)
print(f'Es infinito: {math.isinf(infinito_positivo)}')
# en negativo se hace con -Infinity
