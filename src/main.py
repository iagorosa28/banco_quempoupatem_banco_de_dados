from config_supabase import supabase
from gerente import menu_acesso_g
from cliente import login_c

# Loop principal:
print()
print("Bem-vindo(a) ao Banco QuemPoupaTem!!!")
while(True):
    print()
    print("Menu de Acesso Banco: ")
    print("---------------")
    print("1. Gerente")
    print("2. Cliente")
    print("3. Sair")
    print("---------------")
    opcao = int(input("Digite uma opção: "))
    if opcao == 1:
        menu_acesso_g()
    elif opcao == 2:
        login_c()
    elif opcao == 3:
        print("Tchau!")
        break
    else:
        print("Opção inválida!")

        #bunda