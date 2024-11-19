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
    TRANSFERENCIA : + float taxa
    TRANSFERENCIA : + float valor
    TRANSFERENCIA : + date data de pagamento
    TRANSFERENCIA : + time hora de pagamento
    TRANSFERENCIA : + date data de recebimento
    TRANSFERENCIA : + time hora de recebimento

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
    CLIENTE "1" --> "1..*" DEPOSITO : realiza
    DEBITO "1" --> "1" TRANSFERENCIA : nsei
    DEPOSITO "1" --> "1" TRANSFERENCIA : nsei
    CLIENTE "1" --> "1..*" EXTRATO : consulta
    CLIENTE "1..*" --> "1..*" EMPRESA : nsei
    
    %%CLIENTE "1" --> "1..*" TRANSFERÊNCIA : faz_ou_recebe
    
    %%CONTA "1" --> "1..*" DÉBITO : atualiza
    %%CONTA "1" --> "1..*" DEPÓSITO : atualiza
    %%CONTA "1" --> "1..*" TRANSFERÊNCIA : atualiza
    %%EXTRATO "1" --> "1..*" DÉBITO : gera_um_registro
    %%EXTRATO "1" --> "1..*" DEPÓSITO : gera_um_registro
    %%EXTRATO "1" --> "1..*" TRANSFERÊNCIA : gera_um_registro
    
```
## :space_invader: Como executar o código

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
