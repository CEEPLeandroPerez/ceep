# Nome correto
nome_certo = "Ana"

# Contador de tentativas
tentativas = 0

# Pergunta como o usuário quer tentar
print("Escolha uma opção:")
print("1 - Digitar o nome completo")
print("2 - Montar o nome letra por letra")
opcao = input("Digite 1 ou 2: ")

# Laço para tentar 6 vezes
while tentativas < 6:
    if opcao == "1":
        # Opção 1: Digitar o nome completo
        nome = input("Digite o nome: ")
        if nome == nome_certo:
            print("Nome correto!")
            break
        else:
            tentativas += 1
            print(f"Nome errado! Restam {6 - tentativas} tentativa(s).")
    elif opcao == "2":
        # Opção 2: Montar letra por letra
        nome_montado = ""
        print(f"Monte o nome com {len(nome_certo)} letras.")
        for i in range(len(nome_certo)):
            letra = input(f"Digite a letra {i+1}: ")
            nome_montado += letra
        if nome_montado == nome_certo:
            print("Nome correto!")
            break
        else:
            tentativas += 1
            print(f"Nome errado! Restam {6 - tentativas} tentativa(s).")
    else:
        print("Opção inválida! Escolha 1 ou 2.")
        opcao = input("Digite 1 ou 2: ")
        continue

if tentativas == 6:
    print("Acabaram as tentativas.")