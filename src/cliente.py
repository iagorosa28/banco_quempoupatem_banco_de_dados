from config_supabase import supabase
from datetime import datetime

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
    id_cliente = resultado.data[0]["id"]  # Obtém o cliente do gerente.
    # Chama o menu do cliente com o ID.    
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
            consultar_saldo(id_cliente)
        elif opcao == 2:
            debito(id_cliente)
        elif opcao == 3:
            deposito(id_cliente)
        elif opcao == 4:
            transferencia(id_cliente)
        elif opcao == 5:
            extrato(id_cliente)
        elif opcao == 6:
            investimentos(id_cliente)
        elif opcao == 7:
            print("Tchau!")
            break
        else:
            print("Opção inválida!")

# Consultar saldo:
def consultar_saldo(id_cliente):
    print()
    resultadoConta = supabase.table("conta").select("saldo").eq("id_cliente", id_cliente).execute()
    conta = resultadoConta.data[0]  # Pegando a primeira conta
    print(f"Saldo: {conta['saldo']}")


# Realizando cálculos de taxa:
def taxa_calc(id_cliente, valor):
    resultado_conta = supabase.table("conta").select("tipo").eq("id_cliente", id_cliente).execute()
    tipo_conta = resultado_conta.data[0]["tipo"]
    taxa = 0
    if tipo_conta == "normal":
        taxa = 0.05
    elif tipo_conta == "plus":
        taxa = 0.03
    return valor * taxa

# Realizando cálculos de débito:
def debitando(id_cliente, valor, valor_taxa):
    resultado_conta = supabase.table("conta").select("saldo").eq("id_cliente", id_cliente).execute()
    saldo = float(resultado_conta.data[0]["saldo"])

    valor_final = valor + valor_taxa
    saldo_final = saldo - valor_final

    dados_debito = {
        "valor": valor,
        "taxa": valor_taxa,
        "id_cliente": id_cliente
    }
    resultado_saldo_final = supabase.table("conta").update({"saldo": saldo_final}).eq("id_cliente", id_cliente).execute()
    if resultado_saldo_final.data:
        resultado_debito = supabase.table("debito").insert(dados_debito).execute()
        if resultado_debito.data:
            return resultado_debito.data[0].get("id")
    return None

# Débito:
def debito(id_cliente):
    print()
    valor = float(input("Digite o valor do débito: "))
    valor_taxa = taxa_calc(id_cliente, valor)
    resultado = debitando(id_cliente, valor, valor_taxa)
    if resultado:
        data = datetime.now().strftime("%Y-%m-%d")
        hora = datetime.now().strftime("%H:%M:%S")
        registra_extrato(data, hora, "débito", "-", valor, valor_taxa, id_cliente)
        print("Débito realizado com sucesso!")
    else:
        print("Erro ao realizar o débito!")


# Realizando cálculos de depósito:
def depositando(id_cliente, valor):
    resultado_saldo = supabase.table("conta").select("saldo").eq("id_cliente", id_cliente).execute()
    saldo = float(resultado_saldo.data[0]["saldo"])

    saldo_final = saldo + valor

    dados_deposito = {
        "valor": valor,
        "id_cliente": id_cliente
    }
    resultado_saldo_final = supabase.table("conta").update({"saldo": saldo_final}).eq("id_cliente", id_cliente).execute()
    if resultado_saldo_final.data:
        resultado_deposito = supabase.table("deposito").insert(dados_deposito).execute()
        if resultado_deposito.data:
            return resultado_deposito.data[0].get("id")
    return None

# Depósito:
def deposito(id_cliente):
    print()
    valor = float(input("Digite o valor do depósito: "))
    resultado = depositando(id_cliente, valor)
    if resultado:
        data = datetime.now().strftime("%Y-%m-%d")
        hora = datetime.now().strftime("%H:%M:%S")
        registra_extrato(data, hora, "depósito", "+", valor, 0, id_cliente)
        print("Depósito realizado com sucesso!")
    else:
        print("Erro ao realizar o depósito!")

# Transferência:
def transferencia(id_cliente):
    print()
    cpf_destino = input("Digite o CPF do destino: ")
    # Verifica a existência da conta destino:
    resultado_cpf = supabase.table("cliente").select("id").eq("cpf", cpf_destino).execute()
    if resultado_cpf.data:
        # Pega o ID da conta destino:
        id_destino = int(resultado_cpf.data[0]["id"])
        valor = float(input("Digite o valor da transferência: "))
        valor_taxa = taxa_calc(id_cliente, valor)
        # Realiza o débito da conta origem:
        resultado_debito = debitando(id_cliente, valor, valor_taxa)
        if resultado_debito:
            # Realiza o depósito na conta destino:
            resultado_deposito = depositando(id_destino, valor)
            if resultado_deposito:
                dados_transferencia = {
                    "id_debito": resultado_debito,
                    "id_deposito": resultado_deposito
                }
                # Junta os IDs de débito e depóstio das contas origem e destino para registrar uma transferência:
                resultado_transferencia = supabase.table("transferencia").insert(dados_transferencia).execute()
                if resultado_transferencia.data:
                    data = datetime.now().strftime("%Y-%m-%d")
                    hora = datetime.now().strftime("%H:%M:%S")
                    registra_extrato(data, hora, "transferência", "-", valor, valor_taxa, id_cliente)
                    registra_extrato(data, hora, "transferência", "+", valor, 0, id_destino)
                    print("Transferência realizada com sucesso!")
                else:
                    print("Erro ao realizar a transferência")
            else:
                print("Erro ao depositar valor na conta destino!")
        else:
            print("Erro ao debitar valor da conta origem!")
    else:
        print("Conta destino não encontrada!")


# Realiza registros de extrato:
def registra_extrato(data, hora, tipo_operacao, sinal, valor, taxa, id_cliente):
    dados_registro = {
        "data": data,
        "hora": hora,
        "tipo_operacao": tipo_operacao,
        "sinal": sinal,
        "valor": valor,
        "taxa": taxa,
        "id_cliente": id_cliente
    }
    resultado_registro = supabase.table("extrato").insert(dados_registro).execute()

# Extrato:
def extrato(id_cliente):
    print()
    dados = supabase.table("extrato").select("*").eq("id_cliente", id_cliente).execute()
    for extrato in dados.data:
        print("-" * 15)  # Separador entre os registros
        print(f"Data: {extrato['data']}, Horário: {extrato['hora']}, Tipo: {extrato['tipo_operacao']}, "
              f"Valor: {extrato['sinal']} R$ {float(extrato['valor']):.2f}, Taxa: {float(extrato['taxa']):.2f}")
    print("-" * 15)  # Separador entre os registros

# Menu investimentos:
def investimentos(id_cliente):
    print()
    print("Área Investimentos")
    while(True):
        print()
        print("---------------")
        print("Menu Investimentos: ")
        print("1. Listar Empresas")
        print("2. Comprar Cotas")
        print("3. Vender Cotas")
        print("4. Meus Investimentos")
        print("5. Sair")
        print("---------------")
        opcao = int(input("Digite uma opção: "))
        if opcao == 1:
            listar_e()
        elif opcao == 2:
            comprar_cotas(id_cliente)
        elif opcao == 3:
            print("FODA-SE")
        elif opcao == 4:
            print("FODA-SE")
        elif opcao == 5:
            print("Tchau!")
            break
        else:
            print("Opção inválida!")

# Listar empresas (como não consegui importar do gerente eu colei aqui tbm):
def listar_e():
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

                print()
                print("-" * 15)  # Separador entre os registros
                print(f"Nome: {empresa_info['nome']}")
                print(f"CNPJ: {empresa_info['cnpj']}")
                print(f"Valor cota: {empresa_info['valor_cota']}")
                print("-" * 15)  # Separador entre os registros
                
            # Incrementa o contador para a próxima iteração
            cont += 1
    else:
        # Quando não tem empresa cadastrada
        print("O banco não possui empresas")  

# Realizando cálculos para comprar cotas:
def investindo(id_cliente, id_empresa, qtde):
    resultado_conta = supabase.table("conta").select("saldo").eq("id_cliente", id_cliente).execute()
    resultado_empresa = supabase.table("empresa").select("valor_cota").eq("id", id_empresa).execute()
    saldo = float(resultado_conta.data[0]["saldo"])
    valor_cota = float(resultado_empresa.data[0]["valor_cota"])

    valor_compra = qtde * valor_cota
    saldo_final = saldo - valor_compra
    valor_cota_final = valor_cota + (0.01*qtde)

    resultado_saldo_final = supabase.table("conta").update({"saldo": saldo_final}).eq("id_cliente", id_cliente).execute()
    if resultado_saldo_final.data:
        resultado_valor_cota = supabase.table("empresa").update({"valor_cota": valor_cota_final}).eq("id", id_empresa).execute()
        if resultado_valor_cota.data:
            dados_investimento = {
                "id_cliente": id_cliente,
                "id_empresa": id_empresa,
                "quantidade": qtde
            }
            resultado_investimento = supabase.table("investimento").insert(dados_investimento).execute()
            if resultado_investimento.data:
                return valor_compra
    return None

# Comprar cotas:
def comprar_cotas(id_cliente):
    print()
    cnpj_empresa = input("Digite o CNPJ da empresa: ")
    resultado_cnpj = supabase.table("empresa").select("id").eq("cnpj", cnpj_empresa).execute()
    if resultado_cnpj.data:
        id_empresa = int(resultado_cnpj.data[0]["id"])
        qtde = int(input("Digite a quantidade de cotas que deseja comprar: "))
        valor_investimento = investindo(id_cliente, id_empresa, qtde)
        if valor_investimento:
            data = datetime.now().strftime("%Y-%m-%d")
            hora = datetime.now().strftime("%H:%M:%S")
            registra_extrato(data, hora, "compra de cota(s)", "-", valor_investimento, 0, id_cliente)
            print("Investimento realizado com sucesso!")
        else:
            print("Falha ao investir!")
    else:
        print("Empresa não encontrada!")