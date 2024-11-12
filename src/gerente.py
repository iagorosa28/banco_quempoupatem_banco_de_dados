# Loop inicial dos gerentes (antes deles "logarem"):
def menu_inicial_g():
    print()
    print("Menu Inicial Gerente")
    while(True):
        print()
        print("Menu: ")
        print("1. Cadastrar")
        print("2. Logar")
        print("3. Excluir")
        print("4. Sair")
        opcao = int(input("Digite uma opção: "))
        if opcao == 1:
            print("Cadastrar!")
        elif opcao == 2:
            print("Logar!")
        elif opcao == 3:
            print("Excluir!")
        elif opcao == 4:
            print("Tchau!")
            break
        else:
            print("Opção inválida!")