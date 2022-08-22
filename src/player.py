import bd
import menu
import world

def andar(jogador, posicao_jogador):
    menu.clear()

    if posicao_jogador.norte != None: # nao retirar o None, pode existir id 0
        print('[1] Norte')
    if posicao_jogador.sul != None:
        print('[2] Sul')
    if posicao_jogador.leste != None:
        print('[3] Leste')
    if posicao_jogador.oeste != None:
        print('[4] Oeste')

    print('[0] Nao andar')

    while True:
        opt_andar = input('[?] ').strip()

        try:
            opt_andar = abs(int(opt_andar))
        except:
            print(menu._txt_otp_invalida)
            continue

        if opt_andar == 1 and posicao_jogador.norte != None:
            bd.set_posicao_jogador(jogador, posicao_jogador.norte)
            return True
        if opt_andar == 2 and posicao_jogador.sul != None:
            bd.set_posicao_jogador(jogador, posicao_jogador.sul)
            return True
        if opt_andar == 3 and posicao_jogador.leste != None:
            bd.set_posicao_jogador(jogador, posicao_jogador.leste)
            return True
        if opt_andar == 4 and posicao_jogador.oeste != None:
            bd.set_posicao_jogador(jogador, posicao_jogador.oeste)
            return True

        if opt_andar == 0:
            return True

        print(menu._txt_otp_invalida)
        

def inventario(jogador):
    menu.clear()

    item_equipado = bd.get_item_equipado(jogador)
    if item_equipado[1]:
        print(f'[i] Item equipado:  {item_equipado[1].nome}')

    roupa_equipada = bd.get_roupa_equipada(jogador)
    if roupa_equipada[1]:
        print(f'[i] Roupa equipado: {roupa_equipada[1].nome}')

    print("\n[1] Armas")
    print("[2] Roupas")
    print("[3] Ferramentas")
    print("[4] Ingredientes")
    print("[0] Fechar inventario")

    while True:
        inventario = []
        opt_inventario = input('[?] ').strip()

        try:
            opt_inventario = abs(int(opt_inventario))
        except:
            print(menu._txt_otp_invalida)
            continue

        if opt_inventario == 1:
            inventario = bd.get_inventario_por_tipo(jogador, 'a')
            inventario_armas(jogador, inventario)
            return True

        if opt_inventario == 2:
            inventario = bd.get_inventario_por_tipo(jogador, 'r')
            inventario_roupas(jogador, inventario)
            return True
            
        if opt_inventario == 3:
            inventario = bd.get_inventario_por_tipo(jogador, 'f')
            inventario_ferramentas(jogador, inventario)
            return True
            
        if opt_inventario == 4:
            inventario = bd.get_inventario_por_tipo(jogador, 'i')
            inventario_ingredientes(jogador, inventario)
            return True
            
        if opt_inventario == 0:
            return True

        print(menu._txt_otp_invalida)
        

def inventario_armas(jogador, inventario):

    while True:
        menu.clear()
        print('[i] Armas\n')

        i = 1
        for item in inventario:
            print(f'[{i}] {item[1].nome}')
            i+=1
        print('[0] Voltar')
        opt_arma = input('[?] ').strip()

        try:
            opt_arma = abs(int(opt_arma))
        except:
            print(menu._txt_otp_invalida)
            continue

        if opt_arma > len(inventario):
            print(menu._txt_otp_invalida)
            input('[i] precione ENTER para continuar')
            continue
            
        if opt_arma == 0:
            return True

        menu.clear()
        print(f"[i] Nome:      {inventario[opt_arma-1][1].nome}")
        print(f"[i] Descricao: {inventario[opt_arma-1][1].descricao}")
        print(f"[i] Dano:      {inventario[opt_arma-1][1].dano}")

        print(f"\n[?] Equipar {inventario[opt_arma-1][1].nome}? (S/N)")

        if(input('[?]').lower() == 's'):
            bd.set_item_equipado(jogador, inventario[opt_arma-1][0].id)
        else:
            continue

        


def inventario_roupas(jogador, inventario):
    while True:
        menu.clear()
        print('[i] Roupas\n')

        i = 1
        for item in inventario:
            print(f'[{i}] {item[1].nome}')
            i+=1
        print('[0] Voltar')
        opt_roupa = input('[?] ').strip()

        try:
            opt_roupa = abs(int(opt_roupa))
        except:
            print(menu._txt_otp_invalida)
            continue

        if opt_roupa > len(inventario):
            print(menu._txt_otp_invalida)
            input('[i] precione ENTER para continuar')
            continue
            
        if opt_roupa == 0:
            return True

        menu.clear()
        print(f"[i] Nome:             {inventario[opt_roupa-1][1].nome}")
        print(f"[i] Descricao:        {inventario[opt_roupa-1][1].descricao}")
        print(f"[i] Protecao Termica: {inventario[opt_roupa-1][1].protecao_termica}")
        print(f"[i] Protecao Fisica:  {inventario[opt_roupa-1][1].protecao_termica}")

        print(f"\n[?] Equipar {inventario[opt_roupa-1][1].nome}? (S/N)")

        if(input('[?] ').lower() == 's'):
            bd.set_roupa_equipada(jogador, inventario[opt_roupa-1][0].id)
        else:
            continue

def inventario_ferramentas(jogador, inventario):
    while True:
        menu.clear()
        print('[i] Ferramentas\n')

        i = 1
        for item in inventario:
            print(f'[{i}] {item[1].nome}')
            i+=1
        print('[0] Voltar')
        opt_ferramenta = input('[?] ').strip()

        try:
            opt_ferramenta = abs(int(opt_ferramenta))
        except:
            print(menu._txt_otp_invalida)
            continue

        if opt_ferramenta > len(inventario):
            print(menu._txt_otp_invalida)
            input('[i] precione ENTER para continuar')
            continue
            
        if opt_ferramenta == 0:
            return True

        menu.clear()
        print(f"[i] Nome:             {inventario[opt_ferramenta-1][1].nome}")
        print(f"[i] Descricao:        {inventario[opt_ferramenta-1][1].descricao}")

        print(f"\n[?] Usar {inventario[opt_ferramenta-1][1].nome}? (S/N)")

        if(input('[?] ').lower() == 's'):
            funcao = inventario[opt_ferramenta-1][1].funcao
            try:
                eval('world.'+ funcao)
                return
            except:
                print('[-] Nao foi possivel utilizar a ferramenta')
                input("[i] precione enter para continuar")
        else:
            continue

def inventario_ingredientes(jogador, inventario):
    while True:
        menu.clear()
        print('[i] Ingredientes\n')

        i = 1
        for item in inventario:
            print(f'[{i}] {item[1].nome}')
            i+=1
        print('[0] Voltar')
        opt_ingrediente = input('[?] ').strip()

        try:
            opt_ingrediente = abs(int(opt_ingrediente))
        except:
            print(menu._txt_otp_invalida)
            continue

        if opt_ingrediente > len(inventario):
            print(menu._txt_otp_invalida)
            input('[i] precione ENTER para continuar')
            continue
            
        if opt_ingrediente == 0:
            return True
        
        menu.clear()
        print(f"[i] Nome:             {inventario[opt_ingrediente-1][1].nome}")
        print(f"[i] Descricao:        {inventario[opt_ingrediente-1][1].descricao}")

        print(f"\n[?] Usar {inventario[opt_ingrediente-1][1].nome}? (S/N)")

        if(input('[?] ').lower() == 's'):
            funcao = inventario[opt_ingrediente-1][1].funcao
            try:
                print('world.'+ funcao)
                eval('world.'+ funcao)
            except:
                print('[-] Nao foi possivel utilizar o ingrediente')
                input("[i] precione enter para continuar")
        else:
            continue

def craft(jogador, posicao):
    while True:
        menu.clear()
        print('[i] Craft\n')

        itens_na_pos = bd.get_instancia_item_possicao(posicao.id)

        if itens_na_pos:
            for item_na_pos in itens_na_pos:
                if item_na_pos.id_item == 11: # workbench:
                    lista_crafts = bd.get_crafts(True)
                else: 
                    lista_crafts = bd.get_crafts(False)
        else:
            lista_crafts = bd.get_crafts(False)

        i = 1
        for craft in lista_crafts:
            print(f'[{i}] {craft.nome}')
            i+=1
        print('[0] Voltar')
        opt_craft = input('[?] ').strip()

        try:
            opt_craft = abs(int(opt_craft))
        except:
            print(menu._txt_otp_invalida)
            continue

        if opt_craft > len(lista_crafts):
            print(menu._txt_otp_invalida)
            input('[i] precione ENTER para continuar')
            continue
            
        if opt_craft == 0:
            return True

        menu.clear()
        print(f"[i] Nome:             {lista_crafts[opt_craft-1].nome}")
        print(f"[i] Materiais:        {lista_crafts[opt_craft-1].descricao}")

        print(f"\n[?] Construis {lista_crafts[opt_craft-1].nome}? (S/N)")

        if(input('[?] ').lower() == 's'):
            crafitar(jogador, lista_crafts[opt_craft-1])
        else:
            continue

def crafitar(jogador, craft):

    if craft.id_item1:
        if not bd.verificar_inventario(jogador, craft.id_item1, craft.quant_item1):
            print('[-] Voce nao possui todos os ingredientes necessarios')
            input('[i] precione ENTER para continuar')
            return False

    if craft.id_item2:
        if not bd.verificar_inventario(jogador, craft.id_item2, craft.quant_item2):
            print('[-] Voce nao possui todos os ingredientes necessarios')
            input('[i] precione ENTER para continuar')
            return False
    
    if craft.id_item3:
        if not bd.verificar_inventario(jogador, craft.id_item3, craft.quant_item3):
            print('[-] Voce nao possui todos os ingredientes necessarios')
            input('[i] precione ENTER para continuar')
            return False

    if craft.id_item1:
        for i in range(craft.quant_item1):
            bd.remover_item_iventario(jogador, craft.id_item1)

    if craft.id_item2:
        for i in range(craft.quant_item2):
            bd.remover_item_iventario(jogador, craft.id_item2)

    if craft.id_item3:
        for i in range(craft.quant_item3):
            bd.remover_item_iventario(jogador, craft.id_item3)
    
    instancia_criada = bd.criar_instancia_item(craft.id_item_resultado)

    bd.adicionar_item_iventario(jogador, instancia_criada)
    return True

