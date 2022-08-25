-- mapa
\c dontstarve;
INSERT INTO mapa VALUES (DEFAULT, '1997-08-24', 25, 'p');

-- bioma
INSERT INTO bioma (id, chance_batalha, delta_temp, nome) VALUES (DEFAULT, 0.1, 10, 'floresta');

-- posicaoes
INSERT INTO posicao VALUES (DEFAULT, 1, 1 , NULL, NULL , NULL , NULL,'Voce esta no limite superior da fronteira, onde os mares verdejantes impedem a sua saida da mata');
INSERT INTO posicao VALUES (DEFAULT, 1, 1, NULL, NULL , NULL , NULL,'Você se depara com uma estrada de mao unica, onde observa ao longe um longo exercito marchando em sua procura');
INSERT INTO posicao VALUES (DEFAULT, 1, 1, NULL, NULL , NULL , NULL,'Voce se encontra em uma clareira no meio da mata, na sua frente bem distante tem um mar, e a suas costas uma cadeia de montanha gelidas');
INSERT INTO posicao VALUES (DEFAULT, 1, 1, NULL, NULL , NULL , NULL,'A sua frente você encontra areas interminaveis de vegetação virgem,onde contem muita dificuldade de trafegar');
INSERT INTO posicao VALUES (DEFAULT, 1, 1, NULL, NULL , NULL , NULL,'Voce esta no limite inferior da fronteira, onde as montanhas geladas impedem a sua saida da mata');
UPDATE posicao SET sul = 3 WHERE id=1;
UPDATE posicao SET  oeste = 3 WHERE id=2;
UPDATE posicao SET sul = 5,norte = 1,oeste = 2,leste = 4 WHERE id=3;
UPDATE posicao SET leste = 3 WHERE id=4;
UPDATE posicao SET norte = 3 WHERE id=5;
-- 0 1 0
-- 2 3 4
-- 0 5 0

-- arma
INSERT INTO arma VALUES (DEFAULT, 'Machado', 10, 'Machado tambem é uma arma');

-- ferramenta
INSERT INTO ferramenta VALUES (DEFAULT, 'Picareta', 'bater em pedra', 'Picareta nao é de escrever');
INSERT INTO ferramenta VALUES (DEFAULT, 'Workbench', 'Fazer coisas', 'workbench é de escrever');

-- roupa
INSERT INTO roupa VALUES (DEFAULT, 'Casaco', 10,5,'Casaco de frio');

-- ingrediente
INSERT INTO ingrediente VALUES (DEFAULT, 'cipo', 'ingrediente', 'Uma corda natual!');


-- instancia_item
INSERT INTO instancia_item  VALUES (DEFAULT,1, 'a'); -- machado
INSERT INTO instancia_item  VALUES (DEFAULT,1, 'f'); -- picareta
INSERT INTO instancia_item  VALUES (DEFAULT,2, 'f'); -- workbench
INSERT INTO instancia_item  VALUES (DEFAULT,4, 'r'); -- frio
INSERT INTO instancia_item  VALUES (DEFAULT,1, 'i'); -- cipo

-- instancia_item_posicao
INSERT INTO instancia_item_posicao VALUES (3, 3); -- workbench na posicao 3

-- monstro
INSERT INTO monstro VALUES (DEFAULT,'PernaL ongas',1,'Perna Longas é um monstro',20,1,4);
INSERT INTO monstro VALUES (DEFAULT,'Gato de botas',10,'Gato de botas é um monstro',100,3,5);

-- mochila
INSERT INTO mochila VALUES (1);

-- jogador
INSERT INTO jogador VALUES (DEFAULT, 'Joao',1, 3,NULL,NULL);


-- mochila_guarda_instancia_de_item
INSERT INTO mochila_guarda_instancia_de_item VALUES (1, 5);
INSERT INTO mochila_guarda_instancia_de_item VALUES (1, 5);
INSERT INTO mochila_guarda_instancia_de_item VALUES (1, 5);

-- craft
INSERT INTO craft VALUES (DEFAULT, 5, 3, NULL, NULL, NULL, NULL, 'false', 'Uma corda nao tao natual!');
