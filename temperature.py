"""
Exercício — Pesquisa de Temperaturas

Uma estação meteorológica deseja registrar as temperaturas de um determinado dia.

Crie um programa que solicite ao usuário que digite temperaturas (números inteiros ou decimais).

A entrada de dados deve continuar até que o usuário digite 999, que será utilizado apenas 
para encerrar o programa (não deve ser considerado uma temperatura válida).

Ao final, o programa deve exibir:

Quantidade de temperaturas registradas.
Soma de todas as temperaturas.
Média das temperaturas.
Maior temperatura registrada.
Menor temperatura registrada.
Quantas temperaturas foram positivas.
Quantas temperaturas foram negativas.
Quantas temperaturas foram exatamente iguais a zero.

Exemplo de execução
Digite uma temperatura: 18
Digite uma temperatura: -3
Digite uma temperatura: 25
Digite uma temperatura: 0
Digite uma temperatura: 12
Digite uma temperatura: 999

Saída esperada (valores de exemplo):

Quantidade: 5
Soma: 52
Média: 10.4
Maior temperatura: 25
Menor temperatura: -3
Positivas: 3
Negativas: 1
Zeros: 1
"""

qtd = 0
soma = 0
media = 0
maior = 0
menor = 0
pos = 0
neg = 0
zero = 0

print("\n========= PESQUISA DE TEMPERATURAS =========\n")

while True:
    
    temp = int(input("* Informe uma temperatura (nº inteiro): "))

    if temp == 999:
        break

    #maior e menor
    if qtd == 0:
        maior = temp
        menor = temp

    else:
        if temp > maior:
            maior = temp

        if temp < menor:
            menor = temp

    qtd += 1            #qtd registrada
    soma += temp        #soma

    #positivas, negativas e zeros
    if temp > 0:
        pos += 1
    elif temp < 0:
        neg += 1
    else:
        zero += 1

#media
if temp > 0 or temp < 0:
    media = soma / qtd
              


print("\n-> Qtd de temperaturas registradas:", qtd)
print("-> Soma de todas as temperaturas:", soma)
print(f"-> Media de todas as temperaturas: {media}°")
print(f"-> Maior temperatura registrada: {maior}°")
print(f"-> Menor temperatura registrada: {menor}°")
print("-> Temperaturas positivas:", pos)
print("-> Temperaturas negativas:", neg)
print("-> Temperaturas igual a zero:", zero)

