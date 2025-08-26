"""
Crie um programa que calcule o volume de uma caixa retangular. Use as seguintes dimensões:
Comprimento: 12 cm
Largura: 14 cm
Altura: 20 cm O programa deve calcular o volume e exibir o resultado em cm³.

"""

comprimento = 12
largura = 14
altura = 20
volume = comprimento*largura*altura

print(f"O volume da caixa retangular, que tem comprimento de {comprimento} cm, largura de {largura} cm e altura de {altura} cm, é de {volume} cm^3.")

# Para tornar dinâmico seria possível solicitar a entrada do usúario

resposta = input ("Deseja calcular o volume de um retângulo? (Sim/Não)")

if resposta.strip().lower() == "sim":
    comprimento = int(input ("Informe o comprimento: "))
    largura = int(input ("Informe a largura: "))
    altura = int(input ("Informe a altura: "))

    volume = comprimento*largura*altura

    print(f"O volume da caixa retangular, que tem comprimento de {comprimento} cm, largura de {largura} cm e altura de {altura} cm, é de {volume} cm^3.")
else:
    print(f"Ok, o volume não será calculado")