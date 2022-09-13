
import psycopg2
conn = psycopg2.connect(
    host = "db",
    port = "5432",
    database="dontstarve",
    user="sbd1",
    password="asdfghjkl")
cursor = conn.cursor()

def get_jogadores():
    cursor.execute("SELECT  * FROM jogador")
    return cursor.fetchall()

def get_jogador_id(id):
    cursor.execute(f"SELECT * FROM jogador WHERE id = '{id}'")
    aux = cursor.fetchone()
    jogador = type('', (), {})()
    jogador.id = aux[0]
    jogador.nome = aux[1]
    jogador.vida = aux[2]
    jogador.temp_corporal = aux[3]
    jogador.id_mochila = aux[4]
    jogador.id_posicao = aux[5]
    jogador.id_roupa_equipada = aux[6]
    jogador.id_item_equipado = aux[7]
    return jogador

def del_jogador(id):
    try:
        cursor.execute(f"DELETE FROM jogador WHERE id = {id}")
        conn.commit()
    except:
        return False
    return True

def set_vida_jogador(id_jogador, vida):
    cursor.execute(f"UPDATE jogador SET vida = {vida} WHERE id = {id_jogador};")
    conn.commit()
    return True

def novo_jogador(nome: str):
    # inserir novo jogador no bd, em caso de falha retornar False
    # em caso de sucesso:
    cursor.execute(f"INSERT INTO mochila VALUES (DEFAULT);")
    cursor.execute(f"SELECT id FROM mochila ORDER BY  id  DESC LIMIT 1;")
    id_mochila = cursor.fetchone()
    cursor.execute(f"INSERT INTO jogador VALUES (DEFAULT,'{nome}',100,36,{id_mochila[0]}, 134,NULL,NULL);")
    cursor.execute(f"SELECT id FROM jogador ORDER BY  id  DESC LIMIT 1;")
    id = cursor.fetchone()
    cursor.execute(f"SELECT id FROM ferramenta WHERE nome =  'Picareta Detreriorada'")
    id_picareta = cursor.fetchone()[0]
    instancia_item1 = criar_instancia_item(id_picareta,'f')
    cursor.execute(f"SELECT id FROM ferramenta WHERE nome =  'Machado Fraco'")
    id_machado = cursor.fetchone()[0]
    instancia_item2 = criar_instancia_item(id_machado,'f')
    jogador = get_jogador_id(id[0])
    adicionar_item_iventario(jogador,instancia_item1)
    adicionar_item_iventario(jogador,instancia_item2)
    conn.commit()
    return jogador


def get_posicao_jogador(id_jogador):
    # pegar infos da posicao que o jogador se encontra no banco
    cursor.execute(f"SELECT id_posicao FROM jogador WHERE id ='{id_jogador}'")
    id_pos = cursor.fetchone()[0]
    return get_posicao(id_pos)


def set_posicao_jogador (id, posicao):
    # setar posicao do jogador "nome" para "posicao"
    cursor.execute(f"UPDATE jogador SET id_posicao = {posicao} WHERE id = '{id}'")
    conn.commit()
    return True


def get_inventario_por_tipo (id, tipo):
    # retornar todos as intancias de item associadas a mochila player.mochila no formato[[instancia, item], ...]
    cursor.execute(f"SELECT id_mochila FROM jogador WHERE id = {id}")
    id_mochila = cursor.fetchone()[0]
    cursor.execute(f"SELECT id_instancia_item FROM mochila_guarda_instancia_de_item WHERE id_mochila = {id_mochila}")
    instancias = cursor.fetchall()
    result = []
    for instancia in instancias:
        cursor.execute(f"SELECT * FROM instancia_item WHERE id = {instancia[0]}")
        news = cursor.fetchone()
        if(news[2] == tipo):
            result.append(get_item_por_id_instancia(instancia[0]))
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
    elif(tipo == 'f'):
        cursor.execute(f"SELECT * FROM ferramenta WHERE id = {id_item}")
        aux = cursor.fetchone()
        ferramenta = type('', (), {})()
        ferramenta.id = aux[0]
        ferramenta.nome = aux[1]
        ferramenta.funcao = aux[2]
        ferramenta.descricao = aux[3]
        ferramenta.instancia = id_instancia
        return (ferramenta)
    elif(tipo == 'r'):
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
    elif(tipo == 'i'):
        cursor.execute(f"SELECT * FROM ingrediente WHERE id = {id_item}")
        aux = cursor.fetchone()
        ingrediente = type('', (), {})()
        ingrediente.id = aux[0]
        ingrediente.nome = aux[1]
        ingrediente.funcao = aux[2]
        ingrediente.descricao = aux[3]
        ingrediente.instancia = id_instancia
        return (ingrediente)


def get_posicao(id_pos):
    # retornar infos da posicao que o jogador se encontra no banco
    cursor.execute(f"SELECT * FROM posicao WHERE id = {id_pos}")
    aux = cursor.fetchone()
    position = type('', (), {})()
    position.id = aux[0]
    position.bioma = aux[2]
    position.norte = aux[3]
    position.sul = aux[4]
    position.leste = aux[5]
    position.oeste = aux[6]
    position.descricao = aux[7]
    position.pedras =  aux[8]
    position.madeiras = aux[9]
    return position


def set_pedras(id_pos, pedras):
    cursor.execute(f"UPDATE posicao SET pedras = {pedras} WHERE id = {id_pos}")
    conn.commit()
    return True


def get_instancia_item_por_id(id_item):
    cursor.execute(f"SELECT * FROM instancia_item WHERE id = {id_item}")
    return cursor.fetchall()


def set_item_equipado(id_jogador, id_instancia_item):
    cursor.execute(f"UPDATE jogador SET id_item_equipado = {id_instancia_item} WHERE id = {(id_jogador)}")
    conn.commit()
    return True
    


def get_item_equipado(id_jogado):
    cursor.execute(f"SELECT id_item_equipado FROM jogador WHERE id = {(id_jogado)}")
    id_item = cursor.fetchone()
    result = get_item_por_id_instancia(id_item[0]) if id_item[0] != None else None
    return result


def set_roupa_equipada(id_jogador, id_instancia_item):
    cursor.execute(f"UPDATE jogador SET id_roupa_equipada = {id_instancia_item} WHERE id = {(id_jogador)}")
    conn.commit()
    return True


def get_roupa_equipada(id_jogador):
    cursor.execute(f"SELECT id_roupa_equipada FROM jogador WHERE id = {id_jogador}")
    id_item = cursor.fetchone()
    result = get_item_por_id_instancia(id_item[0]) if id_item[0] != None else None
    return result


def add_instancia_item_possicao(id_pos, id_instancia):
    # adicionar linha na tabela instancia_item_posicao, retornar T/F
    cursor.execute(f"INSERT INTO instancia_item_posicao VALUES ({id_pos},{id_instancia})")
    conn.commit()
    return True


def get_instancia_item_posicao(id_pos):
    # retornar todos as instancia_item_posicao que tenha como id_posicao "id_pos"
    cursor.execute(f"SELECT id_instancia_item FROM instancia_item_posicao WHERE id_posicao = {id_pos}")
    aux = cursor.fetchone()
    result = []
    if aux:
        for i in aux:
            result.append(get_instancia_item_por_id(i))
    return result


def del_instancia_item_posicao(id_pos, id_instancia):
    # deletar linha na tabela instancia_item_posicao, retornar T/F
    cursor.execute(f"DELETE FROM instancia_item_posicao WHERE id_posicao = {id_pos} AND id_instancia_item = {id_instancia}")
    conn.commit()
    return cursor.fetchone()


def get_crafts(workbench):

    # retornar todos os crafts se 'workbench' == True
    if workbench:
        cursor.execute(f"SELECT * FROM craft")
    else:
        cursor.execute(f"SELECT * FROM craft WHERE necessita_workbench = 'false'")
    aux = cursor.fetchall()
    result = []
    if aux:
        for i in aux:
            item = get_item_por_id(i[0])
            craft = type('', (), {})()
            craft.id = i[0]
            craft.id_item1= i[1]
            craft.quant_item1 = i[2]
            craft.id_item2 = i[3]
            craft.quant_item2 = i[4]
            craft.id_item3 = i[5]
            craft.quant_item3 = i[6]
            craft.needs_workbench = i[7]
            craft.descricao = i[8]
            craft.nome = item.nome if item else None
            result.append(craft)
    return result

def get_item_por_id(id):
    try:
        cursor.execute(f"SELECT * FROM arma WHERE id = {id}")
        aux = cursor.fetchone()
        if aux:
            arma = type('', (), {})()
            arma.id = aux[0]
            arma.nome = aux[1]
            arma.dano = aux[2]
            arma.descricao = aux[3]
            return arma
    except:
        try:
            cursor.execute(f"SELECT * FROM ferramenta WHERE id = {id}")
            aux = cursor.fetchone()
            if aux:
                ferramenta = type('', (), {})()
                ferramenta.id = aux[0]
                ferramenta.nome = aux[1]
                ferramenta.defesa = aux[2]
                ferramenta.descricao = aux[3]
                return ferramenta
        except:
            try:
                cursor.execute(f"SELECT * FROM roupa WHERE id = {id}")
                aux = cursor.fetchone()
                if aux:
                    roupa = type('', (), {})()
                    roupa.id = aux[0]
                    roupa.nome = aux[1]
                    roupa.defesa = aux[2]
                    roupa.descricao = aux[3]
                    return roupa
            except:
                try:
                    cursor.execute(f"SELECT * FROM ingrediente WHERE id = {id}")
                    aux = cursor.fetchone()
                    if aux:
                        ingrediente = type('', (), {})()
                        ingrediente.id = aux[0]
                        ingrediente.nome = aux[1]
                        ingrediente.descricao = aux[2]
                        return ingrediente
                except:
                    return None;


def get_mochila_id(jogador):
    cursor.execute(f"SELECT id_mochila FROM jogador WHERE id = '{jogador.id}'")
    return cursor.fetchone()[0]

def verificar_inventario(id, id_item, quantidade = 1):
    # retornar True se o jogador possuir quantidade do item necessário, False se nao
    # SELECT 
    # COUNT(cod_serviço) AS quantidade
    # FROM tb_ordem_serviço
    # WHERE cod_serviço = 'A';
    cursor.execute(f"SELECT id_instancia_item FROM instancia_item WHERE id_item = {id_item}")
    aux = cursor.fetchone()
    if(len(aux) > quantidade):
        cursor.execute(f"SELECT id_instancia_item FROM mochila_guarda_instancia_de_item WHERE id_mochila = {get_mochila_id(id)} ")
        aux2 = cursor.fetchone()
        if(aux2 in aux):
            return True
    return False

def criar_instancia_item(id_item,tipo):
    # criar uma nova instancia de item e retornar seu id
    cursor.execute(f"INSERT INTO instancia_item VALUES (DEFAULT,{id_item},'{tipo}')")
    cursor.execute(f"SELECT id FROM instancia_item ORDER BY  id  DESC LIMIT 1;")
    conn.commit()
    return cursor.fetchone()[0]


def remover_item_iventario(id, id_item):

    id_mochila = get_mochila_id(id)
    cursor.execute(f"DELETE FROM mochila_guarda_instancia_de_item WHERE id_mochila = {id_mochila} AND id_instancia_item = {id_item}")
    conn.commit()
    return cursor.fetchall()
    

def adicionar_item_iventario(id, id_instancia_item):
    # adicionar item na mochila do jogador
    id_mochila = get_mochila_id(id)
    cursor.execute(f"INSERT INTO mochila_guarda_instancia_de_item VALUES ({id_mochila},{id_instancia_item})")
    conn.commit()
    return True


def get_bioma(id_bioma):
    cursor.execute(f"SELECT * FROM bioma WHERE id = {id_bioma}")
    aux = cursor.fetchone()
    bioma = type('', (), {})()
    bioma.id = aux[0]
    bioma.chance_batalha = aux[1]
    bioma.delta_temp = aux[2]
    bioma.nome = aux[3]
    bioma.nivel = aux[4]
    return bioma

def get_monstros_by_pos(id_pos):
    cursor.execute(f"SELECT * FROM monstro WHERE id_posicao = {id_pos}")
    aux = cursor.fetchone()
    monstros = []
    try:
        aux = list(aux)[::-1]
        while aux:
            monstro = type('', (), {})()
            monstro.id = aux.pop()
            monstro.nome = aux.pop()
            monstro.dano = aux.pop()
            monstro.descricao = aux.pop()
            monstro.vida = aux.pop()
            monstro.isca = aux.pop()
            monstro.id_posicao = aux.pop()
            monstros.append(monstro)
    finally:
        return monstros


def del_monstro(id_monstro):
    try:
        cursor.execute(f"DELETE FROM monstro WHERE id = {id_monstro}")
        conn.commit()
        return True
    except:
        return False