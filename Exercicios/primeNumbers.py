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
while True:     #repetição até eu digitar -1

    #número primo é todo aquele número que se divide por ele mesmo e por 1, SOMENTE.
    num = int(input("Informe um número inteiro (-1 para sair): "))
    if num == -1:
        break

    primo = True        # assumimos inicialmente que o número é primo

    if num <= 1:        #se num for = 0 ou 1 -> False: não é primo
        primo = False

    else:
        for divisores in range(2, num): #divisores recebe os nº entre 2 e o número inserido

            if num % divisores == 0:    #se o resto da divisão entre num e o divisor for 0 ele não é primo
                primo = False           #quer dizer que se num for divisível por um nº além de 1 e dele mesmo o número tem outros divisores (não primo); obs: (DIFÍCIL)
                break

    if primo:
        print(f"{num} é primo\n")
    else:
        print(f"{num} não é primo\n")

# o programa começa considerando que todos os nº são primos, logo eu preciso de um critério para negar, então no range eu 
# tenho os divisores (com exceção daqueles que são divisíveis para todos: 1 e o próprio nº)     
    