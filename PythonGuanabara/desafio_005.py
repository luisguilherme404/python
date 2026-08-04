"""
ENUNCIADO:
Faça um programa que leia um número inteiro e mostre na tela o seu antecessor e sucessor
"""
import random

def antecessor(num):
    antecessor = num - 1

    print('\nPredecessor: {:>8}'.format(antecessor))

def sucessor(num):
    sucessor = num + 1

    print('Successor: {:>8}\n'.format(sucessor))

num = random.randint(0, 100)

antecessor(num)
print('Number provided: {:^5}'.format(num))
sucessor(num)