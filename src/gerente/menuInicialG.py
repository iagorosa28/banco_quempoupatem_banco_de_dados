from printsMenuInicialG import prints_menu_inicial_g

def menu_inicial_g():
    print()
    print("Menu Inicial Gerente")
    while(True):
        print()
        prints_menu_inicial_g()
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