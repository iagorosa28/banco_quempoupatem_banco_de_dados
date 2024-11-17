from config_supabase import supabase

# Login do cliente:
def login_c():
    print()
    # implementar login aqui (Mariah).
    print("Login Cliente")
    # se o login for concluído -> então chamar a função menu_c.
    menu_c()

# Menu cliente:
def menu_c():
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