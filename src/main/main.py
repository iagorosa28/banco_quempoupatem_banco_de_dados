import os
from dotenv import load_dotenv
from supabase import create_client, Client
from printsMenu import prints_menu

# Carrega as variáveis de ambiente
load_dotenv()
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

# Cria a conexão com o Supabase
supabase: Client = create_client(supabase_url, supabase_key)

# Loop principal
print()
print("Bem-vindo(a) ao Banco QuemPoupaTem!!!")
while(True):
    print()
    prints_menu()
    opcao = int(input("Digite uma opção: "))
    if opcao == 1:
        print("Gerente!")
    elif opcao == 2:
        print("Cliente!")
    elif opcao == 3:
        print("Tchau!")
        break
    else:
        print("Opção inválida!")