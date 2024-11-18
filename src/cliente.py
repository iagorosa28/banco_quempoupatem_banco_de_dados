from config_supabase import supabase

# Login do cliente:
def login_c():
    print()
    cpf = input("Insira seu CPF: ")
    verificacaoCPF = consultar_cpf(cpf)
    while True:
        if verificacaoCPF == False:
            cpf = input("CPF incorreto! Digite novamente: ")
            verificacaoCPF = consultar_cpf(cpf)
        else:
            resultado = supabase.table("cliente").select("id").eq("cpf", cpf).execute()
            id_cliente = resultado.data[0]["id"]  # Obtém o ID do gerente.
            break
        
    senha = input("Insira uma senha: ")
    verificacaoSenha = supabase.table("conta").select("senha").eq("id_cliente", id_cliente).execute()
    conferindoSenha = verificacaoSenha.data[0]["senha"]
    while True:
        if senha != conferindoSenha:
            senha = input('Senha Incorreta! Digite novamente: ')
            verificacaoSenha = supabase.table("conta").select("senha").eq("id_cliente", id_cliente).execute()
        else:
            break

    resultado = supabase.table("cliente").select("id").eq("cpf", cpf).execute()
    id_cliente = resultado.data[0]["id"]  # Obtém o ID do gerente.
    # Chama o menu do gerente com o ID.    
    menu_c(id_cliente)

# Verifica se o CPF que foi digitado bate com algum CPF na tabela cliente:
def consultar_cpf(cpf):
    resultado = supabase.table("cliente").select("cpf").eq("cpf", cpf).execute()
    if resultado.data:
        return True
    else:
        return False

# Menu cliente:
def menu_c(id_cliente):
    print()
    print("Área Cliente")
    while(True):
        print()
        print("---------------")
        print("Menu Cliente: ")
        print("1. Consultar Saldo")
        print("2. Débito")
        print("3. Depósito")
        print("4. Transferência")
        print("5. Extrato")
        print("6. Investimentos")
        print("7. Sair")
        print("---------------")
        opcao = int(input("Digite uma opção: "))
        if opcao == 1:
            consultar_saldo()
        elif opcao == 2:
            debito()
        elif opcao == 3:
            deposito()
        elif opcao == 4:
            transferencia()
        elif opcao == 5:
            extrato()
        elif opcao == 6:
            investimentos()
        elif opcao == 7:
            print("Tchau!")
            break
        else:
            print("Opção inválida!")

# Consultar saldo:
def consultar_saldo():
    print()
    # Implementar aqui (Mariah).
    print("Consultar Saldo")

# Débito:
def debito():
    print()
    # Implementar aqui (Iago).
    print("Débito")

# Depósito:
def deposito():
    print()
    # Implementar aqui (Iago).
    print("Depósito")

# Transferência:
def transferencia():
    print()
    # Implementar aqui (Iago).
    print("Transferência")

# Extrato:
def extrato():
    print()
    # Implementar aqui (Mariah).
    print("Extrato")

# Investimentos:
def investimentos():
    print()
    # Implementar aqui (Iago).
    print("Investimentos")