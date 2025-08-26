"""
Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.


< 18.5: classificacao = "Abaixo do peso" 

< 25: classificacao = "Peso normal"

 < 30: classificacao = "Sobrepeso"

 Para os demais cenários: classificacao = "Obeso"

"""
while True:
    try:
        peso = float(input("Digite seu peso em kg (Ex. 75): ").strip())
        if peso <= 0:
            print("Peso inválido! Digite um valor maior que 0.\n")
            continue
        break
    except ValueError:
        print("Entrada inválida! Digite apenas números.\n")

while True:
    try:
        altura = float(input("Digite sua altura em metros (Ex. 1.85): ").strip())
        if altura <= 0:
            print("Altura inválida! Digite um valor maior que 0.\n")
            continue
        break
    except ValueError:
        print("Entrada inválida! Digite apenas números.\n")

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

print(f"\nSeu IMC é {imc:.2f}")
print(f"Classificação: {classificacao}")