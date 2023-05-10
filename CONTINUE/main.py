# numeros pares dentro de un conjunto de datos
# for i in range(6):
#     if i % 2 == 0:
#         print(f"valor: {i}")

# lo mismo usando continue

for i in range(6):
    if i % 2 != 0:
        continue
    print(f"Valor: {i}")