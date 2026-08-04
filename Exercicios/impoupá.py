import random   #usando para gerar números aleatórios entre 0 e 100
import time     #usando para ter uma pausa de 1 segundo entre o texto 'nº gerado' e 'processando'

while True:

    try:
        print('========= PAR OU ÍMPAR =========\n')

        num = random.randint(0, 100)

        print(f'Número gerado: {num}')
        time.sleep(1)
        print('Processando...')
        time.sleep(1)

        if num % 2 == 0:  #se o resto da divisão de num por 2 for igual a 0 o número é par
            print('{} é par.'.format(num))
            
        else:
            print(f'{num} é ímpar')  #caso contrário, é ímpar

    except KeyboardInterrupt:
        print('\nATENÇÃO: o uso do atalho CTRL + C finalizou o programa.')
        break
                   