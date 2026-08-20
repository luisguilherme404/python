"""

017 - Crie a classe Produto, onde podemos cadastrar nome e o preço. Crie também um método
que mostre a etiqueta de preço do produto

"""
from rich.table import Table
from rich import print

class Produto:
    def __init__(self, nome = 'None', preco = 0):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        return f'{self.nome} - R$ {self.preco:.2f}'

    def __str__(self):
        return self.etiqueta()

produtos = []

while True:
    nome = input('\nInforme o nome do produto: ')
    custo = float(input('Informe o preço do produto: '))

    produto = Produto(nome, custo)
    produtos.append(produto)

    continuar = input('Deseja cadastrar outro produto (s/n): ')
    if continuar == 'n' or continuar == 'N':
        break

tabela = Table(title='\n[bold on black]PRODUTOS[/]') #título
tabela.add_column('Nome')   #coluna Nome
tabela.add_column('Preço')  #coluna Preço

for i in produtos:
    tabela.add_row(
        i.nome,
        f'R$ {i.preco:.2f}'
    )

print(tabela)
