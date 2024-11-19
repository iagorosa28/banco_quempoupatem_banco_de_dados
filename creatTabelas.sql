CREATE SEQUENCE cliente_id_seq;
CREATE TABLE cliente (
  id INT PRIMARY KEY DEFAULT nextval('cliente_id_seq'),
  nome VARCHAR NOT NULL,
  cpf VARCHAR UNIQUE NOT NULL,
  idade INT NOT NULL
);

CREATE SEQUENCE gerente_id_seq;
CREATE TABLE gerente (
  id INT PRIMARY KEY DEFAULT nextval('gerente_id_seq'),
  nome VARCHAR NOT NULL,
  login VARCHAR UNIQUE NOT NULL,
  senha VARCHAR NOT NULL
);

CREATE TABLE conta (  
  id_cliente INT NOT NULL REFERENCES cliente(id) ON DELETE CASCADE,
  tipo VARCHAR NOT NULL,
  saldo FLOAT NOT NULL,
  senha VARCHAR NOT NULL,
  id_gerente INT REFERENCES gerente(id) ON DELETE SET NULL,
  PRIMARY KEY (id_cliente) 
);

CREATE SEQUENCE debito_id_seq;
CREATE TABLE debito(
  id INT PRIMARY KEY DEFAULT nextval('debito_id_seq'),
  valor FLOAT NOT NULL,
  taxa FLOAT NOT NULL,
  id_cliente INT NOT NULL REFERENCES cliente(id) ON DELETE CASCADE
);

CREATE SEQUENCE deposito_id_seq;
CREATE TABLE deposito(
  id INT PRIMARY KEY DEFAULT nextval('deposito_id_seq'),
  valor FLOAT NOT NULL,
  id_cliente INT NOT NULL REFERENCES cliente(id) ON DELETE CASCADE
);

CREATE SEQUENCE transferencia_id_seq;
CREATE TABLE transferencia(
  id INT PRIMARY KEY DEFAULT nextval('transferencia_id_seq'),
  id_debito INT UNIQUE REFERENCES debito(id) ON DELETE SET NULL,
  id_deposito INT UNIQUE REFERENCES deposito(id) ON DELETE SET NULL
);

CREATE SEQUENCE extrato_id_seq;
CREATE TABLE extrato(
  id INT PRIMARY KEY DEFAULT nextval('extrato_id_seq'),
  data DATE NOT NULL,
  hora TIME NOT NULL,
  tipo_operacao VARCHAR NOT NULL,
  sinal VARCHAR NOT NULL,
  valor FLOAT NOT NULL,
  taxa FLOAT NOT NULL,
  id_cliente INT NOT NULL REFERENCES cliente(id) ON DELETE CASCADE
)

CREATE SEQUENCE empresa_id_seq;
CREATE TABLE empresa (
  id INT PRIMARY KEY DEFAULT nextval('empresa_id_seq'),
  nome VARCHAR NOT NULL,
  cnpj VARCHAR UNIQUE NOT NULL,
  valor_cota FLOAT NOT NULL
);

CREATE TABLE investimento (
  id_cliente INT NOT NULL REFERENCES cliente(id) ON DELETE CASCADE,
  id_empresa INT NOT NULL REFERENCES empresa(id) ON DELETE CASCADE,
  quantidade INT NOT NULL,
  PRIMARY KEY (id_cliente, id_empresa) 
)