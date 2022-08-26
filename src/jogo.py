import bd
import menu

def jogo_init(jogador: str, first_time: bool):

    menu.clear()

    if first_time:
        print('[i] Tutorial \n')

    while menu.menu_jogador(jogador):
        # menu.clear()
        continue
