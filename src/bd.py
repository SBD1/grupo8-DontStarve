# mock
# mock jogador
import psycopg2
conn = psycopg2.connect(
    host = "db",
    port = "5432",
    database="dontstarve",
    user="sbd1",
    password="asdfghjkl")

cursor = conn.cursor()


jogador = type('', (), {})()

jogador.id = 1
jogador.nome = 'player1'
jogador.vida = 100
jogador.id_mochila = 1
jogador.id_posicao = 0
jogador.id_roupa_equipada = None
jogador.id_item_equipado = None
#end mock jogador

# mock pos
pos0 = type('', (), {})()
pos0.id = 0
pos0.bioma = 1
pos0.norte = 1
pos0.sul = None
pos0.leste = None
pos0.oeste = 2
pos0.descricao = 'floresta bonita'
pos0.pedras = 30


pos1 = type('', (), {})()
pos1.id = 1
pos1.bioma = 1
pos1.norte = None
pos1.sul = 0
pos1.leste = None
pos1.oeste = None
pos1.descricao = 'floresta ao norte'
pos1.pedras = 10

pos2 = type('', (), {})()
pos2.id = 2
pos2.bioma = 1
pos2.norte = None
pos2.sul = None
pos2.leste = 0
pos2.oeste = None
pos2.descricao = 'floresta ao oeste'
pos2.pedras = 0

# end mock pos

# mock bioma
bioma1 = type('', (), {})()
bioma1.id = 1
bioma1.chance_batalha = 0.30 # 30%
bioma1.delta_temp = 10
bioma1.nome = 'floresta'
# end mock bioma

# mock arma
item1 = type('', (), {})()
item1.id = 1
item1.nome = 'Espada nv1'
item1.dano = 10
item1.descricao = 'Espada velha'

item2 = type('', (), {})()
item2.id = 2
item2.nome = 'Espada nv2'
item2.dano = 20
item2.descricao = 'Espada nova'
# end mock arma

# mock ferramenta
item3 = type('', (), {})()
item3.id = 3
item3.nome = 'Picareta nv1'
item3.funcao = 'pegar_pedra(jogador, 1)'
item3.descricao = 'Picareta Velha'

item4 = type('', (), {})()
item4.id = 4
item4.nome = 'Picareta nv2'
item4.funcao = 'pegar_pedra(jogador, 2)'
item4.descricao = 'Picareta Nova'
# end mock ferramenta

# mock roupa
item5 = type('', (), {})()
item5.id = 5
item5.nome = 'roupa 1'
item5.protecao_termica = 10
item5.protecao_fisica = 1
item5.descricao = 'roupa de frio'

item6 = type('', (), {})()
item6.id = 6
item6.nome = 'roupa 2'
item6.protecao_termica = 5
item6.protecao_fisica = 15
item6.descricao = 'roupa de combate'
# end mock roupa

# mock ingrediente
item7 = type('', (), {})()
item7.id = 7
item7.nome = 'cipo'
item7.funcao = None
item7.descricao = 'corda natural'

item8 = type('', (), {})()
item8.id = 8
item8.nome = 'ferro'
item8.funcao = None
item8.descricao = 'o queridinho dos ferreiros'

item9 = type('', (), {})()
item9.id = 9
item9.nome = 'madeira'
item9.funcao = None
item9.descricao = 'o queridinho dos herbivoros'

item10 = type('', (), {})()
item10.id = 10
item10.nome = 'corda'
item10.funcao = None
item10.descricao = 'corda artificial'

item11 = type('', (), {})()
item11.id = 11
item11.nome = 'workbench'
item11.funcao = 'colocar_na_pos(jogador, 11)'
item11.descricao = 'o queridinho dos manufatores'

# end mock ingretiente


# mock instancia item
instancia_item1 = type('', (), {})()
instancia_item1.id = 1
instancia_item1.id_item = 1 # espada nv1
instancia_item1.tipo = 'a'

instancia_item2 = type('', (), {})()
instancia_item2.id = 2
instancia_item2.id_item = 3 # picareta nv1
instancia_item2.tipo = 'f'

instancia_item3 = type('', (), {})()
instancia_item3.id = 3
instancia_item3.id_item = 4 # picareta nv2
instancia_item3.tipo = 'f'

instancia_item4 = type('', (), {})()
instancia_item4.id = 4
instancia_item4.id_item = 5 # roupa
instancia_item4.tipo = 'r'

instancia_item5 = type('', (), {})()
instancia_item5.id = 5
instancia_item5.id_item = 7 # cipo
instancia_item5.tipo = 'i'

instancia_item6 = type('', (), {})()
instancia_item6.id = 6
instancia_item6.id_item = 7 # cipo
instancia_item6.tipo = 'i'

instancia_item7 = type('', (), {})()
instancia_item7.id = 7
instancia_item7.id_item = 8 # ferro
instancia_item7.tipo = 'i'

instancia_item8 = type('', (), {})()
instancia_item8.id = 8
instancia_item8.id_item = 9 # madeira
instancia_item8.tipo = 'i'

instancia_item9 = type('', (), {})()
instancia_item9.id = 9
instancia_item9.id_item = 9 # madeira
instancia_item9.tipo = 'i'

instancia_item10 = type('', (), {})()
instancia_item10.id = 10
instancia_item10.id_item = 10 # corda
instancia_item10.tipo = 'i'

instancia_item11 = type('', (), {})()
instancia_item11.id = 11
instancia_item11.id_item = 11 # workbench
instancia_item11.tipo = 'f'

instancia_item12 = type('', (), {})()
instancia_item12.id = 12
instancia_item12.id_item = 1 # espada nv 1
instancia_item12.tipo = 'a'
# end instancia item

# mock instancia item posicao
instancia_item_posicao0 = type('', (), {})()
instancia_item_posicao0.id_posicao = None
instancia_item_posicao0.id_instancia_item = None

instancia_item_posicao1 = type('', (), {})()
instancia_item_posicao1.id_posicao = None
instancia_item_posicao1.id_instancia_item = None

instancia_item_posicao2 = type('', (), {})()
instancia_item_posicao2.id_posicao = None
instancia_item_posicao2.id_instancia_item = None
#end mock instancia item posicao

# mock mochila
mochila = type('', (), {})()
mochila.id = 1
# end mock mochila

# mock mochila_guarda_instancia_de_item
item_mochila1 = type('', (), {})()
item_mochila1.id_mochila = 1
item_mochila1.id_instancia_item = 1

item_mochila2 = type('', (), {})()
item_mochila2.id_mochila = 1
item_mochila2.id_instancia_item = 2

item_mochila3 = type('', (), {})()
item_mochila3.id_mochila = 1
item_mochila3.id_instancia_item = 3

item_mochila4 = type('', (), {})()
item_mochila4.id_mochila = 1
item_mochila4.id_instancia_item = 4

item_mochila5 = type('', (), {})()
item_mochila5.id_mochila = 1
item_mochila5.id_instancia_item = 5

item_mochila6 = type('', (), {})()
item_mochila6.id_mochila = 1
item_mochila6.id_instancia_item = 6

item_mochila7 = type('', (), {})()
item_mochila7.id_mochila = 1
item_mochila7.id_instancia_item = 7

item_mochila8 = type('', (), {})()
item_mochila8.id_mochila = 1
item_mochila8.id_instancia_item = 8

item_mochila9 = type('', (), {})()
item_mochila9.id_mochila = 1
item_mochila9.id_instancia_item = 9

item_mochila10 = type('', (), {})()
item_mochila10.id_mochila = 0
item_mochila10.id_instancia_item = 10

item_mochila11 = type('', (), {})()
item_mochila11.id_mochila = 0
item_mochila11.id_instancia_item = 11

item_mochila12 = type('', (), {})()
item_mochila12.id_mochila = 0
item_mochila12.id_instancia_item = 12
# end mock mochila_guarda_instancia_de_item

# mock craft
craft1 = type('', (), {})()
craft1.nome = 'corda'
craft1.descricao = '2 cipos'
craft1.id = 1
craft1.id_item1 = 7 # cipo
craft1.quant_item1 = 2
craft1.id_item2 = None
craft1.quant_item2 = None
craft1.id_item3 = None
craft1.quant_item3 = None
craft1.necessita_workbench = False
craft1.id_item_resultado = 10

craft2 = type('', (), {})()
craft2.nome = 'workbench'
craft2.descricao = '1 madeira'
craft2.id = 2
craft2.id_item1 = 9 # madeira
craft2.quant_item1 = 1
craft2.id_item2 = None
craft2.quant_item2 = None
craft2.id_item3 = None
craft2.quant_item3 = None
craft2.necessita_workbench = False
craft2.id_item_resultado = 11

craft3 = type('', (), {})()
craft3.nome = 'espada nv1'
craft3.descricao = '1 madeira, 1 ferro'
craft3.id = 3
craft3.id_item1 = 9 # madeira
craft3.quant_item1 = 1
craft3.id_item2 = 8 # ferro
craft3.quant_item2 = 1
craft3.id_item3 = None
craft3.quant_item3 = None
craft3.necessita_workbench = True
craft3.id_item_resultado = 1

# end mock craft

# mock monstros
monstro1 = type('', (), {})()
monstro1.id = 1
monstro1.nome = 'coelho'
monstro1.descricao = 'igualzinho a seu jantar.'
monstro1.dano = 2
monstro1.vida = 15
monstro1.isca = 0
monstro1.id_posicao = 0

monstro2 = type('', (), {})()
monstro2.id = 2
monstro2.nome = 'lobo'
monstro2.descricao = 'quem come seu jantar.'
monstro2.dano = 8
monstro2.vida = 40
monstro2.isca = 1
monstro2.id_posicao = 0
# end mock monstros

# end mock


def get_jogadores():
    cursor.execute("SELECT  * FROM jogador")
    return cursor.fetchall()

def get_jogador_id(id):
    cursor.execute(f"SELECT * FROM jogador WHERE id = '{id}'")
    jogador = type('', (), {})()
    jogador.id = 1
    jogador.nome = 'player1'
    jogador.vida = 100
    jogador.id_mochila = 1
    jogador.id_posicao = 0
    jogador.id_roupa_equipada = None
    jogador.id_item_equipado = None
    return jogador

def del_jogador(jogador):
    cursor.execute(f"DELETE FROM jogador WHERE id = {get_jogador_id(jogador)}")
    
    return cursor.fetchall()

def set_vida_jogador(jogador, vida):
    cursor.execute(f"UPDATE jogador SET vida = {vida} WHERE id = {get_jogador_id(jogador)};")
    return cursor.fetchall()

def get_jogos_salvos():
    # retornar todos os jog adores salvos em array
    cursor.execute("SELECT  * FROM jogador")
    return cursor.fetchall()


def novo_jogador(nome: str):
    # inserir novo jogador no bd, em caso de falha retornar False
    # em caso de sucesso:
    cursor.execute(f"INSERT INTO mochila VALUES (DEFAULT);")
    cursor.execute(f"SELECT id FROM mochila ORDER BY  id  DESC LIMIT 1;")
    id_mochila = cursor.fetchone()[0]
    cursor.execute(f"INSERT INTO jogador VALUES (DEFAULT,'{nome}',100,36,{id_mochila}, 3,NULL,NULL);")
    id = cursor.lastrowid
    return get_jogador_id(id)


def get_posicao_jogador(id):
    # pegar infos da posicao que o jogador se encontra no banco
    cursor.execute(f"SELECT id_posicao FROM jogador WHERE id ='{id}'")
    idpos = cursor.fetchone()[0]
    return get_posicao(idpos)


def set_posicao_jogador(nome, posicao):
    # setar posicao do jogador "nome" para "posicao"
    cursor.execute(f"UPDATE jogador SET id_posicao = {posicao} WHERE nome = '{nome[1]}'")
    return cursor.fetchall()


def get_inventario_por_tipo(id, tipo):
    # retornar todos as intancias de item associadas a mochila player.mochila no formato[[instancia, item], ...]
    cursor.execute(f"SELECT id_mochila FROM jogador WHERE id = {id}")
    id_mochila = cursor.fetchone()[0]
    cursor.execute(f"SELECT id_instancia_item FROM mochila_guarda_instancia_de_item WHERE id_mochila = {id_mochila} AND id_instancia_item IN (SELECT id FROM instancia_item WHERE tipo = {tipo})")
    instancias = cursor.fetchall()
    result = []
    for i in instancias:
        cursor.execute(f"SELECT id_item FROM instancia_item WHERE id = {i[0]}")
        id_item = cursor.fetchone()[0]
        if(tipo == 'a'):
            cursor.execute(f"SELECT * FROM arma WHERE id = {id_item}")
            aux = cursor.fetchone()
            arma = type('', (), {})()
            arma.id = aux[0]
            arma.nome = aux[1]
            arma.dano = aux[2]
            arma.descricao = aux[3]
            arma.instancia = i
            result.append(arma)
        if(tipo == 'f'):
            cursor.execute(f"SELECT * FROM ferramenta WHERE id = {id_item}")
            aux = cursor.fetchone()
            ferramenta = type('', (), {})()
            ferramenta.id = aux[0]
            ferramenta.nome = aux[1]
            ferramenta.funcao = aux[2]
            ferramenta.descricao = aux[3]
            ferramenta.instancia = i
            result.append(ferramenta)
        if(tipo == 'r'):
            cursor.execute(f"SELECT * FROM roupa WHERE id = {id_item}")
            aux = cursor.fetchone()
            roupa = type('', (), {})()
            roupa.id = aux[0]
            roupa.nome = aux[1]
            roupa.protecao_termica = aux[2]
            roupa.protecao_fisica = aux[3]
            roupa.descricao = aux[4]
            roupa.instancia = i
            result.append(roupa)
        if(tipo == 'i'):
            cursor.execute(f"SELECT * FROM ingrediente WHERE id = {id_item}")
            aux = cursor.fetchone()
            ingrediente = type('', (), {})()
            ingrediente.id = aux[0]
            ingrediente.nome = aux[1]
            ingrediente.funcao = aux[2]
            ingrediente.descricao = aux[3]
            ingrediente.instancia = i
            result.append(ingrediente)
    return result


def get_item_por_id_instancia(id_instancia):
    # retornar todos as intancias de item associadas a mochila player.mochila no formato[[instancia, item], ...]
    cursor.execute(f"SELECT * FROM instancia_item WHERE id = {id_instancia}")
    instancia = cursor.fetchone()
    id_item = instancia[1]
    tipo = instancia[2]
    
    if(tipo == 'a'):
        cursor.execute(f"SELECT * FROM arma WHERE id = {id_item}")
        aux = cursor.fetchone()
        arma = type('', (), {})()
        arma.id = aux[0]
        arma.nome = aux[1]
        arma.dano = aux[2]
        arma.descricao = aux[3]
        arma.instancia = id_instancia
        return (arma)
    if(tipo == 'f'):
        cursor.execute(f"SELECT * FROM ferramenta WHERE id = {id_item}")
        aux = cursor.fetchone()
        ferramenta = type('', (), {})()
        ferramenta.id = aux[0]
        ferramenta.nome = aux[1]
        ferramenta.funcao = aux[2]
        ferramenta.descricao = aux[3]
        ferramenta.instancia = id_instancia
        return (ferramenta)
    if(tipo == 'r'):
        cursor.execute(f"SELECT * FROM roupa WHERE id = {id_item}")
        aux = cursor.fetchone()
        roupa = type('', (), {})()
        roupa.id = aux[0]
        roupa.nome = aux[1]
        roupa.protecao_termica = aux[2]
        roupa.protecao_fisica = aux[3]
        roupa.descricao = aux[4]
        roupa.instancia = id_instancia
        return (roupa)
    if(tipo == 'i'):
        cursor.execute(f"SELECT * FROM ingrediente WHERE id = {id_item}")
        aux = cursor.fetchone()
        ingrediente = type('', (), {})()
        ingrediente.id = aux[0]
        ingrediente.nome = aux[1]
        ingrediente.funcao = aux[2]
        ingrediente.descricao = aux[3]
        ingrediente.instancia = id_instancia
        return (ingrediente)


#TODO implementar mock
def get_posicao(id_pos):
    # retornar infos da posicao que o jogador se encontra no banco
    cursor.execute(f"SELECT * FROM posicao WHERE id = {id_pos}")
    return cursor.fetchall()


def set_pedras(id_pos, pedras):
    cursor.execute(f"UPDATE posicao SET pedras = {pedras} WHERE id = {id_pos}")
    return cursor.fetchall()


def get_instancia_item_por_id(id_item):
    cursor.execute(f"SELECT * FROM instancia_item WHERE id = {id_item}")
    return cursor.fetchall()

    
def get_item_por_id(id_item):
    cursor.execute(f"SELECT * FROM item WHERE id = {id_item}")
    return cursor.fetchall()


def set_item_equipado(id_jogador, id_instancia_item):
    cursor.execute(f"UPDATE jogador SET id_item_equipado = {id_instancia_item} WHERE id = {(id_jogador)}")
    return cursor.fetchall()
    


def get_item_equipado(id_jogado):
    cursor.execute(f"SELECT id_item_equipado FROM jogador WHERE id = {(id_jogado)}")
    return cursor.fetchall()


def set_roupa_equipada(id_jogador, id_instancia_item):
    cursor.execute(f"UPDATE jogador SET id_roupa_equipada = {id_instancia_item} WHERE id = {(id_jogador)}")
    return cursor.fetchall()


def get_roupa_equipada(id_jogador):
    cursor.execute(f"SELECT id_roupa_equipada FROM jogador WHERE id = {(id_jogador)}")
    return cursor.fetchone()[0]


def add_instancia_item_possicao(id_pos, id_instancia):
    # adicionar linha na tabela instancia_item_posicao, retornar T/F
    cursor.execute(f"INSERT INTO instancia_item_posicao VALUES ({id_pos},{id_instancia})")
    return cursor.fetchall()


def get_instancia_item_posicao(id_pos):
    # retornar todos as instancia_item_posicao que tenha como id_posicao "id_pos"
    cursor.execute(f"SELECT id_instancia_item FROM instancia_item_posicao WHERE id_posicao = {id_pos}")
    aux = cursor.fetchall()
    result = []
    for i in aux:
        result.append(get_instancia_item_por_id(i))
    return cursor.fetchall()


def del_instancia_item_posicao(id_pos, id_instancia):
    # deletar linha na tabela instancia_item_posicao, retornar T/F
    cursor.execute(f"DELETE FROM instancia_item_posicao WHERE id_posicao = {id_pos} AND id_instancia_item = {id_instancia}")
    return cursor.fetchall()


def get_crafts(workbench):

    # retornar todos os crafts se 'workbench' == True
    if workbench:
        return cursor.execute(f"SELECT * FROM craft").fetchall()

    return cursor.execute(f"SELECT * FROM craft WHERE necessita_workbench = 'false'").fetchall()

    #TODO find via id player
def get_mochila_id(nome_jogador):
    cursor.execute(f"SELECT id_mochila FROM jogador WHERE nome = '{nome_jogador[1]}'")
    return cursor.fetchone()[0]

def verificar_inventario(jogador, id_item, quantidade = 1):
    # retornar True se o jogador possuir quantidade do item necessario, False se nao
    # SELECT 
    # COUNT(cod_servico) AS quantidade
    # FROM tb_ordem_servico
    # WHERE cod_servico = 'A';
    cursor.execute(f"SELECT COUNT(id_instancia_item) AS quantidade FROM mochila_guarda_instancia_de_item WHERE id_mochila = {get_mochila_id(jogador)} AND id_instancia_item = {id_item}")
    return cursor.fetchone()[0] >= quantidade


    #TODO return id instancia item
def criar_instancia_item(id_item,tipo):
    # criar uma nova instancia de item e retornar seu id
    cursor.execute(f"INSERT INTO instancia_item VALUES (DEFAULT,{id_item},'{tipo}')")
    return cursor.fetchall()


def remover_item_iventario(jogador, id_item):

    id_mochila = get_mochila_id(jogador)
    cursor.execute(f"DELETE FROM mochila_guarda_instancia_de_item WHERE id_mochila = {id_mochila} AND id_instancia_item = {id_item}")
    return cursor.fetchall()
    

def adicionar_item_iventario(jogador, id_instancia_item):
    # adicionar item na mochila do jogador
    id_mochila = get_mochila_id(jogador)
    cursor.execute(f"INSERT INTO mochila_guarda_instancia_de_item VALUES ({id_mochila},{id_instancia_item})")
    return cursor.fetchall()


def get_bioma(id_bioma):
    cursor.execute(f"SELECT * FROM bioma WHERE id = {id_bioma}")
    aux = cursor.fetchall()
    bioma = type('', (), {})()
    bioma.id = aux[0]
    bioma.chance_batalha = aux[1]
    bioma.delta_temp = aux[2]
    bioma.nome = aux[3]
    bioma.nivel = aux[4]
    return bioma

#TODO return all monstros da pos
def get_monstros_by_pos(id_pos):
    cursor.execute(f"SELECT * FROM monstro WHERE id_posicao = {id_pos}")
    aux = cursor.fetchall()
    monstro = type('', (), {})()
    monstro.id = aux[0]
    monstro.nome = aux[1]
    monstro.dano = aux[2]
    monstro.descricao = aux[3]
    monstro.vida = aux[4]
    monstro.isca = aux[5]
    monstro.id_posicao = aux[6]
    return monstro


def del_monstro(id_monstro):
    try:
        cursor.execute(f"DELETE FROM monstro WHERE id = {id_monstro}")
        return True
    except:
        return False