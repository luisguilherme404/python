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

    num1 = int(input("\n1º -> Informe um número inteiro (-1 para sair): "))

    if num1 == -1:  #se num1 = -1 o programa é finalizado
        print("Programa finalizado.\n")
        break

    num2 = int(input("2º -> Informe um número inteiro: "))
    #print("\n")

    if num1 > num2:     #se num1 for maior que num2 troque os valores das variáveis
        num1, num2 = num2, num1     


    for i in range(num1, num2 + 1):  #o for atribui o valor de num1, num2 ao i para o próximo for; ex: num1=2, num2=11 -> i = 2 a 10
        primo = True

        if i <= 1:          #se i <= 1 já considera como não primo e nem exibe
            primo = False
        else:
            for divisores in range(2, i):           #percorre do 2 ao valor de i; ex: i=3 entre 3 e 2 só existe o 2, 3 % 2 o resto é 1, então é primo     
                                                    #i = 4, entre 4 e 2 existe 2 e 3, 4%2 tem resto 0, então não é primo
                if i % divisores == 0:  #se i = 3; 
                    primo = False
                    break

            if primo:
                print("Número primo:", i)