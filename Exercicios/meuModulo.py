#========= EXEMPLOS TEÓRICOS =========
def saudar (nome):
    print(f'Olá, {nome}!')

#========= MENSAGEM PARA O EXCEPT =========
def msgExcecao(msg):       #não precisa da var msg
    if msg:                #usado somente com a var msg e por estar usando valores booleanos
        print('\nATENÇÃO: você finalizou o programa com o atalho \'CTRL + C\'')

#========= FUNÇÃO PARA NÚMEROS PRIMOS =========
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


#========= FUNÇÃO PARA CALCULADORA (+, -, *, /) =========
def soma(a, b):
    soma = a + b
    print("Resultado: ", soma)

def subtrair(a, b):
    subtrair = a - b
    print('Resultado: ', subtrair)

def multiplicar(a, b):
    multiplicar = a * b
    print('Resultado: ', multiplicar)

def dividir(a, b):
    try:
        divisao = a / b
        print(f'Resultado: {divisao}')
        
    except ZeroDivisionError:
        print('Não é possível dividir por ZERO.')


