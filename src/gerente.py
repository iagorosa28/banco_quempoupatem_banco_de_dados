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
            login_g()
        elif opcao == 3:
            excluir_g()
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

# Login do gerente:
def login_g():
    print()
    print("Login Gerente")
    # implementar login aqui (Mariah).
    # se o login for concluído -> então chamar a função menu_g.
    # tem que guardar o id do gerente que está logando e passar como parâmetro na função menu gerente.
    # exemplo mais ou menos de como você tem que fazer: 
    login = "iagorosa28"
    resultado = supabase.table("gerente").select("id").eq("login", login).execute()
    id_gerente = resultado.data[0]["id"]  # Obtém o ID do gerente.
    menu_g(id_gerente)  # Chama o menu do gerente com o ID.

# Excluir gerente:
def excluir_g():
    print()
    chave_acesso = int(input("Digite a chave de acesso do banco: "))
    if chave_acesso == n_acesso:
        login = input("Insira o login do gerente que deseja excluir: ")
        consulta = consultar_login(login)
        if consulta:
            # Exclui o gerente pelo login no banco de dados: 
            resultado = supabase.table("gerente").delete().eq("login", login).execute()
            print("Gerente excluido com sucesso!")
        else:
            print("Login inexistente!")
    else:
        print("Chave de acesso incorreta!")

# Menu gerente:
def menu_g(id_gerente):
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
            criar_conta_c(id_gerente)
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

# Verifica se o CPF que foi digitado bate com algum CPF na tabela cliente:
def consultar_cpf(cpf):
    resultado = supabase.table("cliente").select("cpf").eq("cpf", cpf).execute()
    if resultado.data:
        return True
    else:
        return False

# Criar conta cliente:
def criar_conta_c(id_gerente):
    print()
    cpf = input("Digite o CPF: ")
    if consultar_cpf(cpf):
        print("Já existe uma conta com esse CPF!")
    else:
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        if idade < 18:
            conta = "estudante"
        else:
            conta = input("Digite o tipo de conta (normal ou plus): ")
            while conta != "normal" and conta != "plus":
                conta = input("Digite um tipo de conta existente (normal ou plus): ") 
            saldo = float(input("Digite o saldo inicial: "))
            while saldo < 0:
                saldo = float(input("Digite o saldo inicial com valores >= 0:"))
            senha = input("Digite a senha: ")
            dados_cliente = {
            "nome": nome,
            "cpf": cpf,
            "idade": idade
            }
            # Insere os dados no banco de dados:
            resultado_cliente = supabase.table("cliente").insert(dados_cliente).execute()
            # Verifica se os dados foram inseridos com sucesso:
            if resultado_cliente.data:
                consulta_id_cliente = supabase.table("cliente").select("id").eq("cpf", cpf).execute() # Consultando ID do cliente.
                id_cliente = consulta_id_cliente.data[0]["id"] # Obtém o ID do cliente.
                dados_conta = {
                    "id_cliente": id_cliente,
                    "tipo": conta,
                    "saldo": saldo,
                    "senha": senha,
                    "id_gerente": id_gerente
                }
                # Insere os dados no banco de dados:
                resultado_conta = supabase.table("conta").insert(dados_conta).execute()
                # Verifica se os dados foram inseridos com sucesso:
                if resultado_conta.data:
                    print("Conta do cliente criada com sucesso!")
                else:
                    print("Erro ao cadastrar conta: ", resultado_conta.error)    
            else:
                print("Erro ao cadastrar cliente: ", resultado_cliente.error)