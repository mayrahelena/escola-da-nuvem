"""
A fórmula para calcular a área de uma circunferência é: área = π ×raio2. Considerando para
este problema que π = 3.14159265: 

• Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π. 

Entrada: A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável
raio.
Saída: Apresente a mensagem "A=" seguido pelo valor da variável area, conforme exemplo
abaixo, com 4 casas após o ponto decimal.
"""

# O  Valor de pi
pi = 3.14159265

# Lendo a entrada do valor do raio informada pelo usuário
raio = float(input("Informe o valor do raio em cm (exemplo: 12): "))

# Calculando a área da circunferência
area = pi * (raio ** 2)

# Exibindo o resultado com 4 casas decimais
print(f"A área da circunferência, do raio de {raio} cm, é A={area:.4f} cm²")
