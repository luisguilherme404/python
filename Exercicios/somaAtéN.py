import random
import time

def soma(num):
    soma = 0
    for i in range(1, num + 1):
        soma += i
    return soma   

while True:
    try:
        n = random.randint(0, 10)
        print(f'\nNum gerado: {n}')
        print(f'Soma: {soma(n)}')

        time.sleep(3)

    except KeyboardInterrupt:
        print('\nATENÇÃO: você usou o atalho \'CTRL + C\' para finalizar o programa')
        break