from config_supabase import supabase

# Loop inicial dos gerentes (antes deles "logarem"):
def menu_acesso_g():
    print()
    print("Área de Acesso Gerente")
    while(True):
        print()
        print("Menu de Acesso Gerente: ")
        print("---------------")
        print("1. Cadastrar")
        print("2. Logar")
        print("3. Excluir")
        print("4. Sair")
        print("---------------")
        opcao = int(input("Digite uma opção: "))
        if opcao == 1:
            cadastrar_g()
        elif opcao == 2:
            print("Logar!")
        elif opcao == 3:
            print("Excluir!")
        elif opcao == 4:
            print("Tchau!")
            break
        else:
            print("Opção inválida!")

# Para gerenciar os gerentes (cadastrar e excluir) é preciso de uma chave de acesso fornecida pelo banco.
# Chave de acesso: 15072023
n_acesso = 15072023

# Verifica se o login que foi digitado bate com algum login na tabela gerente:
def consultar_login(login):
    resultado = supabase.table("gerente").select("login").eq("login", login).execute()
    if resultado.data:
        return True
    else:
        return False

# Cadastrar gerente:
def cadastrar_g():
    print()
    chave_acesso = int(input("Digite a chave de acesso do banco: "))
    if chave_acesso == n_acesso:
        nome = input("Insira o nome: ")
        login = input("Insira um login: ")
        consulta = consultar_login(login)
        while consulta:
            login = input("Login já existente! digitar outro login: ")
            consulta = consultar_login(login)
        senha = input("Insira uma senha: ")
        dados = {
            "nome": nome,
            "login": login,
            "senha": senha
        }
        # Insere os dados no banco de dados:
        resultado = supabase.table("gerente").insert(dados).execute()
        # Verifica se os dados foram inseridos com sucesso:
        if resultado.data:
            print("Gerente cadastrado com sucesso!")
        else:
            # Teoricamente era para mostrar qual foi o erro:
            print("Erro ao cadastrar gerente: ", resultado.error)
    else:
        print("Chave de acesso incorreta!")

def login_g():
    print()
    print("Login Gerente")
    # implementar login aqui (Mariah).
    # se o login for concluído -> então chamar a função menu_g.
    menu_g()

# Aqui excluir_g (Iago)

# Menu gerente:
def menu_g():
    print()
    print("Área Gerente")
    while(True):
        print()
        print("---------------")
        print("Menu Gerente: ")
        print("1. Criar Conta Cliente")
        print("2. Excluir Conta Cliente")
        print("3. Consultar Contas Clientes")
        print("4. Cadastrar Empresa")
        print("5. Sair")
        print("---------------")
        opcao = int(input("Digite uma opção: "))
        if opcao == 1:
            print("Criar Conta Cliente")
        elif opcao == 2:
            print("Excluir Conta Cliente")
        elif opcao == 3:
            print("Consultar Contas Cliente")
        elif opcao == 4:
            print("Cadastrar Empresa")
        elif opcao == 5:
            print("Tchau!")
            break
        else:
            print("Opção inválida!")