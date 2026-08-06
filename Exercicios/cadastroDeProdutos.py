"""
Cadastro de produtos

Você precisa criar um programa para cadastrar produtos.

Cada produto possui:

nome
preco
quantidade

Os produtos devem ficar armazenados em uma lista de dicionários.

Estrutura esperada:

produtos = [
    {
        "nome": "Arroz",
        "preco": 25.50,
        "quantidade": 3
    },
    {
        "nome": "Feijão",
        "preco": 8.50,
        "quantidade": 5
    }
]
Crie estas funções:
def adicionar_produto():
    pass

def listar_produtos():
    pass

def calcular_valor_total():
    pass
O menu deve ser:
===== ESTOQUE =====

0 - Sair
1 - Adicionar produto
2 - Listar produtos
3 - Valor total do estoque
Regras

Adicionar produto:

O programa pergunta:

Nome:
Preço:
Quantidade:

E adiciona um dicionário à lista.

Listar:

Mostre algo parecido com:

Produto: Arroz
Preço: R$ 25.50
Quantidade: 3

Produto: Feijão
Preço: R$ 8.50
Quantidade: 5

Valor total:

Para cada produto:

preço × quantidade

Depois some todos.

Por exemplo:

Arroz: 25.50 × 3 = 76.50
Feijão: 8.50 × 5 = 42.50

Valor total: R$ 119.00
"""
import random
import time

produtos = []
valor = []
while True:

    def adicionar():
        nome = input('\nInforme o nome do produto: ')
        valor = float(input('Informe o preço do produto: R$ '))
        qtdProdutos = int(input('Informe a quantidade de produtos:'))

        produto = {
                'Nome': nome,
                'Valor': valor,
                'Quantidade': qtdProdutos
                    }
        
        produtos.append(produto)

    def lista():
        for percorrer in produtos:
            print(percorrer)

    def valores():
        soma = 0

        #valor total
        for percorrer in produtos:  
            soma += percorrer['Valor']

        print(f'Valor total: {soma}')
            
    adicionar()
    lista()
    valores()
