"""
Exercício 5 — Descobrindo Primos

Peça um número.

Descubra se ele é primo.

Exemplo:

Digite: 29

29 é primo

ou

Digite: 24

24 não é primo

Esse exercício força bastante o raciocínio com for, % e if.
"""

divisores = 1

num = int(input("Informe um número inteiro: "))

for sla in range(1, num):

    if num % sla == 0:
        divisores += 1
        

print(divisores)