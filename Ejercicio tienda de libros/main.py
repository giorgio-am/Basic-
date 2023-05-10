print("Proporcione los siguientes datos del libro: ")
nombre = input("Proporciona el nombre del libro: ")
id = int(input("Proporcione el ID del libro: "))
precio = float(input("Proporcione el precio del libro: "))
envioGratuito = input("Indica si es envio es gratuito (True/False): ")

if envioGratuito == "True":
    envioGratuito = True
elif envioGratuito == "False":
    envioGratuito = False
else:
    envioGratuito = "valor incorrecto"
# usar comilla triple: agregar información en varias lineas
print(f''' 
    Nombre: {nombre}
    ID: {id}
    Precio: {precio}
    Envio Gratuito: {envioGratuito}
''')
