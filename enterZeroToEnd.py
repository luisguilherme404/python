"""
Usando while.

Peça números infinitamente.

Quando digitar 0, pare.

No final mostre:

quantidade de números digitados
soma deles
média
"""
num = 1
soma = 0
qtdNum = 0

while num != 0:     #enquanto num for diferente de 0 continue inserindo um nº inteiro
    
    num = int(input("Input a integer (0 to break): "))

    if num != 0:
        qtdNum += 1             #maneira 1 de contar os números
        soma = soma + num       #soma += num

    else:                       #não precisa do else
        #qtdNum -= 1            #maneira 2 de contar os números
        break
    
    media = soma / qtdNum

print(f"\n-> Numbers quantity (except 0): {qtdNum}")
print(f"-> Sum: {soma}")
print(f"->Média: {media}")
