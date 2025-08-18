

def cadastrar_aluno():
    """
    Função para coletar informações de cadastro de um aluno.
    """
    print("--- Formulário de Cadastro ---")

    
    nome_completo = input("Digite o nome completo: ")
   
    cpf = input("Digite o CPF (apenas números): ")
    
    data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
    
    escola = input("Digite o nome da escola onde estuda: ")
   
    endereco = input("Digite o endereço completo (Rua, Número, Bairro, Cidade, Estado): ")

    cep = input("Digite o CEP (apenas números): ")

    
    dados_cadastro = {
        "nome_completo": nome_completo,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "escola": escola,
        "endereco": endereco,
        "cep": cep
    }

    print("\n--- Cadastro Concluído ---")
    
    
    for chave, valor in dados_cadastro.items():
        print(f"{chave.replace('_', ' ').title()}: {valor}")


cadastrar_aluno()