"""
Crie um programa que permita a um professor registrar as notas de uma turma. 
O programa deve continuar solicitando notas até que o professor digite 'fim'. 
Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar 
solicitando. No final, deve exibir a média da turma.
"""

notas = []

print("Digite as notas da turma (de 0 a 10).")
print("Quando terminar, digite 'fim'.")

while True:  # loop infinito, só vai parar com 'break'
    entrada = input("Digite uma nota ou 'fim': ")

    if entrada.lower() == "fim":  # .lower() garante que aceita 'FIM' ou 'Fim'
        break  # sai do loop

    try:
        nota = float(entrada)  # converte para número (float aceita decimais)

        # 3. Verificar se a nota é válida (entre 0 e 10)
        if 0 <= nota <= 10:
            notas.append(nota)  # adiciona na lista
        else:
            print("Nota inválida! Digite um valor entre 0 e 10.")

    except ValueError:  # erro caso não consiga converter para número
        print("Entrada inválida! Digite um número ou 'fim'.")

if len(notas) > 0:
    media = sum(notas) / len(notas)
    print(f"\n A média da turma é: {media:.2f}")
else:
    print("\n Nenhuma nota válida foi registrada.")