# banco_quempoupatem_banco_de_dados
```mermaid
erDiagram
    CLIENTE {
    string nome
    int CPF
    int idade
    }

    GERENTE {
    string nome
    string login
    int senha
    }

    CONTA {
    string tipoDeConta
    float valor
    int senha
    date dataDeCriacao
    time horaDeCriacao
    }

    DEBITO {
    float valor
    float taxa
    date dataDePagamento
    time horaDePagamento
    }

    DEPOSITO {
    float valor
    date dataDeRecebimento
    time horaDeRecebimento
    }

    TRANSFERENCIA {
    float taxa
    float valor
    date dataDePagamento
    time horaDePagamento
    date dataDeRecebimento
    time horaDeRecebimento
    }

    EXTRATO {
    float taxa
    float valor
    string tipoDaOperacao 
    date dataDaOperacao
    time horarioDaOperacao
    }

    GERENTE }| -- || CONTA : gerencia
    CLIENTE || -- || CONTA : utiliza
    CLIENTE || -- |{ DEBITO : realiza
    CLIENTE || -- |{ DEPOSITO : realiza
    CLIENTE || -- |{ TRANSFERENCIA : faz ou recebe
    CLIENTE || -- |{ EXTRATO : consulta
    CONTA || -- |{ DEBITO : atualiza
    CONTA || -- |{ DEPOSITO : atualiza
    CONTA || -- |{ TRANSFERENCIA : atualiza
    EXTRATO || -- |{ DEBITO : gera um registro
    EXTRATO || -- |{ DEPOSITO : gera um registro
    EXTRATO || -- |{ TRANSFERENCIA : gera um registro

```
