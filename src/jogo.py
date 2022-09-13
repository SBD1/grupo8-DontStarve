import bd
import menu
tutorial = """Esse é um jogo de aventura, onde você deve explorar o mundo e coletar recursos para sobreviver.
Os recurso disponiveis são: madeira, pedras
Com esse recursos pode craftar itens, que podem ser usados para sobreviver ou para lutar contra monstros.
os itens são picareta,machado,espada
Para se locomover ande para o norte,sul,leste,oeste
cada posição tem um bioma, que pode ser floresta, deserto, pantano ou tundra
os recursos em cada biomas são diferentes
os monstros também são diferentes em cada bioma
existe uma chance de lutar contra um monstro em cada posição
mas cuidado, se você morrer, o jogo acaba
boa sorte!

Dica: o primeiro bioma que você deve explorar é a floresta, pois lá tem muita madeira e pedras

"""

def jogo_init(jogador: str, first_time: bool):

    menu.clear()

    if first_time:
        print(tutorial)
        input('[i] precione ENTER para continuar')

    while menu.menu_jogador(jogador):
        # menu.clear()
        continue
