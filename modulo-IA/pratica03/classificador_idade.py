"""
Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

Criança (0-12 anos),

Adolescente (13-17 anos),

Adulto (18-59 anos)

Idoso (60 anos ou mais).


"""
# Entrada do usuário
entrada = input("Informe a idade: ").strip()

# Tenta converter para número inteiro
try:
    idade = int(entrada)
except ValueError:
    print("Idade inválida! Digite um número INTEIRO (ex.: 0, 15, 60).")
else:
    # Agora que temos certeza que é inteiro, validamos a faixa etária
    if idade < 0:
        print("Idade inválida! Idade não pode ser negativa.")
    elif idade <= 12:
        print(f"A idade de {idade} anos é classificada como Criança.")
    elif idade <= 17:
        print(f"A idade de {idade} anos é classificada como Adolescente.")
    elif idade <= 59:
        print(f"A idade de {idade} anos é classificada como Adulto.")
    else:
        print(f"A idade de {idade} anos é classificada como Idoso.")