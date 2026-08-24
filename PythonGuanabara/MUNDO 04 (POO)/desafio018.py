"""
018 - Crie a classe Churrasco, onde seja possível informar quantas pessoas vão participar
e mostre quanto de carne deve ser comprado, o custo total do churrasco e o preço 
por pessoa.

Considere: 
* Consumo por pessoa: 400g
* Preço: R$82,40/Kg
"""

from rich import print
from rich.traceback import install
install()

class Churrasco:
    def __init__(self, qtd = None, kg = None, cT = None, cP = None):
        self.qtdPessoas = qtd
        self.qtdCarne = kg
        self.custoTotal = cT
        self.custoPessoa = cP

    def __str__(self):
        return f'\n| Quantidade de pessoas: {self.qtdPessoas} \n| Quantidade de carne: {self.qtdCarne:.1f} [red on black]Kg[/] \n| Custo total: [blue bold]R${self.custoTotal:.2f}[/] \n| Custo por pessoa: [blue bold]R${self.custoPessoa:.2f}[/]'


valorKG = 82.4
qtdPadrao = 400/1000 #quilos

while True:
    pessoas = int(input('\nInforme quantas pessoas participarão: '))

    if pessoas == 0:
        print('Erro de divisão por zero.')
        break

    else:

        #comprar essa qtd de carne para x pessoas:
        comprarCarne = pessoas * qtdPadrao

        #valor da qtd de carne para x pessoas:
        valorTotal = comprarCarne * valorKG

        #valor dividido pela quantidade de pessoas
        valorIndividual = valorTotal/pessoas

        convidado = Churrasco(pessoas, comprarCarne, valorTotal, valorIndividual)
        print(f'{convidado}')
