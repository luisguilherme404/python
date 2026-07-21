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


num = int(input("Informe um número inteiro: "))

for divisores in range(1, num + 1):

    if num <= 1:
        print(f"{num} não é primo.")
        break

    if num % divisores == 0:
        divisores += 1
        print(f"{num} é primo")
    if num % divisores > 0:
        print("Não é primo")

            


            
    


