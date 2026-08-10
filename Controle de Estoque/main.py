import funcoes
import time

while True:
    print('\n{:=^40}'.format(''))
    print('\tCONTROLE DE ESTOQUE')
    print('{:=^40}'.format(''))

    print('\n0 - Sair')
    print('1 - Cadastro de funcionário')
    print('2 - Equipes cadastradas')
    print('3 - Registro de retirada')
    print('4 - Lista de materiais retirados')
    escolha = int(input('-> Sua escolha: '))

    if escolha == 0:
        print('Programa finalizado...')
        #time.sleep(2)
        break
    elif escolha == 1:
        funcoes.cadastroDeEquipes()
    elif escolha == 2:
        funcoes.listaDeEquipes()
    elif escolha == 3:
        funcoes.registroDeRetiradas()
    elif escolha == 4:
        funcoes.listaDemateriaisRetirados()
        