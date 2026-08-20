"""

017 - Crie a classe Produto, onde podemos cadastrar nome e o preço. Crie também um método
que mostre a etiqueta de preço do produto

"""
from rich.table import Table
from rich import print
itens = []

#característica padrão dos produtos cadastrados, vulgo classe
class Produto:
    #valores default
    def __init__(self, nome = 'None', preco = 0):
        self.nome = nome
        self.preco = preco

    #mostrar produtos em forma de tabela com a biblioteca rich
    def mostrarTabela(self):
        tabela = Table(title='\n[bold on black]PRODUTOS[/]') #título
        tabela.add_column('Nome')   #coluna Nome
        tabela.add_column('Preço')  #coluna Preço
        
        for i in itens:
            tabela.add_row(f'{i['Nome']}', f'R${i['Valor']:.2f}') #add linha a cada produto cadastrado

        return tabela   #exibir tabela

    def __str__(self):
        return self.mostrarTabela() #chama a função de mostrar tabela

#while para cadastrar vários:
while True:
    #nome e preço do produto:
    nome = input('\nInforme o nome do produto: ')
    custo = float(input('Informe o preço do produto: '))

    #produtos cadastrados:
    produtos = {
        'Nome': nome,
        'Valor': custo
    }  

    #adicionar produtos cadastrados no fim da lista:
    itens.append(produtos)

    #objeto:
    produtoCadastrado = Produto(produtos['Nome'], produtos['Valor'])
    print(produtoCadastrado.__str__())
