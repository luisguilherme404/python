import random
import time
import meuModulo

def tabuada(num):
    for i in range(0, 13):
        mult = num * i

        print(f'{num} x {i} = {mult}')
  
while True:

    try:
        
        num = random.randint(1, 10)

        print('\nNumber provided: {:^5}'.format(num))
        tabuada(num)
        time.sleep(3)


    except KeyboardInterrupt:
        meuModulo.msgExcecao(True)
        #meuModulo.msgExcecao()
        break