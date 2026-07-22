"""
🎯 Próximo desafio

Agora eu te proporia um exercício que junta tudo isso:

Peça dois números inteiros e mostre todos os números primos existentes entre eles.

Exemplo:

Início: 10
Fim: 30

Primos encontrados:

11
13
17
19
23
29

Esse exercício vai obrigar você a usar:

input()
for dentro de for (laços aninhados)
%
if
break
variável primo

É um excelente desafio para consolidar tudo o que você aprendeu até agora.
"""

while True:

    num1 = int(input("1º -> Informe um número inteiro (-1 para sair): "))

    if num1 == -1:
        break

    num2 = int(input("2º -> Informe um número inteiro (-1 para sair): "))


    for i in range(num1, num2):     #i percorre do num1 até num2
        primo = True

        for divisores in range(2, i):        

            if i <= 1:
                primo = False
                break
            
            else:
                if i % divisores == 0:
                    primo = False
                    break
        if primo:
            print(i)
                   
