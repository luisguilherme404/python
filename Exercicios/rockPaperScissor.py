#Pedra, papel, tesoura

import random
import time

placarUser = 0
placarMq = 0
while True:
    
    maquina = random.randint(1, 3)
    escolha = int(input('\n0- Sair / 1 - Rock / 2 - Paper / 3 - Scissor: '))
    if escolha == 0:
        print('Programa finalizado...\n')
        time.sleep(1)
        break
    elif escolha < 1 or escolha > 3:
        for i in range(1, 4):
            print('Não fode, escolha entre 1 e 3. LERDÃO `-´')
            time.sleep(1)

    #pedra e papel
    if escolha == 1 and maquina == 2:
        placarMq += 1
        user = 'Pedra'
        maq = 'Papel'
        print(f'VOCÊ: {user}\nMÁQUINA: {maq}')
        print('========= MÁQUINA GANHOU! =========')
        #print(f'-> Placar: Usuário {placarUser} x {placarMq} Máquina')
        
    elif maquina == 1 and escolha == 2:
        placarUser += 1
        user = 'Papel'
        maq = 'Pedra'
        print(f'VOCÊ: {user}\nMÁQUINA: {maq}')
        print('========= USUÁRIO GANHOU! =========')
        #print(f'-> Placar: Usuário {placarUser} x {placarMq} Máquina')
        

    #papel e tesoura
    elif escolha == 2 and maquina == 3:
        placarMq += 1
        user = 'Papel'
        maq = 'Tesoura'
        print(f'VOCÊ: {user}\nMÁQUINA: {maq}')
        print('========= MÁQUINA GANHOU! =========')
        #print(f'-> Placar: Usuário {placarUser} x {placarMq} Máquina')
        
    elif escolha == 3 and maquina == 2:
        placarUser += 1
        user = 'Tesoura'
        maq = 'Papel'
        print(f'VOCÊ: {user}\nMÁQUINA: {maq}')
        print('========= USUÁRIO GANHOU! =========')
        #print(f'-> Placar: Usuário {placarUser} x {placarMq} Máquina')

    #tesoura e pedra
    elif escolha == 1 and maquina == 3:
        placarUser += 1
        user = 'Pedra'
        maq = 'Tesoura'
        print(f'VOCÊ: {user}\nMÁQUINA: {maq}')
        print('========= USUÁRIO GANHOU! =========')
        #print(f'-> Placar: Usuário {placarUser} x {placarMq} Máquina')

    elif escolha == 3 and maquina == 1:
        placarMq += 1
        maq = 'Pedra'
        user = 'Tesoura'
        print(f'VOCÊ: {user}\nMÁQUINA: {maq}')
        print('========= MÁQUINA GANHOU! =========')
        #print(f'-> Placar: Usuário {placarUser} x {placarMq} Máquina')

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