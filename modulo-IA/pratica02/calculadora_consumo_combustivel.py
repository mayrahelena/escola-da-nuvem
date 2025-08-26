"""
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

Distância percorrida: 300 km
Combustível gasto: 25 litros 

O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, 
incluindo o resultado final arredondado para duas casas decimais.
"""

distância_percorrida = 300
combustivel_gasto = 25
consumo_medio = distância_percorrida / combustivel_gasto

print(f"Distância percorrida {distância_percorrida} km.")
print(f"O combustível gasto: {combustivel_gasto} litros.") 
print(f"O consumo médio para esse trajeto foi: {consumo_medio} km/l.")