numero = int(input("proporciona un valor entre 1 y 3: "))
numeroTexto = ""
if numero == 1:
    numeroTexto = "numero uno"
elif numero == 2:
    numeroTexto = "numero dos"
elif numero == 3:
    numeroTexto = "numero tres"
else:
    numeroTexto = "Valor fuera de Rango"

print(f"Numero proporcionado: {numero} - {numeroTexto}")