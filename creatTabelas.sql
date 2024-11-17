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
  id_gerente INT NOT NULL REFERENCES gerente(id),
  PRIMARY KEY (id_cliente) 
);

CREATE SEQUENCE debito_id_seq;
CREATE TABLE debito(
  id INT PRIMARY KEY DEFAULT nextval('debito_id_seq'),
  valor FLOAT NOT NULL,
  taxa FLOAT NOT NULL,
  data DATE NOT NULL,
  hora TIME NOT NULL,
  id_cliente INT NOT NULL REFERENCES cliente(id)
);

CREATE SEQUENCE deposito_id_seq;
CREATE TABLE deposito(
  id INT PRIMARY KEY DEFAULT nextval('deposito_id_seq'),
  valor FLOAT NOT NULL,
  data DATE NOT NULL,
  hora TIME NOT NULL,
  id_cliente INT NOT NULL REFERENCES cliente(id)
);

CREATE SEQUENCE transferencia_id_seq;
CREATE TABLE transferencia(
  id INT PRIMARY KEY DEFAULT nextval('transferencia_id_seq'),
  id_debito INT NOT NULL UNIQUE REFERENCES debito(id) ON DELETE CASCADE,
  id_deposito INT NOT NULL UNIQUE REFERENCES deposito(id) ON DELETE CASCADE
);

--EXTRATO

CREATE SEQUENCE empresa_id_seq;
CREATE TABLE empresa (
  id INT PRIMARY KEY DEFAULT nextval('empresa_id_seq'),
  nome VARCHAR NOT NULL,
  cnpj VARCHAR UNIQUE NOT NULL,
  valor_cota FLOAT NOT NULL
);

CREATE TABLE investimento (
  id_cliente INT NOT NULL REFERENCES cliente(id),
  id_empresa INT NOT NULL REFERENCES empresa(id),
  quantidade INT NOT NULL,
  PRIMARY KEY (id_cliente, id_empresa) 
)