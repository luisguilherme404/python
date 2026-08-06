#Pedra, papel, tesoura

import random 
import time
import meuModulo

placarUser = 0
placarMq = 0
while True:
    try:
        maquina = random.randint(1, 3)
        escolha = int(input('\n0- Sair / 1 - Rock / 2 - Paper / 3 - Scissor: '))

    except KeyboardInterrupt:
        meuModulo.msgExcecao(True)
        break

    except ValueError:
        print('\nAVISO:\n1 - Saia do programa antes de tentar rodar novamente.'
              '\n2 - Escolha de acordo com as opções fornecidas no menu.'
              '\n3 - Tentou quebrar o código? °-°')
        continue

    #0 para sair
    if escolha == 0:
        print('Obrigado por jogar!')
        print('Programa finalizado...\n')
        time.sleep(1)
        break
    #caso o usuário insira qualqur outro nº fora das opções
    elif escolha < 0 or escolha > 3:
        for i in range(1, 4):
            print('Não fode, escolha entre as opções fornecidas. LERDÃO `-´')
            time.sleep(1)

    #pedra e papel
    if escolha == 1 and maquina == 2:
        placarMq += 1
        user = 'Pedra'
        maq = 'Papel'
        print(f'VOCÊ: {user}\nMÁQUINA: {maq}')
        print('========= MÁQUINA GANHOU! =========')
        
    elif maquina == 1 and escolha == 2:
        placarUser += 1
        user = 'Papel'
        maq = 'Pedra'
        print(f'VOCÊ: {user}\nMÁQUINA: {maq}')
        print('========= USUÁRIO GANHOU! =========')
        

    #papel e tesoura
    elif escolha == 2 and maquina == 3:
        placarMq += 1
        user = 'Papel'
        maq = 'Tesoura'
        print(f'VOCÊ: {user}\nMÁQUINA: {maq}')
        print('========= MÁQUINA GANHOU! =========')
        
    elif escolha == 3 and maquina == 2:
        placarUser += 1
        user = 'Tesoura'
        maq = 'Papel'
        print(f'VOCÊ: {user}\nMÁQUINA: {maq}')
        print('========= USUÁRIO GANHOU! =========')

    #empate
    #tesoura e pedra
    elif escolha == 1 and maquina == 3:
        placarUser += 1
        user = 'Pedra'
        maq = 'Tesoura'
        print(f'VOCÊ: {user}\nMÁQUINA: {maq}')
        print('========= USUÁRIO GANHOU! =========')

    #empate
    elif escolha == 3 and maquina == 1:
        placarMq += 1
        maq = 'Pedra'
        user = 'Tesoura'
        print(f'VOCÊ: {user}\nMÁQUINA: {maq}')
        print('========= MÁQUINA GANHOU! =========')

    #empate
    elif escolha == maquina:
        if escolha == 1:
            user = 'Pedra'
            maq = 'Pedra'

        elif escolha == 2:
            user = 'Papel'
            maq = 'Papel' 

        elif escolha == 3:
            user = 'Tesoura'
            maq = 'Tesoura'   

        print(f'VOCÊ: {user}\nMÁQUINA: {maq}')
        print('========= EMPATE! =========')

    print(f'-> Placar: Usuário {placarUser} x {placarMq} Máquina')
    