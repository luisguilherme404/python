""" 
ENUNCIADO:
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
possíveis informações sobre ele
"""
while True:

    try:
        x = input('\nEscreve um trem aí quaquer: ')
        print(f'\'{x}\' é alfa-numérico:', x.isalnum())
        print(f'\'{x}\' é uma palavra:', x.isalpha())
        print(f'\'{x}\' é um número:', x.isnumeric())
        print(f'\'{x}\' é um espaço:', x.isspace())
        print(f'\'{x}\' é uma palavra em MAIÚSCULO:', x.isupper())
        print(f'\'{x}\' é uma palavra em MINÚSCULO:', x.islower())
        
    except KeyboardInterrupt:
        print('\nATENÇÃO: você usou o atalho \'CTRL + C\' para finalizar o programa')
        break
