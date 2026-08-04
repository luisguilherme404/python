def saudar (nome):
    print(f'Olá, {nome}!')

def calcular(a, b):
    return a + b

def msgExcecao(msg):       #não precisa da var msg
    if msg:                #usado somente com a var msg e por estar usando valores booleanos
        print('\nATENÇÃO: você finalizou o programa com o atalho \'CTRL + C\'')
