"""
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

Valor em reais: R$ 100.00

Taxa do dólar: R$ 5.60

Taxa do euro: R$ 6.60 

"""

valor_reais = 100.00
taxa_dolar = 5.60
taxa_euro = 6.60 

conversor_dolar = valor_reais / taxa_dolar
conversor_euro = valor_reais / taxa_euro

print (f"O valor em reais: R$ {valor_reais:.2f}.")
print (f"O valor em dolares: US$ {conversor_dolar:.2f}.")
print (f"O valor euros: € {conversor_euro:.2f}.")
