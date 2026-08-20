"""

017 - Crie a classe Produto, onde podemos cadastrar nome e o preço. Crie também um método
que mostre a etiqueta de preço do produto

"""
from rich.table import Table
from rich import print
itens = []

class Produto:
    def __init__(self, nome = 'None', preco = 0):
        self.nome = nome
        self.preco = preco

    def mostrarTabela(self):
        tabela = Table(title='\n[bold on black]PRODUTOS[/]')
        tabela.add_column('Nome')
        tabela.add_column('Preço')
        
        for i in itens:
            tabela.add_row(f'{i['Nome']}', f'R${i['Valor']:.2f}' )

        print(tabela)

    def __str__(self):
        return self.mostrarTabela()

def main(self):
    while True:
        nome = input('\nInforme o nome do produto: ')
        custo = float(input('Informe o preço do produto: '))

        produtos = {
            'Nome': nome,
            'Valor': custo
        }   
        itens.append(produtos)

        
        teste = Produto(produtos['Nome'], produtos['Valor'])
        #print(teste.__str__())

        print(self.mostrarTabela())

