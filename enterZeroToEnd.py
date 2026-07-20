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

while True:     #enquanto num for diferente de 0 continue inserindo um nº inteiro
    
    num = int(input("Enter a integer (0 to exit): "))
    maior = num
    menor = num

    if num > maior:
        maior = num
    if num < menor:
        menor = num

    if num == 0:
        break

    qtdNum += 1
    soma = soma + num

    if num > 0 or num < 0:
        media = soma / num
    else:
        media = 0


    
print(maior)
print(menor)


print(f"\n-> Numbers quantity (except 0): {qtdNum}")
print(f"-> Sum: {soma}")
print(f"->Média: {media}")
