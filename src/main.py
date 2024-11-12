import os
from dotenv import load_dotenv
from supabase import create_client, Client
from gerente import menu_inicial_g
from cliente import login_c

# Carrega as variáveis de ambiente:
load_dotenv()
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

# Cria a conexão com o Supabase:
supabase: Client = create_client(supabase_url, supabase_key)

# Loop principal:
print()
print("Bem-vindo(a) ao Banco QuemPoupaTem!!!")
while(True):
    print()
    print("Menu: ")
    print("1. Gerente")
    print("2. Cliente")
    print("3. Sair")
    opcao = int(input("Digite uma opção: "))
    if opcao == 1:
        menu_inicial_g()
    elif opcao == 2:
        login_c()
    elif opcao == 3:
        print("Tchau!")
        break
    else:
        print("Opção inválida!")