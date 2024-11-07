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
    string tipo de conta
    float valor
    int senha
    date data de criação
    time hora de criação
    }

    DÉBITO {
    float valor
    float taxa
    date data de pagamento
    time hora de pagamento
    }

    DEPÓSITO {
    float valor
    date data de recebimento
    time hora de recebimento
    }

    TRANSFERÊNCIA {
    float taxa
    float valor
    date data de pagamento
    time hora de pagamento
    date data de recebimento
    time hora de recebimento
    }

    EXTRATO {
    float taxa
    float valor
    string tipo da operação 
    date data da operação
    time horário da operação
    }

    GERENTE }| -- || CONTA : gerencia
    CLIENTE || -- || CONTA : utiliza
    CLIENTE || -- |{ DÉBITO : realiza
    CLIENTE || -- |{ DEPÓSITO : realiza
    CLIENTE || -- |{ TRANSFERÊNCIA : faz ou recebe
    CLIENTE || -- |{ EXTRATO : consulta
    CONTA || -- |{ DÉBITO : atualiza
    CONTA || -- |{ DEPÓSITO : atualiza
    CONTA || -- |{ TRANSFERÊNCIA : atualiza
    EXTRATO || -- |{ DÉBITO : gera um registro
    EXTRATO || -- |{ DEPÓSITO : gera um registro
    EXTRATO || -- |{ TRANSFERÊNCIA : gera um registro

```
