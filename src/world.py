import bd
import random
import menu
import player

def pegar_pedra(jogador, nivel):
    posicao = bd.get_posicao_jogador(jogador)
    sorte = random.uniform(.5, 1.5)

    quant_pedras_pegas = round(sorte * nivel * 10)
    quant_pedras_pegas = min(quant_pedras_pegas, posicao.pedras)

    menu.clear()

    if quant_pedras_pegas > 0:
        bd.set_pedras(posicao.id, posicao.pedras - quant_pedras_pegas)
        print(f'[i] {jogador} pegou {quant_pedras_pegas} pedras')
    else:
        print(f'[i] Nao ha pedras por aqui')

    input("\n[i] precione enter para continuar")
    return 

def colocar_na_pos(jogador, id_item):
    instancia_item = bd.verificar_inventario(jogador, id_item)
    bd.add_instancia_item_possicao(0, instancia_item)
    bd.remover_item_iventario(jogador, instancia_item.id_item)


def verificar_luta(jogador, id_pos):

    pos = bd.get_posicao(id_pos)
    bioma = bd.get_bioma(pos.bioma)

    sorte = random.uniform(0, 1)
    if sorte <= bioma.chance_batalha:

        monstros = bd.get_monstros_by_pos(id_pos)
        if len(monstros) == 0:
            return

        foo = random.randint(0,len(monstros)-1)
        monstro = monstros[foo]
        luta(jogador, monstro)



def luta(jogador, monstro):
    jogador = bd.get_jogador()

    menu.clear()
    print(f'[i] um {monstro.nome} selvagem apareceu!')
    print(f'[i] {monstro.descricao}')
    input("[i] precione ENTER para continuar")

    vida_jogador = jogador.vida - (monstro.dano*2)

    if(vida_jogador <= 0):
        player.morte(jogador.id)

    menu.clear()
    print(f'[i] voce levou {monstro.dano*2} de dano, mas matou o monstro')
    input("[i] precione ENTER para continuar")
    bd.set_vida_jogador(jogador, vida_jogador)
    bd.del_monstro(monstro.id)




