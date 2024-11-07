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

    CLIENTE || -- || CONTA : utiliza
    CLIENTE || -- |{ DEBITO : realiza
    CLIENTE || -- |{ DEPOSITO : realiza
    CLIENTE || -- |{ TRANSFERENCIA : faz_ou_recebe
    CLIENTE || -- |{ EXTRATO : consulta
    CONTA || -- |{ DEBITO : atualiza
    CONTA || -- |{ DEPOSITO : atualiza
    CONTA || -- |{ TRANSFERENCIA : atualiza
    EXTRATO || -- |{ DEBITO : gera_um_registro
    EXTRATO || -- |{ DEPOSITO : gera_um_registro
    EXTRATO || -- |{ TRANSFERENCIA : gera_um_registro
    GERENTE }| -- || CONTA : gerencia

```
### Modelo Relacional na 3FN

## :space_invader: Como executar o código

## :busts_in_silhouette: Desenvolvedores
| [<img loading="lazy" src="https://github.com/Mariah-Gomes/ProjetoCompMovel1/assets/141663285/e6827fd1-d8fe-4740-b6fc-fbbfccd05752" width=115><br><sub>Mariah Santos Gomes</sub>](https://github.com/Mariah-Gomes) | [<img loading="lazy" src="https://github.com/Mariah-Gomes/ProjetoCompMovel1/assets/141663285/66d7e656-b9e4-43b7-94fa-931b736df881" width=115><br><sub>Iago Rosa de Oliveira</sub>](https://github.com/iagorosa28) |
| :---: | :---: |
