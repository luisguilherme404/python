"""
Peça um número.

Mostre a tabuada de 1 até 20 usando for.

Exemplo:

7 x 1 = 7
7 x 2 = 14

...

7 x 20 = 140
"""

print("\n========= TABUADA =========\n")

num = int(input("Input a integer: "))
print('\n')

for i in range(1, 21):     #i começa de 1 e vai até 20
    print(f"{num} x {i} = {num * i}")
    #ex: 5 x 1 = 5, 5 x 2 = 10... até chegar em 5 x 20 = 100
    #i é o controlador, ele que tem os números do laço, no caso de 1 a 20