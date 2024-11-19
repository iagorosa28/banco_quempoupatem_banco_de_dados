# banco_quempoupatem_banco_de_dados

> Status do projeto: Em andamento

> Esse projeto nos foi proposto no 5ºSemestre na disciplina de Banco de Dados

> Escrevemos esse projeto juntos durante as aulas

### Tópicos
🔹[Diagrama Relacional](#straight_ruler-diagrama-relacional)

🔹[Como executar o código](#space_invader-como-executar-o-código)

🔹[Desenvolvedores](#busts_in_silhouette-desenvolvedores)

## :straight_ruler: Diagrama Relacional
### Modelo de Entidade Relacional
```mermaid
erDiagram
    CLIENTE {
    string nome
    string CPF
    int idade
    }

    GERENTE {
    string nome
    string login
    string senha
    }

    CONTA {
    string tipo
    float saldo
    string senha
    }

    DEBITO {
    float valor
    float taxa
    }

    DEPOSITO {
    float valor
    }

    TRANSFERENCIA {

    }

    EXTRATO {
    date data
    time hora
    string tipo_operacao
    string sinal
    float valor
    float taxa
    }

    EMPRESA {
    string nome
    string CNPJ
    float valor_cota
    }

    INVESTIMENTO {
    int quantidade
    }

    CLIENTE  || -- || CONTA : utiliza
    GERENTE  || -- |{ CONTA : gerencia
    CLIENTE  || -- |{ DEBITO : realiza
    CLIENTE  || -- |{ DEPOSITO : realiza_ou_recebe
    DEBITO   || -- || TRANSFERENCIA : realiza
    DEPOSITO || -- || TRANSFERENCIA : reccebe
    CLIENTE  || -- |{ EXTRATO : gera 
    CLIENTE  || -- o{ INVESTIMENTO : realiza
    EMPRESA || -- o{ INVESTIMENTO : recebe
```
### Modelo Relacional na 3FN
```mermaid
classDiagram
    class CLIENTE
    CLIENTE : + int id
    CLIENTE : + string nome
    CLIENTE : + int CPF
    CLIENTE : + int idade

    class GERENTE
    GERENTE : + int id
    GERENTE : + string nome
    GERENTE : + string login
    GERENTE : + string senha

    class CONTA
    CONTA : + int cliente_id
    CONTA : + string tipo
    CONTA : + float saldo
    CONTA : + string senha
    CONTA : + int gerente_id

    class DEBITO
    DEBITO : + int id
    DEBITO : + float valor
    DEBITO : + float taxa
    DEBITO : + int cliente_id

    class DEPOSITO
    DEPOSITO : + int id
    DEPOSITO : + float valor
    DEPOSITO : + int cliente_id

    class TRANSFERENCIA
    TRANSFERENCIA : + int id
    TRANSFERENCIA : + int id_debito
    TRANSFERENCIA : + int id_deposito

    class EXTRATO
    EXTRATO : + int id
    EXTRATO : + date data 
    EXTRATO : + time horario
    EXTRATO : + string tipo_operação
    EXTRATO : + string sinal
    EXTRATO : + float taxa
    EXTRATO : + float valor
    EXTRATO : + int cliente_id
    
    class EMPRESA
    EMPRESA : + int id
    EMPRESA : + string nome
    EMPRESA : + string CNPJ
    EMPRESA : + float valor_cota

    class INVESTIMENTO
    INVESTIMENTO : int cliente_id
    INVESTIMENTO : int empresa_id
    INVESTIMENTO : int quantidade

    CLIENTE "1" --> "1" CONTA : utiliza
    GERENTE "1..*" --> "1..*" CONTA : gerencia
    CLIENTE "1" --> "1..*" DEBITO : realiza
    CLIENTE "1" --> "1..*" DEPOSITO : realiza_ou_reccebe
    DEBITO "1" --> "1" TRANSFERENCIA : realiza
    DEPOSITO "1" --> "1" TRANSFERENCIA : recebe
    CLIENTE "1" --> "1..*" EXTRATO : consulta
    CLIENTE "1..*" --> "0..*" INVESTIMENTO : realiza
    EMPRESA "1..*" --> "0..*" INVESTIMENTO : recebe 
```
## :space_invader: Como executar o código
### Passos Iniciais
**1º PASSO:** Faça um *git clone* do projeto e abra-o preferencialmente no VSCode.

**2º PASSO:** Faça login ou crie uma conta no Supabase. Insira as informações recebidas ao criar a conta (SUPABASE_URL e SUPABASE_KEY) no arquivo `.env`. Isso permitirá que os dados sejam exibidos no seu perfil.

**3º PASSO:** Execute o código presente no arquivo `createTabelas.sql` no Supabase. Este script criará as tabelas necessárias para armazenar os dados.

**4º PASSO:** Execute o arquivo `main.py`. Assim, o código será iniciado e estará pronto para realizar as operações.

### Rodando o Banco

**1ºPASSO:** Ao rodar o arquivo `main.py` deverá aparecer no seu terminal a mensagem da foto abaixo. Logo, que ela aparecer você deverá escolher uma opção.

<div align="center">
   <img width=400 height=250 src="https://github.com/user-attachments/assets/f0e9646f-71f6-4fdf-9f23-5df7a716d98c"/>
</div>

**2ºPASSO:** É recomendamento que primeiro selecione a opção "Gerente", porque, a única pessoa que consegue criar contas é o Gerente e apartir de uma conta criada o cliente consegue acessar e fazer as operações. Portanto, primeiro selecionamos a opção "Gerente" e aparece o seguinte menu:

<div align="center">
   <img width=400 height=250 src="https://github.com/user-attachments/assets/e8553b29-e4f8-4c4f-843c-b664859277cc"/>
</div>

**3ºPASSO:** No primeiro acesso precisa cadastrar um gerente, porque seu banco de dados ainda não possui nenhum cliente cadastrado. Portanto, selecionamos a opção cadastrar, mas quando já possuimos um gerente cadastrado não precisamos realizar esse passo e podemos logar direto. ***DETALHE IMPORTANTE:* Ao fazer algumas operações como cadastrar ou excluir gerente do banco de dados do banco precisamos inserir uma senha que é *15072023*** 

<div align="center">
   <img width=400 height=250 src="https://github.com/user-attachments/assets/a629e141-a3e3-4872-8a7d-033abe30b458"/>
</div>

**4ºPASSO:** Depois de cadastrar um gerente, podemos logar o gerente e logo em seguida aparecerá um menu das operações que ele pode realizar no banco. Como havia dito antes só o gerente pode cadastrar contas, antes de selecionarmos a operação no menu principal cliente é necessário ter um cliente cadastrado por um gerente no banco de dados do banco.

<div align="center">
   <img width=400 height=250 src="https://github.com/user-attachments/assets/432ff0fa-f190-4685-9f0c-a7598588a716"/>
</div>

**5ºPASSO:** Com uma conta criada, podemos selecionar a opção do menu cliente. Lembrando que essa conta criada já está salva no banco de dados, portanto, se fechar e abrir o programa não será necessário cadastrar ela de novo 

<div align="center">
   <img width=400 height=250 src="https://github.com/user-attachments/assets/896d3f15-b779-4018-b794-43202d1d6dd7"/>
</div>

**6ºPASSO:** 

### Realizando Querys



## :busts_in_silhouette: Desenvolvedores
| [<img loading="lazy" src="https://github.com/Mariah-Gomes/ProjetoCompMovel1/assets/141663285/e6827fd1-d8fe-4740-b6fc-fbbfccd05752" width=115><br><sub>Mariah Santos Gomes</sub>](https://github.com/Mariah-Gomes) | [<img loading="lazy" src="https://github.com/Mariah-Gomes/ProjetoCompMovel1/assets/141663285/66d7e656-b9e4-43b7-94fa-931b736df881" width=115><br><sub>Iago Rosa de Oliveira</sub>](https://github.com/iagorosa28) |
| :---: | :---: |

### Dados dos Desenvolvedores
Iago Rosa de Oliveira R.A.: 22.224.027-7

Mariah Santos Gomes R.A.: 22.224.026-8

### Anotações
- Extrato join de todos
- Colocar as datas para todos
- A gnt nn precisa fazer a parte de insert de update, só fazer cadastrar e as 10 operações
