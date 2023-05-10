import math
from decimal import Decimal
# NaN Not a Number, no es caps sensitive
# es un tipo de dato numerico indefinido
a = float('NaN')
print(f'a: {a}')
print(f'Es Nan (not a number)?: {math.isnan(a)}')

a = Decimal('NaN')
print(f'Es Nan (not a number)?: {math.isnan(a)}')
