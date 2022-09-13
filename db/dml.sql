-- SQLBook: Code
-- mapa
\c dontstarve;
INSERT INTO mapa VALUES (DEFAULT, '1997-08-24', 25, 'p');

-- bioma
INSERT INTO bioma (id, chance_batalha, delta_temp, nome) VALUES (DEFAULT, 0.1, 5, 'floresta');

INSERT INTO bioma (id, chance_batalha, delta_temp, nome) VALUES (DEFAULT, 0.2, 10, 'pantano');

INSERT INTO bioma (id, chance_batalha, delta_temp, nome) VALUES (DEFAULT, 0.4, 20, 'deserto');

INSERT INTO bioma (id, chance_batalha, delta_temp, nome) VALUES (DEFAULT, 0.6, -20, 'Tundra');
INSERT INTO bioma (id, chance_batalha, delta_temp, nome) VALUES (DEFAULT, 0.0, 0, 'Ponte');
INSERT INTO bioma (id, chance_batalha, delta_temp, nome) VALUES (DEFAULT, 1.0, 0, 'Rio');

-- posicaoes
INSERT INTO posicao VALUES (1,1, 3, NULL, 10, 2, NULL, 'O jogador se encontra no fim da ilha, unico caminho póssivel se encontra a sul ou leste',4,0);
INSERT INTO posicao VALUES (2,1, 3, NULL, 11, 3, 1,'O jogador está na beira do fim da ilha ao norte ele vê nada além de vazio',4,0);
INSERT INTO posicao VALUES (3,1, 3, NULL, 12, 4, 2, 'O jogador está na beira do fim da ilha ao norte ele vê nada além de vazio',4,0);
INSERT INTO posicao VALUES (4,1, 3, NULL, 13, NULL, 3, 'Ao norte é possivel ver somente o fim da ilha, ao leste um rio intransponível dê meia volta',4,0);
INSERT INTO posicao VALUES (5,1, 6, NULL, NULL, NULL, NULL, 'nesta posição existe um rio intransponível  de cor escura. não há nada para se fazer aqui',4,0);
INSERT INTO posicao VALUES (6,1, 4, NULL, 15, 7, NULL, 'Ao norte é possivel ver somente o fim da ilha, ao oeste um rio intransponível dê meia volta',1,3);
INSERT INTO posicao VALUES (7,1, 4, NULL, 16, 8, 6, 'O jogador está na beira do fim da ilha, ao norte ele vê nada além de vazio',1,3);
INSERT INTO posicao VALUES (8,1, 4, NULL, 17, 9, 7, 'O jogador está na beira do fim da ilha, ao norte ele vê nada além de vazio',1,3);
INSERT INTO posicao VALUES (9,1, 4, NULL, 18, NULL, 8, 'O jogador se encontra no fim da ilha, unico caminho póssivel se encontra a sul ou oeste',1,3);
INSERT INTO posicao VALUES (10,1, 3, 1, 19, 11, NULL, 'O jogar se encontra em um empasse, a oeste ele encontrar nada além de escuridão e resolve não seguir por ali',5,0);
INSERT INTO posicao VALUES (11,1, 3, 2, 20, 12, 10, 'Aqui jaz um deserto escaldante que não possui nada além de areia e animais peçonhentos.',5,0);
INSERT INTO posicao VALUES (12,1, 3, 3, 21, 13, 11, 'Aqui jaz um deserto escaldante que não possui nada além de areia e animais peçonhentos.',5,0);
INSERT INTO posicao VALUES (13,1, 3, 4, 22, NULL, 12, 'ao oeste existe uma ponte velha, pode ser que aguente você passar',5,0);
INSERT INTO posicao VALUES (14,1, 5, NULL, NULL, 13, 15, 'nesta posição existe uma ponte que não está em boas condições, seja rapido em sua pericia e avance logo em dia direção desejada. não se sabe quanto tempo ela irá aguentar seu peso sobre a ponte durar.',0,0);
INSERT INTO posicao VALUES (15,1, 5, 6, 24, 16, 14, 'ao leste existe uma ponte velha, pode ser que aguente você passar',2,2);
INSERT INTO posicao VALUES (16,1, 4, 7, 25, 17, 15, 'O gelo toma conta de tudo ao seu redor, tendo dificuldade inclusive de observar ao seu redor.',2,2);
INSERT INTO posicao VALUES (17,1, 4, 8, 26, 18, 16, 'O gelo toma conta de tudo ao seu redor, tendo dificuldade inclusive de observar ao seu redor.',2,2);
INSERT INTO posicao VALUES (18,1, 4, 9, 27, NULL, 17, 'a leste é possivel ver um penhasco extremamente profundo é melhor não ir por ali',2,2);
INSERT INTO posicao VALUES (19,1, 3, 10, 28, 20, NULL, 'O jogar se encontra em um empasse, a oeste ele encontrar nada além de escuridão e resolve não seguir por ali, mas na sua localização você encontra a caverna , lotada de recurso o mordomo do local chamado Alfred lhe deixa coletar pra ajudar na jornada',20,20);
INSERT INTO posicao VALUES (20,1, 3, 11, 29, 21, 19, 'Aqui jaz um deserto escaldante que não possui nada além de areia e animais peçonhentos.',4,1);
INSERT INTO posicao VALUES (21,1, 3, 12, 30, 22, 20, 'Aqui jaz um deserto escaldante que não possui nada além de areia e animais peçonhentos.',4,1);
INSERT INTO posicao VALUES (22,1, 3, 13, 31, NULL, 21, 'A leste existe um rio intransponivel é impossivel passar por ali, ache outro caminho, talvez exista uma ponte',4,1);
INSERT INTO posicao VALUES (23,1, 6, NULL, NULL, NULL, NULL, 'nesta posição existe um rio intransponível  de cor escura. não há nada para se fazer aqui',0,0);
INSERT INTO posicao VALUES (24,1, 4, 15, 33, 25, NULL, 'Voce encontra o rio que cerca a ilha por não saber nadar resolve não ir a oeste',2,1);
INSERT INTO posicao VALUES (25,1, 4, 16, 34, 26, 24, 'O gelo toma conta de tudo ao seu redor, tendo dificuldade inclusive de observar ao seu redor.',2,1);
INSERT INTO posicao VALUES (26,1, 4, 17, 35, 27, 25, 'O gelo toma conta de tudo ao seu redor, tendo dificuldade inclusive de observar ao seu redor.',2,1);
INSERT INTO posicao VALUES (27,1, 4, 18, 36, NULL, 26, 'a leste é possivel ver um penhasco extremamente profundo é melhor não ir por ali,talvez exista uma ponte',2,1);
INSERT INTO posicao VALUES (28,1, 3, 19, 37, 29, NULL, 'O jogar se encontra em um empasse, a oeste ele encontrar nada além de escuridão e resolve não seguir por ali',2,1);
INSERT INTO posicao VALUES (29,1, 3, 20, 38, 30, 28, 'Aqui jaz um deserto escaldante que não possui nada além de areia e animais peçonhentos.',2,1);
INSERT INTO posicao VALUES (30,1, 3, 21, 39, 31, 29, 'Aqui jaz um deserto escaldante que não possui nada além de areia e animais peçonhentos.',2,1);
INSERT INTO posicao VALUES (31,1, 3, 22, 40, NULL, 30, 'A leste existe um rio intransponivel é impossivel passar por ali, ache outro caminho, talvez exista uma ponte',2,1);
INSERT INTO posicao VALUES (32,1, 6, NULL, NULL, NULL, NULL, 'nesta posição existe um rio intransponível  de cor escura. não há nada para se fazer aqui',2,1);
INSERT INTO posicao VALUES (33,1, 4, 24, 42, 34, NULL, 'Voce encontra o rio que cerca a ilha por não saber nadar resolve não ir a oeste',0,1);
INSERT INTO posicao VALUES (34,1, 4, 25, 43, 35, 33, 'O gelo toma conta de tudo ao seu redor, tendo dificuldade inclusive de observar ao seu redor.',0,1);
INSERT INTO posicao VALUES (35,1, 4, 26, 44, 36, 34, 'O gelo toma conta de tudo ao seu redor, tendo dificuldade inclusive de observar ao seu redor.',1,1);
INSERT INTO posicao VALUES (36,1, 4, 27, 45, NULL, 35, 'a leste é possivel ver um penhasco extremamente profundo é melhor não ir por ali',1,1);
INSERT INTO posicao VALUES (37,1, 3, 28, 46, 38, NULL, 'O jogar se encontra em um empasse, a oeste ele encontrar nada além de escuridão e resolve não seguir por ali',2,0);
INSERT INTO posicao VALUES (38,1, 3, 29, 47, 39, 37, 'Aqui jaz um deserto escaldante que não possui nada além de areia e animais peçonhentos.',2,0);
INSERT INTO posicao VALUES (39,1, 3, 30, 48, 40, 38, 'Aqui jaz um deserto escaldante que não possui nada além de areia e animais peçonhentos.',2,0);
INSERT INTO posicao VALUES (40,1, 3, 31, 49, NULL, 39, 'A leste existe um rio intransponivel é impossivel passar por ali, ache outro caminho, talvez exista uma ponte',2,0);
INSERT INTO posicao VALUES (41,1, 6, NULL, NULL, NULL, NULL, 'nesta posição existe um rio intransponível  de cor escura. não há nada para se fazer aqui',2,0);
INSERT INTO posicao VALUES (42,1, 4, 33, 51, 43, NULL, 'Voce encontra o rio que cerca a ilha por não saber nadar resolve não ir a oeste',2,3);
INSERT INTO posicao VALUES (43,1, 4, 34, 52, 44, 42, 'O gelo toma conta de tudo ao seu redor, tendo dificuldade inclusive de observar ao seu redor.',2,3);
INSERT INTO posicao VALUES (44,1, 4, 35, 53, 45, 43, 'O gelo toma conta de tudo ao seu redor, tendo dificuldade inclusive de observar ao seu redor.',2,3);
INSERT INTO posicao VALUES (45,1, 4, 36, 54, NULL, 44, 'a leste é possivel ver um penhasco extremamente profundo é melhor não ir por ali',2,3);
INSERT INTO posicao VALUES (46,1, 3, 37, 55, 47, NULL, 'O jogar se encontra em um empasse, a oeste ele encontrar nada além de escuridão e resolve não seguir por ali',1,1);
INSERT INTO posicao VALUES (47,1, 3, 38, 56, 48, 46, 'Aqui jaz um deserto escaldante que não possui nada além de areia e animais peçonhentos.',1,1);
INSERT INTO posicao VALUES (48,1, 3, 39, 57, 49, 47, 'Aqui jaz um deserto escaldante que não possui nada além de areia e animais peçonhentos.',1,1);
INSERT INTO posicao VALUES (49,1, 3, 40, 58, NULL, 48, 'A leste existe um rio intransponivel é impossivel passar por ali, ache outro caminho',1,1);
INSERT INTO posicao VALUES (50,1, 6, NULL, NULL, NULL, NULL, 'nesta posição existe um rio intransponível  de cor escura. não há nada para se fazer aqui',1,1);
INSERT INTO posicao VALUES (51,1, 4, 42, 60, 52, NULL, 'Voce encontra o rio que cerca a ilha por não saber nadar resolve não ir a oeste',3,1);
INSERT INTO posicao VALUES (52,1, 4, 43, 61, 53, 51, 'O gelo toma conta de tudo ao seu redor, tendo dificuldade inclusive de observar ao seu redor.',3,1);
INSERT INTO posicao VALUES (53,1, 4, 44, 62, 54, 52, 'O gelo toma conta de tudo ao seu redor, tendo dificuldade inclusive de observar ao seu redor.',3,1);
INSERT INTO posicao VALUES (54,1, 4, 45, 63, NULL, 53, 'a leste é possivel ver um penhasco extremamente profundo é melhor não ir por ali',3,1);
INSERT INTO posicao VALUES (55,1, 3, 46, 64, 56, NULL, 'O jogar se encontra em um empasse, a oeste ele encontrar nada além de escuridão e resolve não seguir por ali',2,0);
INSERT INTO posicao VALUES (56,1, 3, 47, 65, 57, 55, 'Aqui jaz um deserto escaldante que não possui nada além de areia e animais peçonhentos.',2,0);
INSERT INTO posicao VALUES (57,1, 3, 48, 66, 58, 56, 'Aqui jaz um deserto escaldante que não possui nada além de areia e animais peçonhentos.',2,0);
INSERT INTO posicao VALUES (58,1, 3, 49, 67, NULL, 57, 'A leste existe um rio intransponivel é impossivel passar por ali, ache outro caminho, talvez exista uma ponte',2,0);
INSERT INTO posicao VALUES (59,1, 6, NULL, NULL, NULL, NULL, 'nesta posição existe um rio intransponível  de cor escura. não há nada para se fazer aqui',2,0);
INSERT INTO posicao VALUES (60,1, 4, 51, 69, 61, NULL, 'Voce encontra o rio que cerca a ilha por não saber nadar resolve não ir a oeste',2,2);
INSERT INTO posicao VALUES (61,1, 4, 52, 70, 62, 60, 'O gelo toma conta de tudo ao seu redor, tendo dificuldade inclusive de observar ao seu redor.',2,2);
INSERT INTO posicao VALUES (62,1, 4, 53, 71, 63, 61, 'O gelo toma conta de tudo ao seu redor, tendo dificuldade inclusive de observar ao seu redor.',2,2);
INSERT INTO posicao VALUES (63,1, 4, 54, 72, NULL, 62, 'a leste é possivel ver um penhasco extremamente profundo é melhor não ir por ali',2,2);
INSERT INTO posicao VALUES (64,1, 3, 55, 73, 65, NULL, 'O jogar se encontra em um empasse, a oeste ele encontrar nada além de escuridão e resolve não seguir por ali, ao sul existe um ponte que talvez possa passar',2,2);
INSERT INTO posicao VALUES (65,1, 3, 56, NULL, 66, 64, 'Ao sul finalmente é possivel ver agua, mas você não sabe nada :( , ache outro caminho, talvez exista uma ponte',1,0);
INSERT INTO posicao VALUES (66,1, 3, 57, NULL, 67, 65, 'Ao sul finalmente é possivel ver agua, mas você não sabe nada :( , ache outro caminho, talvez exista uma ponte',1,0);
INSERT INTO posicao VALUES (67,1, 3, 58, NULL, NULL, 66, 'Ao sul finalmente é possivel ver agua, mas você não sabe nada :( , ache outro caminho, talvez exista uma ponte',1,0);
INSERT INTO posicao VALUES (68,1, 6, NULL, NULL, NULL, NULL, 'nesta posição existe um rio intransponível  de cor escura. não há nada para se fazer aqui',1,0);
INSERT INTO posicao VALUES (69,1, 4, 60, NULL, 70, NULL, 'Ao sul e a oeste finalmente é possivel ver agua, mas você não sabe nada :( , ache outro caminho, talvez exista uma ponte',1,2);
INSERT INTO posicao VALUES (70,1, 4, 61, NULL, 71, 69, 'Ao sul finalmente é possivel ver agua, mas você não sabe nada :( , ache outro caminho, talvez exista uma ponte',1,2);
INSERT INTO posicao VALUES (71,1, 4, 62, NULL, 72, 70, 'O gelo toma conta de tudo ao seu redor, tendo dificuldade inclusive de observar ao seu redor.',1,2);
INSERT INTO posicao VALUES (72,1, 4, 63, NULL, NULL, 71, 'Ao sul finalmente é possivel ver agua, mas você não sabe nada :( , ache outro caminho, talvez exista uma ponte',1,2);
INSERT INTO posicao VALUES (73,1, 5, 64, 82, NULL, NULL, 'nesta posição existe uma ponte que não está em boas condições, seja rapido em sua pericia e avance logo em dia direção desejada. não se sabe quanto tempo ela irá aguentar seu peso sobre a ponte durar.',0,0);
INSERT INTO posicao VALUES (74 ,1, 6, NULL, NULL, NULL, NULL, 'nesta posição existe um rio intransponível  de cor escura. não há nada para se fazer aqui',0,0);
INSERT INTO posicao VALUES (75 ,1, 6, NULL, NULL, NULL, NULL, 'nesta posição existe um rio intransponível  de cor escura. não há nada para se fazer aqui',0,0);
INSERT INTO posicao VALUES (76,1, 6, NULL, NULL, NULL, NULL, 'nesta posição existe um rio intransponível  de cor escura. não há nada para se fazer aqui',0,0);
INSERT INTO posicao VALUES (77,1, 6, NULL, NULL, NULL, NULL, 'nesta posição existe um rio intransponível  de cor escura. não há nada para se fazer aqui',0,0);
INSERT INTO posicao VALUES (78 ,1, 6, NULL, NULL, NULL, NULL, 'nesta posição existe um rio intransponível  de cor escura. não há nada para se fazer aqui',0,0);
INSERT INTO posicao VALUES (79 ,1, 6, NULL, NULL, NULL, NULL, 'nesta posição existe um rio intransponível  de cor escura. não há nada para se fazer aqui',0,0);
INSERT INTO posicao VALUES (80 ,1, 6, NULL, NULL, NULL, NULL, 'nesta posição existe um rio intransponível  de cor escura. não há nada para se fazer aqui',0,0);
INSERT INTO posicao VALUES (81 ,1, 6, NULL, NULL, NULL, NULL, 'nesta posição existe um rio intransponível  de cor escura. não há nada para se fazer aqui',0,0);
INSERT INTO posicao VALUES (82,1, 2, 73, 91, 83, NULL, 'O jogar se encontra em um empasse, a oeste ele encontrar nada além de escuridão e resolve não seguir por ali mas ao norte existe um ponte velha que atravessa o rio',0,4);
INSERT INTO posicao VALUES (83,1, 2, NULL, 92, 84, 82, 'Ao norte é possivel ver um rio incrivel, mas a correnteza é muito forte. Melhor não ir por ali, talvez exista uma ponte',0,4);
INSERT INTO posicao VALUES (84,1, 2, NULL, 93, 85, 83, 'Ao norte é possivel ver um rio incrivel, mas a correnteza é muito forte. Melhor não ir por ali, talvez exista uma ponte',0,4);
INSERT INTO posicao VALUES (85,1, 2, NULL, 94, 86, 84, 'Você chegou ao limite do caminho, a norte e a leste existe um rio com correnteza fortissima, então decide pegar outro caminho',0,4);
INSERT INTO posicao VALUES (86,1, 6, NULL, NULL, NULL, NULL, 'nesta posição existe um rio intransponível  de cor escura. não há nada para se fazer aqui',0,4);
INSERT INTO posicao VALUES (87,1, 1, NULL, 96, 88, NULL, 'Você chegou ao limite do caminho, a norte e a oeste existe um rio com correnteza fortissima, então decide pegar outro caminho',7,9);
INSERT INTO posicao VALUES (88,1, 1, NULL, 97, 89, 87, 'Ao norte existe um rio belissimo mas está cheio de piranhas famintas, com certeza não é um caminho bom de fazer. Talvez exista uma ponte',7,9);
INSERT INTO posicao VALUES (89,1, 1, NULL, 98, 90, 88, 'Ao norte existe um rio belissimo mas está cheio de piranhas famintas, com certeza não é um caminho bom de fazer. Talvez exista uma ponte',7,9);
INSERT INTO posicao VALUES (90,1, 1, NULL, 99, NULL, 89, 'a leste é possivel ver um penhasco extremamente profundo é melhor não ir por ali, muito menos pelo rio de piranhas no norte',7,9);
INSERT INTO posicao VALUES (91,1, 2, 82, 100, 92, NULL, 'O jogar se encontra em um empasse, a oeste ele encontrar nada além de escuridão e resolve não seguir por ali',1,5);
INSERT INTO posicao VALUES (92,1, 2, 83, 101, 93, 91, 'Aqui existe um pantano pegajoso, só de andar já é dificil para todo lugar que olha há feras',1,5);
INSERT INTO posicao VALUES (93,1, 2, 84, 102, 94, 92, 'Aqui existe um pantano pegajoso, só de andar já é dificil para todo lugar que olha há feras',1,5);
INSERT INTO posicao VALUES (94,1, 2, 85, 103, 95, 93, 'A leste existe um rio intransponivel é impossivel passar por ali, ache outro caminho, talvez exista uma ponte',1,5);
INSERT INTO posicao VALUES (95,1, 6, NULL, NULL, NULL, NULL, 'nesta posição existe um rio intransponível  de cor escura. não há nada para se fazer aqui',1,5);
INSERT INTO posicao VALUES (96,1, 1, 87, 105, 97, NULL, 'Um rio com correnteza extramamente forte se encontra a oeste, é melhor não seguir por ai, talvez exista uma forma de passa como por exemplo uma ponte',5,10);
INSERT INTO posicao VALUES (97,1, 1, 88, 106, 98, 96, 'voçê se encontrar em uma floresta fechada, pode ser  perigosa mas é rica em recursos',5,10);
INSERT INTO posicao VALUES (98,1, 1, 89, 107, 99, 97, 'voçê se encontrar em uma floresta fechada, pode ser  perigosa mas é rica em recursos',5,10);
INSERT INTO posicao VALUES (99,1, 1, 90, 108, NULL, 98, 'a leste é possivel ver um penhasco extremamente profundo é melhor não ir por ali, talvez exista uma ponte',5,10);
INSERT INTO posicao VALUES (100,1, 2, 91, 109, 101, NULL, 'O jogar se encontra em um empasse, a oeste ele encontrar nada além de escuridão e resolve não seguir por ali',0,3);
INSERT INTO posicao VALUES (101,1, 2, 92, 110, 102, 100, 'Aqui existe um pantano pegajoso, só de andar já é dificil para todo lugar que olha há feras',0,3);
INSERT INTO posicao VALUES (102,1, 2, 93, 111, 103, 101, 'Aqui existe um pantano pegajoso, só de andar já é dificil para todo lugar que olha há feras',0,3);
INSERT INTO posicao VALUES (103,1, 2, 94, 112, 104, 102, 'A leste existe um rio intransponivel é impossivel passar por ali, ache outro caminho, talvez exista uma ponte',0,3);
INSERT INTO posicao VALUES (104,1, 6, NULL, NULL, NULL, NULL, 'nesta posição existe um rio intransponível  de cor escura. não há nada para se fazer aqui',0,3);
INSERT INTO posicao VALUES (105,1, 1, 96, 114, 106, NULL, 'Um rio com correnteza extramamente forte se encontra a oeste, é melhor não seguir por ai, talvez exista uma forma de passa como por exemplo uma ponte',6,8);
INSERT INTO posicao VALUES (106,1, 1, 97, 115, 107, 105, 'voçê se encontrar em uma floresta fechada, pode ser  perigosa mas é rica em recursos',6,8);
INSERT INTO posicao VALUES (107,1, 1, 98, 116, 108, 106, 'voçê se encontrar em uma floresta fechada, pode ser  perigosa mas é rica em recursos',6,8);
INSERT INTO posicao VALUES (108,1, 1, 99, 117, NULL, 107, 'a leste é possivel ver um penhasco extremamente profundo é melhor não ir por ali, talvez exista uma ponte',6,8);
INSERT INTO posicao VALUES (109,1, 2, 100, 118, 110, NULL, 'O jogar se encontra em um empasse, a oeste ele encontrar nada além de escuridão e resolve não seguir por ali',1,5);
INSERT INTO posicao VALUES (110,1, 2, 101, 119, 111, 109, 'Aqui existe um pantano pegajoso, só de andar já é dificil para todo lugar que olha há feras',1,5);
INSERT INTO posicao VALUES (111,1, 2, 102, 120, 112, 110, 'Aqui existe um pantano pegajoso, só de andar já é dificil para todo lugar que olha há feras',1,5);
INSERT INTO posicao VALUES (112,1, 2, 103, 121, 113, 111, 'A leste se encontra um ponta velha talvez possa passar por lá',1,5);
INSERT INTO posicao VALUES (113,1, 5, NULL, NULL, 114, 112, 'nesta posição existe uma ponte que não está em boas condições, seja rapido em sua pericia e avance logo em dia direção desejada. não se sabe quanto tempo ela irá aguentar seu peso sobre a ponte durar.',1,5);
INSERT INTO posicao VALUES (114,1, 1, 105, 123, 115, 113, 'A oeste é possivel ver uma ponte velha talvez dê para passar por ali',11,14);
INSERT INTO posicao VALUES (115,1, 1, 106, 124, 116, 114, 'voçê se encontrar em uma floresta fechada, pode ser  perigosa mas é rica em recursos',11,14);
INSERT INTO posicao VALUES (116,1, 1, 107, 125, 117, 115, 'voçê se encontrar em uma floresta fechada, pode ser  perigosa mas é rica em recursos',11,14);
INSERT INTO posicao VALUES (117,1, 1, 108, 126, NULL, 116, 'a leste é possivel ver um penhasco extremamente profundo é melhor não ir por ali',11,14);
INSERT INTO posicao VALUES (118,1, 2, 109, 127, 119, NULL, 'O jogar se encontra em um empasse, a oeste ele encontrar nada além de escuridão e resolve não seguir por ali',2,3);
INSERT INTO posicao VALUES (119,1, 2, 110, 128, 120, 118, 'Aqui existe um pantano pegajoso, só de andar já é dificil para todo lugar que olha há feras',2,3);
INSERT INTO posicao VALUES (120,1, 2, 111, 129, 121, 119, 'Aqui existe um pantano pegajoso, só de andar já é dificil para todo lugar que olha há feras',2,3);
INSERT INTO posicao VALUES (121,1, 2, 112, 130, 122, 120, 'A leste existe um rio intransponivel é impossivel passar por ali, ache outro caminho.',2,3);
INSERT INTO posicao VALUES (122,1, 6, NULL, NULL, NULL, NULL, 'nesta posição existe um rio intransponível  de cor escura. não há nada para se fazer aqui',2,3);
INSERT INTO posicao VALUES (123,1, 1, 114, 132, 124, NULL, 'Um rio com correnteza extramamente forte se encontra a oeste, é melhor não seguir por ai, talvez exista uma forma de passa como por exemplo uma ponte',6,9);
INSERT INTO posicao VALUES (124,1, 1, 115, 133, 125, 123, 'voçê se encontrar em uma floresta fechada, pode ser  perigosa mas é rica em recursos',6,9);
INSERT INTO posicao VALUES (125,1, 1, 116, 134, 126, 124, 'voçê se encontrar em uma floresta fechada, pode ser  perigosa mas é rica em recursos',6,9);
INSERT INTO posicao VALUES (126,1, 1, 117, 135, NULL, 125, 'a leste é possivel ver um penhasco extremamente profundo é melhor não ir por ali',6,9);
INSERT INTO posicao VALUES (127,1, 2, 118, 136, 128, NULL, 'O jogar se encontra em um empasse, a oeste ele encontrar nada além de escuridão e resolve não seguir por ali',1,4);
INSERT INTO posicao VALUES (128,1, 2, 119, 137, 129, 127, 'Aqui existe um pantano pegajoso, só de andar já é dificil para todo lugar que olha há feras',1,4);
INSERT INTO posicao VALUES (129,1, 2, 120, 138, 130, 128, 'Aqui existe um pantano pegajoso, só de andar já é dificil para todo lugar que olha há feras',1,4);
INSERT INTO posicao VALUES (130,1, 2, 121, 139, 131, 129, 'A leste existe um rio intransponivel é impossivel passar por ali, ache outro caminho, talvez exista uma ponte',1,4);
INSERT INTO posicao VALUES (131,1, 6, NULL, NULL, NULL, NULL, 'nesta posição existe um rio intransponível  de cor escura. não há nada para se fazer aqui',1,4);
INSERT INTO posicao VALUES (132,1, 1, 123, 141, 133, NULL, 'Um rio com correnteza extramamente forte se encontra a oeste, é melhor não seguir por ai, talvez exista uma forma de passa como por exemplo uma ponte',10,14);
INSERT INTO posicao VALUES (133,1, 1, 124, 142, 134, 132, 'voçê se encontrar em uma floresta fechada, pode ser  perigosa mas é rica em recursos',10,14);
INSERT INTO posicao VALUES (134,1, 1, 125, 143, 135, 133, 'voçê se encontrar em uma floresta fechada, pode ser  perigosa mas é rica em recursos',10,14);
INSERT INTO posicao VALUES (135,1, 1, 126, 144, NULL, 134, 'a leste é possivel ver um penhasco extremamente profundo é melhor não ir por ali',10,14);
INSERT INTO posicao VALUES (136,1, 2, 127, 145, 137, NULL, 'O jogar se encontra em um empasse, a oeste ele encontrar nada além de escuridão e resolve não seguir por ali',4,6);
INSERT INTO posicao VALUES (137,1, 2, 128, 146, 138, 136, 'Aqui existe um pantano pegajoso, só de andar já é dificil para todo lugar que olha há feras',4,6);
INSERT INTO posicao VALUES (138,1, 2, 129, 147, 139, 137, 'Aqui existe um pantano pegajoso, só de andar já é dificil para todo lugar que olha há feras',4,6);
INSERT INTO posicao VALUES (139,1, 2, 130, 148, 140, 138, 'A leste existe um rio intransponivel é impossivel passar por ali, ache outro caminho, talvez exista uma ponte',4,6);
INSERT INTO posicao VALUES (140,1, 6, NULL, NULL, NULL, NULL, 'nesta posição existe um rio intransponível  de cor escura. não há nada para se fazer aqui',4,6);
INSERT INTO posicao VALUES (141,1, 1, 132, 150, 142, NULL, 'Um rio com correnteza extramamente forte se encontra a oeste, é melhor não seguir por ai, talvez exista uma forma de passa como por exemplo uma ponte',9,12);
INSERT INTO posicao VALUES (142,1, 1, 133, 151, 143, 141, 'voçê se encontrar em uma floresta fechada, pode ser  perigosa mas é rica em recursos',9,12);
INSERT INTO posicao VALUES (143,1, 1, 134, 152, 144, 142, 'voçê se encontrar em uma floresta fechada, pode ser  perigosa mas é rica em recursos',9,12);
INSERT INTO posicao VALUES (144,1, 1, 135, 153, NULL, 143, 'a leste é possivel ver um penhasco extremamente profundo é melhor não ir por ali',9,12);
INSERT INTO posicao VALUES (145,1, 2, 136, NULL, 146, NULL, 'Você foi longe demais!! se encontra cercado por montanhas gigantescas o unico caminho possivel se encontra a norte e a leste',2,6);
INSERT INTO posicao VALUES (146,1, 2, 137, NULL, 147, 145, 'Ao sul é possivel encontrar uma montanha intransponível é melhor ir por outra direção, talvez exista uma ponte ',2,6);
INSERT INTO posicao VALUES (147,1, 2, 138, NULL, 148, 146, 'Ao sul é possivel encontrar uma montanha intransponível é melhor ir por outra direção , talvez exista uma ponte',2,6);
INSERT INTO posicao VALUES (148,1, 2, 139, NULL, 149, 147, 'A leste existe um rio intransponivel é impossivel passar por ali, ache outro caminho, talvez exista uma ponte',2,6);
INSERT INTO posicao VALUES (149,1, 6, NULL, NULL, NULL, NULL, 'nesta posição existe um rio intransponível  de cor escura. não há nada para se fazer aqui',2,6);
INSERT INTO posicao VALUES (150,1, 1, 141, NULL, 151, NULL, 'Ao sul é possivel encontrar uma montanha intransponível e um rio gigante a oeste é melhor ir por outra direção ',9,13);
INSERT INTO posicao VALUES (151,1, 1, 142, NULL, 152, 150, 'Ao sul é possivel encontrar uma montanha intransponível é melhor ir por outra direção ',9,13);
INSERT INTO posicao VALUES (152,1, 1, 143, NULL, 153, 151, 'Ao sul é possivel encontrar uma montanha intransponível é melhor ir por outra direção ',9,13);
INSERT INTO posicao VALUES (153,1, 1, 144, NULL, NULL, 152, 'Você foi longe demais!! se encontra cercado por montanhas gigantescas o unico caminho possivel se encontra a norte e a oeste',9,13);


-- arma

INSERT INTO arma VALUES (DEFAULT, 'Espada de Pedra', 4, 'Espada fraca criada apartir de 15 pedras e 15 madeiras, é essencial para sobreviver a encontro de inimigos');
INSERT INTO arma VALUES (DEFAULT, 'Espada de Ferro', 10, 'Espada Forte craida apartir de 5 ferro, 40 madeiras , é uma espada incrivelmente versatil para batalhas contra inimigos fortes');
INSERT INTO arma VALUES (DEFAULT, 'Espada Suprema', 20, 'Espada Suprema craida apartir de 10 ferro, 80 madeiras , é uma espada incrivelmente versatil para batalhas contra inimigos fortes');

-- ferramenta

INSERT INTO ferramenta VALUES (DEFAULT, 'Machado Quebrado', 'pegar_madeira(jogador, 1)', 'Esse Machado aparenta está em pessimas condições mas ainda é possivel obter madeira de arvores');
INSERT INTO ferramenta VALUES (DEFAULT, 'Machado Fraco', 'pegar_madeira(jogador, 2)', 'Machado fraco contruido apartir de 15 pedras, 15 madeiras ');
INSERT INTO ferramenta VALUES (DEFAULT, 'Machado de Ferro', 'pegar_madeira(jogador, 3)', 'Machado de Ferro contruido apartir de 3 ferros , 30 madeiras ');


INSERT INTO ferramenta VALUES (DEFAULT, 'Picareta Detreriorada', 'pegar_pedra(jogador, 1)', 'Essa picareta está quase completamente detreriorada mas ainda é posssivel obter pedras de rochas');
INSERT INTO ferramenta VALUES (DEFAULT, 'Picareta de Madeira', 'pegar_pedra(jogador, 2)', 'Picareta de Madeira contruido apartir de 15 pedras, 15 madeiras e ');
INSERT INTO ferramenta VALUES (DEFAULT, 'Picareta de Ferro', 'pegar_pedra(jogador, 3)', 'Picareta de Ferro contruido apartir de 3 ferros , 30 madeiras ');


INSERT INTO ferramenta VALUES (DEFAULT, 'Workbench', 'colocar_na_pos(jogador, 11)', 'workbench é o principal item para criação de novas ferramentas e armas');

-- roupa

INSERT INTO roupa VALUES (DEFAULT, 'Roupa gasta', 1,2,'Roupa gasta mas ajuda levemente na proteção');
INSERT INTO roupa VALUES (DEFAULT, 'Roupa reforçada', 3,4,'Roupa reforçada, ajuda levemente na proteção termica e proteção fisica');
INSERT INTO roupa VALUES (DEFAULT, 'Casaco de guerra', 7,6,'Casco utilizado pela guerrilha, tem grande proteção fisica e termica');
INSERT INTO roupa VALUES (DEFAULT, 'Roupa do Batman', 10,10,'O melhor do melhor, criado pelo cavaleiro das trevas para enfrentar os males do mundo');


-- ingrediente

INSERT INTO ingrediente VALUES (DEFAULT, 'madeira', 'ingrediente', 'Um pedaço de madeira!');
INSERT INTO ingrediente VALUES (DEFAULT, 'pedra', 'ingrediente', 'Uma unidade de pedra!');


-- instancia_item
INSERT INTO instancia_item  VALUES (DEFAULT,1, 'a'); -- machado
INSERT INTO instancia_item  VALUES (DEFAULT,1, 'f'); -- picareta
INSERT INTO instancia_item  VALUES (DEFAULT,2, 'f'); -- workbench
INSERT INTO instancia_item  VALUES (DEFAULT,4, 'r'); -- frio
INSERT INTO instancia_item  VALUES (DEFAULT,1, 'i'); -- cipo

-- instancia_item_posicao
INSERT INTO instancia_item_posicao VALUES (3, 3); -- workbench na posicao 3

-- MONSTRO

-- (Pantano)
--( nome,dano,descricao,vida,isca,posicao)


INSERT INTO monstro VALUES (DEFAULT,'Sapo',2,'Sapo está irritado com sua presença, ele se prepara pra lhe atacar',10,1,148);
INSERT INTO monstro VALUES (DEFAULT,'Sucuri',4,'Uma jovem sucuri lhe encontra e está preste a lhe atacar',20,2,85);
INSERT INTO monstro VALUES (DEFAULT,'Jacare',8,'Um grande jacare faminto pronto pra atacar qualquer um que encontrar',35,4,118);
INSERT INTO monstro VALUES (DEFAULT,'Pumba(BOSS)',14,'Pumba é considerado o rei do Pantano, sua quantidade de vida é gigante e seu dano fenomenal',100,7,82);

-- (Deserto)
INSERT INTO monstro VALUES (DEFAULT,'Lagarto',2,'Um largarto pequeno e extrassado pronto para atacar todos',3,1,65);
INSERT INTO monstro VALUES (DEFAULT,'escorpiao',6,'Um dos monstro ferozes do deserto, sua baixa vida compensa ao seu alto dano',15,6,39);
INSERT INTO monstro VALUES (DEFAULT,'Camelo',4,'Camelo mutante do deserto,após anos de andarilho esse camelo criou uma proteção quase que inquebravel com uma vida enorme',50,9,57);
INSERT INTO monstro VALUES (DEFAULT,'Vermes da areia(BOSS)',15,'é o rei do deserto, sua enorme boca consegue devorar até o maior dos seres',80,15,13);

-- (Floresta)
INSERT INTO monstro VALUES (DEFAULT,'Perna Longa',1,'Durante anos e anos a fio essa lebre se aventura pela floresta, é relativamente fraco',10,1,90);
INSERT INTO monstro VALUES (DEFAULT,'Burro',3,'Dizem ser um dos monstros mais fraco da floresta, mas já se mostrou capaz de domar até um dragão',15,3,87);
INSERT INTO monstro VALUES (DEFAULT,'Shrek',8,'é o ogro mais feroz da historia é forte mas sua vida se acaba facilmente por conta do seu sedentarismo',24,1,150);
INSERT INTO monstro VALUES (DEFAULT,'Gato de botas(BOSS)',18,'é o rei da floresta com sua arte de esgrima monstruosa, dano gigantesco mas vida baixa',60,3,114);

-- (Tundra)
INSERT INTO monstro VALUES (DEFAULT,'O galo do pantanal',1,'ele está numa paz não se nega a atacar',10,1,24);
INSERT INTO monstro VALUES (DEFAULT,'Os pinguins de madagascar',6,'é o trio mais feroz da tundra com ataque cordenado e vida baixa',20,3,51);
INSERT INTO monstro VALUES (DEFAULT,'O pé grande',14,'é como dizem feroz e gigantesco, acaba com varios de uma só vez com sua pisada mortal',60,1,7);
INSERT INTO monstro VALUES (DEFAULT,'Olaf (BOSS)',25,'aparente se mostra somente uma bola de neve inofenciva, mas com praticas de milenios em magia negra é definitivamente o mais forte de todos',200,3,62);


-- mochila
INSERT INTO mochila VALUES (DEFAULT);
INSERT INTO mochila VALUES (DEFAULT);

-- jogador


-- mochila_guarda_instancia_de_item
INSERT INTO mochila_guarda_instancia_de_item VALUES (1, 5);
INSERT INTO mochila_guarda_instancia_de_item VALUES (1, 5);
INSERT INTO mochila_guarda_instancia_de_item VALUES (1, 5);

-- craft
INSERT INTO craft VALUES (DEFAULT, 5, 3, NULL, NULL, NULL, NULL, 'false', 'Uma corda nao tao natual!');
