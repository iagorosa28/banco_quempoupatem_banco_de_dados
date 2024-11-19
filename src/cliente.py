from config_supabase import supabase
from datetime import datetime

data = datetime.now().strftime("%Y-%m-%d")
hora = datetime.now().strftime("%H:%M:%S")

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
        print("Depósito realizado com sucesso!")
    else:
        print("Erro ao realizar o depósito!")

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