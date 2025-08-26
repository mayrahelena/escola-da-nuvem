"""
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 

O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""


temperatura = float(input("Digite a temperatura: "))
origem = input("Digite a escala de origem (C, F ou K): ").upper()
destino = input("Digite a escala de destino (C, F ou K): ").upper()


if origem == destino:
    resultado = temperatura

elif origem == "C":  # Celsius para outras
    if destino == "F":
        resultado = (temperatura * 9/5) + 32
    elif destino == "K":
        resultado = temperatura + 273.15

elif origem == "F":  # Fahrenheit para outras
    if destino == "C":
        resultado = (temperatura - 32) * 5/9
    elif destino == "K":
        resultado = (temperatura - 32) * 5/9 + 273.15

elif origem == "K":  # Kelvin para outras
    if destino == "C":
        resultado = temperatura - 273.15
    elif destino == "F":
        resultado = (temperatura - 273.15) * 9/5 + 32

print(f"{temperatura}°{origem} equivale a {resultado:.2f}°{destino}")