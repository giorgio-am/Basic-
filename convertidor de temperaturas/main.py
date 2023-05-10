def celsius_fahrenheit(celsius):
    return celsius * 9/5 + 32
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit-32)*5/9

celsius = float(input("Ingrese temperatura en celsius: "))
fahrenheit = float(input("Ingrese temperatura en fahrenheit: "))

print(f' {celsius} celsius equivale a {celsius_fahrenheit(celsius)} en fahrenheit')
print(f'{fahrenheit} fahrenheit equivale a {fahrenheit_celsius(fahrenheit)} en celsius')