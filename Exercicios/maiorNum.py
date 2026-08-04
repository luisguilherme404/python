import random
import time

def maiorNum(n1, n2, n3):
    maior = n1
    
    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3
    
    print(f'O maior número é: {maior}\n')

while True:

    try:
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)
        num3 = random.randint(0, 100)

        i = 1

        print(f'\nNum{i}: {num1}')
        i+= 1
        print(f'Num{i}: {num2}')
        i+= 1
        print(f'Num{i}: {num3}')

        maiorNum(num1, num2, num3)

        time.sleep(5)

    except KeyboardInterrupt:
        print("-> ATENÇÃO: você finalizou o programa com o atalho 'CTRL + C.'\n")
        break






