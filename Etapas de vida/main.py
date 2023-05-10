edad = int(input("Proporciona edad: "))
etapaVida = None

if edad > 0 and edad <= 10: # puede escribirse 0 < edad <= 10
    etapaVida = "Infancia"
elif 10 < edad <= 20:
    etapaVida = "adolescencia"
elif edad > 20 and edad <= 40:
    etapaVida = "adulto joven"
elif edad > 40:
    etapaVida = "GG"
print(etapaVida)