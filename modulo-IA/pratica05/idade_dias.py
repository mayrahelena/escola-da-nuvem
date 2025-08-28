"""
Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.

Fiz um código que calcula a partir da data de nascimento completo só pra teste, segue o código:

from datetime import date

def idade_em_dias(ano_nascimento, mes_nascimento, dia_nascimento):
    # Cria a data de nascimento
    nascimento = date(ano_nascimento, mes_nascimento, dia_nascimento)
    # Data de hoje
    hoje = date.today()
    # Diferença em dias
    idade_dias = (hoje - nascimento).days
    return idade_dias

# Exemplo de uso
ano = int(input("Ano de nascimento: "))
mes = int(input("Mês de nascimento: "))
dia = int(input("Dia de nascimento: "))

print(f"Sua idade em dias é {idade_em_dias(ano, mes, dia)} dias.")

"""

import datetime

def calcular_idade_dias(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365
    return idade_dias

ano_nascimento = int(input("Digite o ano de nascimento: "))
idade_dias = calcular_idade_dias(ano_nascimento)

print(f"Sua idade aproximada em dias é [{idade_dias}] dias.")