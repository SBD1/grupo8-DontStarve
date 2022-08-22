import bd
import random
import menu

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