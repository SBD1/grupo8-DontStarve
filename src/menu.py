import bd
import player
from jogo import jogo_init

_txt_init = '''\n
[1] Carregar jogo
[2] Novo Jogo
[0] Sair\n
'''

_txt_menu_jogador = '''\n
[1] Andar
[2] Inventario
[3] Craft
[0] Sair
'''

_txt_otp_invalida = '\n[-] Digite uma opcao valida!'


def clear():
    print(chr(27) + "[2J")


def menu_init():
    while True:
        clear()
        opt_init = -1
        jogador  = -1
        jogador_novo = True
        opt_init = input(_txt_init).strip()

        if opt_init == '1':
            jogador = menu_carregar_jogo()
            jogador_novo = False
            
            if jogador != -1:
                jogo_init(jogador, jogador_novo)
            continue

        if opt_init == '2':
            jogador = menu_novo_jogo()
            jogador_novo = True

            if jogador != -1:
                jogo_init(jogador, jogador_novo)
            continue

        if opt_init == '0':
            exit()
        
        print(_txt_otp_invalida)
        input("[i] precione enter para continuar")


def menu_carregar_jogo():
    jogos_salvos = []
    opt_carregar = -1
    index = 0
    clear()

    try:
        jogos_salvos = bd.get_jogos_salvos()
    except:
        print('\n[-] Nao foi possivel carregar lista de jogos salvos')
        input("[i] precione enter para continuar")
        return -1

    if jogos_salvos:
        for jogador in jogos_salvos:
            index += 1
            print(f'[{index}] {jogador}')
        print(f'\n[0] Cancelar')

    else:
        clear()
        print('\n[i] Voce nao possui jogos salvos!')
        input("[i] precione enter para continuar")
        return -1

    while True:
        opt_carregar = input().strip()

        try:
            opt_carregar = abs(int(opt_carregar))
        except:
            print(_txt_otp_invalida)
            continue

        if opt_carregar == 0:
            return -1 
        
        if opt_carregar <= index:
            clear()
            print('[+] Carregango jogo...')
            input("[i] precione enter para continuar")
            return jogos_salvos[index-2]
        
        print(_txt_otp_invalida)
        

def menu_novo_jogo():
    while True:
        clear()
        nome_jogador = input(
            '[?] Nome do peronagem: ').strip()

        if nome_jogador == '':
            print('[-] Nenhum nome inserido, jogador nao criado')
            input("[i] precione enter para continuar")
            return -1

        if bd.novo_jogador(nome_jogador) == -1:
            print('[-] Error ao criar novo peronagem. Tente novamente\n')
            input("[i] precione enter para continuar")
            return -1

        print('[+] Carregango jogo...')
        input("[i] precione enter para continuar")
        return nome_jogador

def menu_jogador(jogador):

    while True:
        clear()
        posicao_jogador = bd.get_posicao_jogador(jogador)
        print(posicao_jogador.descricao)

        print(_txt_menu_jogador)
        acao = input('[?] ').strip()

        if acao == '1':
            player.andar(jogador, posicao_jogador)

        if acao == '2':
            player.inventario(jogador)

        if acao == '3':
            player.craft(jogador, posicao_jogador)

        if acao == '0':
            return False