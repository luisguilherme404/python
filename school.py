"""
Exercício 6 — Análise de Idades

Uma escola deseja registrar a idade dos alunos de uma turma.

Crie um programa que permita ao usuário digitar várias idades.

O programa deve continuar pedindo idades até que o usuário digite -1.

Ao final, exiba:

Quantidade de idades informadas.
Soma de todas as idades.
Média das idades.
Maior idade.
Menor idade.
Quantas pessoas são maiores de idade (18 anos ou mais).
Quantas pessoas são menores de idade.
"""
quantity = 0
soma = 0
media = 0
qtdMaiores = 0
qtdMenores = 0

print("\n")

while True:
    age = int(input("Informe sua idade (-1 para sair): "))
    if age == -1:
        break

    if quantity == 0:
        maior = age
        menor = age

    quantity += 1
    soma += age
    media = soma / quantity

    if maior < age:
        maior = age

    if menor > age:
        menor = age        

    if age >= 18:
        qtdMaiores += 1
    else:
        qtdMenores += 1


print("\nQtd de idades inseridas:", quantity)
print("Soma de todas as idades:", soma)
print("Média entre as idades:", media)
print("Maior idade inserida:", maior)
print("Menor idade inserida:", menor)
print("Quantos maiores de idade:", qtdMaiores)
print("Quantos menores de idade:", qtdMenores)





        


