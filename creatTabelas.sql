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
  tipo VARCHAR NOT NULL,
  saldo FLOAT NOT NULL,
  senha VARCHAR NOT NULL,
  id_cliente INT NOT NULL REFERENCES cliente(id),
  id_gerente INT NOT NULL REFERENCES gerente(id),
  PRIMARY KEY (id_cliente, id_gerente) 
);