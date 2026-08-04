import random
import time
import meuModulo

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
        meuModulo.msgExcecao(True)
        break