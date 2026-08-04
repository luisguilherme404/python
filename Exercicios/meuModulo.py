def saudar (nome):
    print(f'Olá, {nome}!')

def calcular(a, b):
    return a + b

def msgExcecao(msg):       #não precisa da var msg
    if msg:                #usado somente com a var msg e por estar usando valores booleanos
        print('\nATENÇÃO: você finalizou o programa com o atalho \'CTRL + C\'')

def numPrimos(num):

    primo = True

    if num <= 1:
        primo = False

    else: 
        for i in range(2, num):

            if num % i == 0:
                primo = False
                break

    if primo:
        print(f'{num} é primo')
    else:
        print(f'{num} não é primo')
