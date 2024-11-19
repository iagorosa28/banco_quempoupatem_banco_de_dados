from config_supabase import supabase
from datetime import datetime
from cliente import registra_extrato

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
    login = input("Insira um login: ")
    verificacaoLogin = consultar_login(login)
    while True:
        if verificacaoLogin == False:
            login = input("Login Incorreto! Digite novamente: ")
            verificacaoLogin = consultar_login(login)
        else:
            break
        
    senha = input("Insira uma senha: ")
    verificacaoSenha = supabase.table("gerente").select("senha").eq("login", login).execute()
    conferindoSenha = verificacaoSenha.data[0]["senha"]
    while True:
        if senha != conferindoSenha:
            senha = input('Senha Incorreta! Digite novamente: ')
            verificacaoSenha = supabase.table("gerente").select("senha").eq("login", login).execute()
        else:
            break

    print("Login Gerente")
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
        print("5. Excluir Empresa")
        print("6. Consultar Empresa")
        print("7. Sair")
        print("---------------")
        opcao = int(input("Digite uma opção: "))
        if opcao == 1:
            criar_conta_c(id_gerente)
        elif opcao == 2:
            excluir_conta_c()
        elif opcao == 3:
            consultar_contas_c()
        elif opcao == 4:
            cadastrar_e()
        elif opcao == 5:
            excluir_e()
        elif opcao == 6:
            consultar_e()
        elif opcao == 7:
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
                    data = datetime.now().strftime("%Y-%m-%d")
                    hora = datetime.now().strftime("%H:%M:%S")
                    registra_extrato(data, hora, "depósito inicial", "+", saldo, 0, id_cliente)
                    print("Conta do cliente criada com sucesso!")
                else:
                    print("Erro ao cadastrar conta: ", resultado_conta.error)    
            else:
                print("Erro ao cadastrar cliente: ", resultado_cliente.error)

# Excluir conta cliente:
def excluir_conta_c():
    print()
    cpf = input("Digite o CPF: ")
    if consultar_cpf(cpf):
        resultado = supabase.table("cliente").delete().eq("cpf", cpf).execute()
        print("Cliente excluido com sucesso!")
    else:
        print("Não existe esse cliente!")

# Consultar contas clientes:
def consultar_contas_c():
    print()
    verificacao = supabase.table("cliente").select("id").execute()
    
    if verificacao.data:
        cont = 0 
        
        resultado = supabase.table("cliente").select("id").execute()
        idS = [cliente["id"] for cliente in resultado.data]
        
        # Quantidade de pessoas
        while cont < len(idS):
            id_cliente = idS[cont]  # ID do cliente atual

            # Consulta dos dados do cliente com base no ID
            cliente = supabase.table("cliente").select("*").eq("id", id_cliente).execute()

            # Consulta da conta do cliente com base no ID
            conta = supabase.table("conta").select("*").eq("id_cliente", id_cliente).execute()
        
            if cliente.data and conta.data:
                cliente_info = cliente.data[0]  # Dados do cliente
                conta_info = conta.data[0]  # Dados da conta

                print(f"Nome: {cliente_info['nome']}")
                print(f"CPF: {cliente_info['cpf']}")
                print(f"Idade: {cliente_info['idade']}")
                print(f"Tipo de conta: {conta_info['tipo']}")
                print(f"Saldo: {conta_info['saldo']}")
                print("-" * 15)  # Separador entre os registros
                
            # Incrementa o contador para a próxima iteração
            cont += 1
    else:
        # Quando não tem cliente cadastrado
        print("O banco não possui clientes")  

# Verifica se o CNPJ que foi digitado bate com algum CNPJ na tabela empresa:
def consultar_cnpj(cnpj):
    resultado = supabase.table("empresa").select("cnpj").eq("cnpj", cnpj).execute()
    if resultado.data:
        return True
    else:
        return False

# Cadastrar empresa:
def cadastrar_e():
    print()
    cnpj = input("Digite O CNPJ: ")
    if consultar_cnpj(cnpj):
        print("Já existe uma empresa com esse CNPJ!")
    else:
        nome = input("Digite o nome: ")
        valor_cota = float(input("Digite o valor da cota: "))
        dados_empresa = {
            "nome": nome,
            "cnpj": cnpj,
            "valor_cota": valor_cota
        }
        # Enviar dados da empresa para o banco de dados:
        resultado_empresa = supabase.table("empresa").insert(dados_empresa).execute()
        if resultado_empresa.data:
            print("Empresa cadastrada com sucesso!")
        else:
            print("Erro ao cadastrar empresa: ", resultado_empresa.error)

# Excluir empresa:
def excluir_e():
    print()
    cnpj = input("Digite o CNPJ: ")
    if consultar_cnpj(cnpj):
        resultado = supabase.table("empresa").delete().eq("cnpj", cnpj).execute()
        print("Empresa excluida com sucesso!")
    else:
        print("Não existe essa empresa!")

# Consultar empresa (roubando o código da Mariah kkkk):
def consultar_e():
    print
    verificacao = supabase.table("empresa").select("id").execute()
    
    if verificacao.data:
        cont = 0 
        
        resultado = supabase.table("empresa").select("id").execute()
        idS = [empresa["id"] for empresa in resultado.data]
        
        # Quantidade de empresas
        while cont < len(idS):
            id_empresa = idS[cont]  # ID da empresa atual

            # Consulta dos dados da empresa com base no ID
            empresa = supabase.table("empresa").select("*").eq("id", id_empresa).execute()
        
            if empresa.data:
                empresa_info = empresa.data[0]  # Dados da empresa

                print(f"Nome: {empresa_info['nome']}")
                print(f"CNPJ: {empresa_info['cnpj']}")
                print(f"Valor cota: {empresa_info['valor_cota']}")
                print("-" * 15)  # Separador entre os registros
                
            # Incrementa o contador para a próxima iteração
            cont += 1
    else:
        # Quando não tem empresa cadastrada
        print("O banco não possui empresas")  