print('Bem vindo(a) a lanchonete da Camila Brazão')
print('=-' * 9, "Cardápio", '=-' * 9)
print(''' | CODIGO |       DESCRIÇÃO       |  VALOR  |
 |   100  |    CACHORRO QUENTE    |   9,00  |
 |   101  | CACHORRO QUENTE DUPLO |  11,00  |
 |   102  |        X - EGG        |  12,00  |
 |   103  |      X - SALADA       |  12,00  |
 |   104  |        X - BACON      |  14,00  |
 |   105  |        X - TUDO       |  17,00  |
 |   200  |  REFRIGERANTE LATA    |   5,00  |
 |   201  |      CHÁ GELADO       |   4,00  |''')
pedido = 0
dinheiro = 0
cachorroquente = 9
cachorroquente_duplo = 11
xegg = 12
xsalada = 12
xbacon = 14
xtudo = 17
refri_lata = 5
chagelado = 4
while True:
    cod = int(input('Entre com o código desejado: '))
    if cod == 100:
        pedido = 9
        print(f'Você pediu um cachorro quente no valor de R$ {cachorroquente}')

    elif cod == 101:
        pedido = 11
        print(f'Você pediu um cachorro quente duplo no valor de R$ {cachorroquente_duplo}')

    elif cod == 102:
        pedido = 12
        print(f'Você pediu um X- Egg no valor de R$ {xegg}')

    elif cod == 103:
        pedido = 12
        print(f'Você pediu um X - Salada no valor de R$ {xsalada}')

    elif cod == 104:
        pedido = 14
        print(f'Você pediu um X - Bacon no valor de R$ {xbacon}')

    elif cod == 105:
        pedido = 17
        print(f'Você pediu um X - Tudo no valor de R$ {xtudo}')

    elif cod == 200:
        pedido = 5
        print(f'Você pediu um refrigerante em lata no valor de R$ {refri_lata}')

    elif cod == 201:
        pedido = 4
        print(f'Você pediu um Chá gelado no valor de R$ {chagelado}')

    else:
        print('Opção inválida!!')
        continue

    print('Deseja pedir mais alguma coisa? ')
    print('1 - SIM')
    print('0 - NÃO')
    resposta = float(input())
    if resposta != 0:
        continue
    pedido += pedido
    print('O total do seu pedido é {}'.format(pedido))
    break