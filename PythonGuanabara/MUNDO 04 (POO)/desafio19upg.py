"""

019 - Crie a classe Livro que vai simular a passagem de páginas de um livro, considerando também se o usuário 
chegou ao fim da leitura.

"""
from rich import print

class Livro:

    def __init__(self, titulo = None, limiteInicial = 10):
        self.titulo = titulo
        self.paginaLimite = limiteInicial
        self.pagina = 1 #inicializo o livro na pág 1

    def pularPg(self, skip = 0):
        self.skip = skip    #recebe a qtd de pág que serão puladas

        self.pagina += self.skip

        if self.pagina < self.paginaLimite:

            for i in range(1, self.pagina + 1):
                print(f'[blue]Pág.: {i}[/] ', end='-> ')
                
        else: 
            self.pagina = self.paginaLimite
            for i in range(1, self.pagina + 1):
                print(f'[blue]Pág.: {i}[/] ', end='-> ')

            print('Você atingiu o limite de páginas do livro.')

    def __str__(self):
        return f"\n\n-> Leitura do Livro '{self.titulo}' que possui {self.paginaLimite} páginas. Você está lendo a página: {self.pagina}\n"

titulo = input('Informe o título do livro: ')
paginaFinal = int(input('Informe o número da última página: '))
pularPg = int(input('Informe quantas páginas você quer pular: '))

leitura = Livro(titulo, paginaFinal)
leitura.pularPg(pularPg)
print(leitura)
