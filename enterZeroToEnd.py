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

maior = 0
menor = 0

while True:     #enquanto num for diferente de 0 continue inserindo um nº inteiro
    
    num = int(input("Enter a integer (0 to exit): "))

    if num == 0:
        break

    #maior número
    if qtdNum == 0:
        maior = num
        menor = num
    
    else:

        if num > maior:
            maior = num

        if num < menor:
            menor = num
    
    qtdNum += 1
    soma += num                   #soma = soma + num

    if num > 0 or num < 0:
        media = soma / qtdNum
    else:
        media = 0

print(f"\n-> Numbers quantity (except 0): {qtdNum}")
print(f"-> Sum: {soma}")
print(f"-> Média: {media}")
print("-> Maior número:", maior)
print("-> Menor número:", menor)