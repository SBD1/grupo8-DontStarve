# mock
# mock jogador
jogador = type('', (), {})()

jogador.id = 1
jogador.nome = 'player1'

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
# end mock

def get_jogos_salvos():
    # retornar todos os jog adores salvos em array
    return ['player1', 'player2']
    return []


def novo_jogador(nome: str):
    # inserir novo jogador no bd, em caso de falha retornar -1
    # em caso de sucesso:
    return nome


def get_posicao_jogador(nome: str):
    # pegar infos da posicao que o jogador se encontra no banco
    return get_posicao(jogador.id_posicao)


def set_posicao_jogador(nome, posicao):
    # setar posicao do jogador "nome" para "posicao"
    jogador.id_posicao = posicao


def get_inventario_por_tipo(jogador, tipo):
    # retornar todos as intancias de item associadas a mochila player.mochila no formato[[instancia, item], ...]
    a = []

    i = 0
    while True:
        i+=1

        b = []
        try:
            mochila = eval(f'item_mochila{i}')
            if mochila.id_mochila != 1:
                continue
        except:
            break

        instancia = get_instancia_item_por_id(mochila.id_instancia_item)
        b.append(instancia)

        if instancia.tipo != tipo:
            continue

        item = get_item_por_id(instancia.id_item)
        b.append(item)

        a.append(b)

    return a


def get_posicao(id_pos):

    # retornar posicao com id == id_pos
    if id_pos == 0:
        return pos0
    if id_pos == 1:
        return pos1
    if id_pos == 2:
        return pos2

    return -1


def set_pedras(id_pos, pedras):
    pos = eval("pos" + str(id_pos))
    pos.pedras = pedras


def get_instancia_item_por_id(id_item):
    if id_item == None:
        return None
    return eval(f'instancia_item{id_item}')

    
def get_item_por_id(id_item):
    if id_item == None:
        return None
    return eval(f'item{id_item}')


def set_item_equipado(nome_jogador, id_instancia_item):
    jogador.id_item_equipado = id_instancia_item


def get_item_equipado(nome_jogador):
    instancia_item_equipado = get_instancia_item_por_id(jogador.id_item_equipado)

    if instancia_item_equipado != None:
        item_equipado = get_item_por_id(instancia_item_equipado.id_item)
    else:
        item_equipado = None

    return [instancia_item_equipado, item_equipado]


def set_roupa_equipada(nome_jogador, id_instancia_item):
    jogador.id_roupa_equipada = id_instancia_item


def get_roupa_equipada(nome_jogador):
    instancia_roupa_equipada = get_instancia_item_por_id(jogador.id_roupa_equipada)

    if instancia_roupa_equipada != None:
        roupa_equipada = get_item_por_id(instancia_roupa_equipada.id_item)
    else:
        roupa_equipada = None

    return [instancia_roupa_equipada, roupa_equipada]


def add_instancia_item_possicao(id_pos, id_instancia):
    # adicionar linha na tabela instancia_item_posicao, retornar T/F
    instancia_item_posicao0.id_posicao = id_pos
    instancia_item_posicao0.id_instancia_item = id_instancia
    return True


def get_instancia_item_possicao(id_pos):
    # retornar todos as instancia_item_posicao que tenha como id_posicao "id_pos"
    if eval(f'instancia_item_posicao{id_pos}.id_posicao') == None:
        return []
    
    return [eval(f'instancia_item_posicao{id_pos}.id_instancia_item')]


def del_instancia_item_possicao(id_pos, id_instancia):
    # deletar linha na tabela instancia_item_posicao, retornar T/F
    instancia_item_posicao0.id_posicao = None
    instancia_item_posicao0.id_instancia_item = None
    return True


def get_crafts(workbench):

    # retornar todos os crafts se 'workbench' == True
    # todos que nao necessitam de workbench se 'workbench' == False
    
    if workbench:
        return [craft1, craft2, craft3]

    return [craft1, craft2]


def verificar_inventario(jogador, id_item, quantidade = 1):
    # retornar True se o jogador possuir quantidade do item necessario, False se nao
    # SELECT 
    # COUNT(cod_servico) AS quantidade
    # FROM tb_ordem_servico
    # WHERE cod_servico = 'A';

    quantidade_inventario = 0

    i = 0
    while True:
        i+=1

        try:
            item = eval(f'item_mochila{i}')
            if item.id_mochila != 1:
                continue
        except:
            break
        item = get_instancia_item_por_id(item.id_instancia_item)

        if item.id_item == id_item:
            quantidade_inventario += 1
        
        if quantidade_inventario == quantidade:
            return item
        
    
    return False


def criar_instancia_item(id_item):
    # criar uma nova instancia de item e retornar seu id

    if id_item == 1: # espada
        return 12
    if id_item == 11: # workbench
        return 11
    if id_item == 10: # corda
        return 10


def remover_item_iventario(jogador, id_item):

    i = 0
    while True:
        i+=1

        try:
            mochila = eval(f'item_mochila{i}')
        except:
            break
        
        item = get_instancia_item_por_id(mochila.id_instancia_item)

        if item.id_item == id_item:
            mochila.id_mochila = 0
            return
    

def adicionar_item_iventario(jogador, id_instancia_item):
    # adicionar item na mochila do jogador

    mochila = eval(f'item_mochila{id_instancia_item}')
    mochila.id_mochila = 1
    return True

# def get_posicoes_vizinhas(posicao_jogador):
#     vizinhos = []

#     vizinhos.append(posicao_jogador.norte) if posicao_jogador.norte != None else vizinhos.append(None)
#     vizinhos.append(posicao_jogador.sul) if posicao_jogador.sul != None else vizinhos.append(None)
#     vizinhos.append(posicao_jogador.leste) if posicao_jogador.leste != None else vizinhos.append(None)
#     vizinhos.append(posicao_jogador.oeste) if posicao_jogador.oeste != None else vizinhos.append(None)

#     return vizinhos