from config_supabase import supabase

# Login do cliente:
def login_c():
    print()
    print("Login Cliente")
    # implementar login aqui (Mariah).
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
            print("Saldo!")
        elif opcao == 2:
            print("Débito!")
        elif opcao == 3:
            print("Depósito!")
        elif opcao == 4:
            print("Transferência!")
        elif opcao == 5:
            print("Extrato!")
        elif opcao == 6:
            print("Investimento!")
        elif opcao == 7:
            print("Tchau!")
            break
        else:
            print("Opção inválida!")