CREATE DATABASE cadastro
DEFAULT CHARACTER SET utf8
DEFAULT COLLATE utf8_general_ci;

CREATE TABLE produtos(
    id int NOT NULL AUTO_INCREMENT,
    nome varchar(30) UNIQUE,
    descricao varchar(30),
    categoria varchar(20),
    preco float,
    PRIMARY_KEY(id)
)DEFAULT CHARSET = utf8;
