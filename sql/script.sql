create database inclusion;
use inclusion;

create table usuarios (
    id int primary key auto_increment,
    nome varchar(255),
    email varchar(255) not null unique,
    senha varchar(255) not null,
    foto LONGBLOB,
    adm boolean
);

CREATE TABLE mensagens (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    mensagem VARCHAR(255),
    aprovada BOOLEAN
);

CREATE TABLE profissionais (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    telefone CHAR(11),
    especialidade VARCHAR(255),
    cidade VARCHAR(255),
    estado VARCHAR(255),
    aprovado BOOLEAN
);