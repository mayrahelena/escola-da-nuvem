"""
Crie um programa que verifique se uma senha é forte. 
Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. 
O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.


"""

while True:
    entrada = input("Digite a senha (ou 'sair' para encerrar): ")
    if entrada.strip().lower() == "sair":
        print("Programa encerrado.")
        break
    senha = entrada
    
    if len(senha) < 8:
        print("Senha fraca. Precisa ter pelo menos 8 caracteres.")
        continue
    if any(ch.isspace() for ch in senha):
        print("Senha inválida. Não pode conter espaços.")
        continue
    if not any(ch.isdigit() for ch in senha):
        print("Senha fraca. Precisa ter pelo menos um número.")
        continue
    if not any(ch.isalpha() for ch in senha):
        print("Senha fraca. Precisa ter pelo menos uma letra.")
        continue
    
    print("Senha forte e válida!")
    break