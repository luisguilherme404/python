import time
import meuModulo
   
while True:
    num = int(input('\nInforme um nº inteiro (-1 para sair): '))
    if num == -1:
        print('Programa finalizado.\n')
        break
    meuModulo.numPrimos(num)


