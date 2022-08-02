CREATE DATABASE dontstave;
\c dontstave;

DROP TABLE IF EXISTS mapa;
DROP TABLE IF EXISTS bioma;
DROP TABLE IF EXISTS posicao;
DROP TABLE IF EXISTS instancia_item;
DROP TABLE IF EXISTS instancia_item_posicao;
DROP TABLE IF EXISTS monstro;
DROP TABLE IF EXISTS jogador;
DROP TABLE IF EXISTS mochila;
DROP TABLE IF EXISTS especializacao_do_item;
DROP TABLE IF EXISTS arma;
DROP TABLE IF EXISTS ferramenta;
DROP TABLE IF EXISTS roupa;
Drop TABLE IF EXISTS ingrediente;
DROP TABLE IF EXISTS mochila_guarda_instancia_de_item;
DROP TABLE IF EXISTS craft;

CREATE DOMAIN texto AS VARCHAR(50) NOT NULL;
CREATE DOMAIN descricao AS VARCHAR(300) NOT NULL;

CREATE TABLE mapa(
    id SERIAL,
    dia Date,
    temp INT,
    estacao varchar(1) NOT NULL CHECK(estacao IN('p', 'v', 'o', 'i')),
    CONSTRAINT mapa_pk PRIMARY KEY(id)
);


CREATE TABLE bioma(
    id SERIAL,
    chance_batalha INT NOT NULL,
    delta_temp INT NOT NULL,
    nome texto NOT NULL,
    CONSTRAINT bioma_pk PRIMARY KEY(id)
);


CREATE TABLE posicao (
    id SERIAL,
    id_mapa INT NOT NULL,
    bioma INT NOT NULL,
    norte INT,
    sul INT,
    leste INT,
    oeste INT,
    descricao descricao,
    CONSTRAINT posicao_pk PRIMARY KEY(id),
    CONSTRAINT norte_posicao_fk FOREIGN KEY(norte) REFERENCES posicao(id),
    CONSTRAINT sul_posicao_fk FOREIGN KEY(sul) REFERENCES posicao(id),
    CONSTRAINT leste_posicao_fk FOREIGN KEY(leste) REFERENCES posicao(id),
    CONSTRAINT oeste_posicao_fk FOREIGN KEY(oeste) REFERENCES posicao(id),
    CONSTRAINT bioma_fk FOREIGN KEY(bioma) REFERENCES bioma(id),
    CONSTRAINT id_mapa_fk FOREIGN KEY(id_mapa) REFERENCES mapa(id)
);

CREATE TABLE instancia_item(
    id SERIAL,
    id_item INT NOT NULL,
    tipo varchar(1) NOT NULL CHECK(tipo IN('a', 'f', 'r', 'i')),
    CONSTRAINT instancia_item_pk PRIMARY KEY(id)
);

CREATE TABLE instancia_item_posicao(
    id_posicao INT NOT NULL,
    id_instancia_item INT NOT NULL, 
    CONSTRAINT instancia_item_posicao_pk PRIMARY KEY(id_posicao),
    CONSTRAINT instancia_item_posicao_sk UNIQUE(id_instancia_item),
    CONSTRAINT id_posicao_instancia_item_posicao_fk FOREIGN KEY(id_posicao) REFERENCES posicao(id),
    CONSTRAINT id_instancia_instancia_item_posicao_fk FOREIGN KEY(id_instancia_item) REFERENCES instancia_item(id)
);

-- INSERT INTO monstro (id, nome, dano, descricao,vida,isca,id_posicao) VALUES (DEFAULT,Pumba,10,'Pumba é um monstro',100,false,1);
CREATE TABLE monstro(
    id SERIAL,
    nome texto NOT NULL,
    dano INT NOT NULL,
    descricao descricao NOT NULL,
    vida INT NOT NULL,
    isca INT NOT NULL,
    id_posicao INT NOT NULL,
    CONSTRAINT monstro_pk PRIMARY KEY(id),
    CONSTRAINT id_posicao_monstro_fk FOREIGN KEY(id_posicao) REFERENCES posicao(id)
);

CREATE TABLE mochila(
    id SERIAL,
    CONSTRAINT mochila_pk PRIMARY KEY(id)
);

-- INSERT INT jogador (id, nome, id_posicao, id_roupa_equipada, id_item_equipado) VALUES (DEFAULT, 'João', 1, 1, 1);
CREATE TABLE jogador(
    id SERIAL,
    nome texto,
    id_mochila INT,
    id_posicao INT NOT NULL,
    id_roupa_equipada INT , -- Triger and storage.
    id_item_equipado INT, -- Triger and storage.
    CONSTRAINT jogador_pk PRIMARY KEY(id),
    CONSTRAINT id_posicao_jogador_fk FOREIGN KEY(id_posicao) REFERENCES posicao(id),
    CONSTRAINT id_mochila_jogador_fk FOREIGN KEY(id_mochila) REFERENCES mochila(id),
     CONSTRAINT id_equipada_jogador_fk FOREIGN KEY(id_item_equipado) REFERENCES instancia_item(id),
    CONSTRAINT id_roupa_equipada_fk FOREIGN KEY(id_roupa_equipada) REFERENCES instancia_item(id)
);
-- INSERT INTO mochila (id, id_jogador) VALUES (DEFAULT, 1);


CREATE TABLE arma(
    id SERIAL,
    dano INT NOT NULL,
    nome texto NOT NULL,
    descricao descricao NOT NULL,
    CONSTRAINT arma_pk PRIMARY KEY(id),
    CONSTRAINT nome_arma_sk UNIQUE(nome)
);


CREATE TABLE ferramenta(
    id SERIAL,
    nome texto,
    funcao texto,
    descricao descricao NOT NULL,
    CONSTRAINT ferramenta_pk PRIMARY KEY(id),
    CONSTRAINT nome_ferramenta_sk UNIQUE(nome)
);


CREATE TABLE roupa(
    id SERIAL,
    nome texto NOT NULL,
    protecao_termica INT NOT NULL,
    protecao_fisica INT NOT NULL,
    descricao descricao NOT NULL,
    CONSTRAINT roupa_pk PRIMARY KEY(id),
    CONSTRAINT nome_roupa_sk UNIQUE(nome)
);

CREATE TABLE ingrediente(
    id Serial,
    nome texto NOT NULL,
    funcao texto NOT NULL,
    descricao descricao NOT NULL,
    CONSTRAINT ingrediente_pk PRIMARY KEY(id),
    CONSTRAINT nome_ingrediente_sk UNIQUE(nome)
);

CREATE TABLE mochila_guarda_instancia_de_item(
    id_mochila INT NOT NULL,
    id_instancia_item INT,
    CONSTRAINT id_instancia_de_item_mochila_guarda_fk FOREIGN KEY(id_mochila) REFERENCES mochila(id),
    CONSTRAINT id_mochila_guarda_instancia_de_item_fk FOREIGN KEY(id_instancia_item)REFERENCES instancia_item(id)
);

CREATE TABLE craft(
    id SERIAL,
    id_item1 INT,
    quant_item1 INT,
    id_item2 INT,
    quant_item2 INT,
    id_item3 INT,
    quant_item3 INT,
    necessita_workbench BOOLEAN,
    descricao descricao NOT NULL,
    CONSTRAINT craft_pk PRIMARY KEY(id),
    CONSTRAINT id_item1_fk FOREIGN KEY(id_item1) REFERENCES instancia_item(id),
    CONSTRAINT id_item2_fk FOREIGN KEY(id_item2) REFERENCES instancia_item(id),
    CONSTRAINT id_item3_fk FOREIGN KEY(id_item3) REFERENCES instancia_item(id)
);
