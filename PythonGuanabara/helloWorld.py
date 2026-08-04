import random

num = random.randint(0, 100)

if num % 2 == 0:  #se o resto da divisão de num por 2 for igual a 0 o número é par
    print('{} é par.'.format(num))
    
else:
    print(f'{num} é ímpar')  #caso contrário, é ímpar