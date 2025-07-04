#calculando a idade de uma pessoa
print("******Qual sua idade*****")
from datetime import datetime

def calcular_idade_simples():
    """
    Calcula a idade de uma pessoa pedindo apenas o ano de nascimento.
    """
    try:
        ano_nascimento = int(input("Em que ano você nasceu? "))
        
        ano_atual = datetime.now().year
        
        idade = ano_atual - ano_nascimento
        
        print(f"Você tem {idade} anos.")
        
    except ValueError:
        print("Por favor, digite um ano válido (apenas números).")

# Chama a função para executar
calcular_idade_simples()