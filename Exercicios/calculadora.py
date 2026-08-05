"""
Exercício 1 – Calculadora com módulo

Crie um módulo chamado meuModulo.py com as funções:

somar(a, b)
subtrair(a, b)
multiplicar(a, b)
dividir(a, b) (trate divisão por zero)

Depois, crie um arquivo main.py que:

Importe o módulo.
Peça dois números ao usuário.
Mostre um menu de operações.
Execute a operação escolhida.

Exemplo:

Digite o primeiro número: 10
Digite o segundo número: 5

1 - Somar
2 - Subtrair
3 - Multiplicar
4 - Dividir

Escolha: 3

Resultado: 50
"""

import meuModulo
import random
import time


while True:
    
    try:
        n1 = random.randint(0, 10)
        n2 = random.randint(0, 10)

        print(f'\nNúmeros informados: {n1} e {n2}')

        print('Escolha uma das opções abaixo:')
        print('0 - Sair')
        print('1 - Somar')
        print('2 - Subtrair')
        print('3 - Multiplicar')
        print('4 - Dividir')
        escolha = int(input('-> Sua escolha: '))

        if escolha == 1:
            print('\n========= OPERADOR SOMA SELECIONADO =========')
            print(f'-> Operação: {n1} + {n2}')
            meuModulo.soma(n1, n2)

        elif escolha == 2:
            print('\n========= OPERADOR SUBTRAÇÃO SELECIONADO =========')
            print(f'-> Operação: {n1} - {n2}')
            meuModulo.subtrair(n1, n2)

        elif escolha == 3:
            print('\n========= OPERADOR MULTIPLICAÇÃO SELECIONADO =========')
            print(f'-> Operação: {n1} * {n2}')
            meuModulo.multiplicar(n1, n2)

        elif escolha == 4:
            print('\n========= OPERADOR DIVISÃO SELECIONADO =========')
            print(f'-> Operação: {n1} / {n2}')
            meuModulo.dividir(n1, n2)

        elif escolha == 0:
            print('Finalizando o programa...')
            time.sleep(1)
            break 

        else:
            for i in range(1, 10):
                print('Insira um número de acordo com as opções disponíveis. Lerdão.')
                time.sleep(1)
                
                if i == random.randint(1, 10):
                    break

    except KeyboardInterrupt:
        print('\nATENÇAO: você finalizou o programa com o atalho \'CTRL + C\'\n')
        break