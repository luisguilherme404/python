"""

019 - Crie a classe Livro que vai simular a passagem de páginas de um livro, considerando também se o usuário 
chegou ao fim da leitura.

"""

class Livro:

    def __init__(self, titulo = None, pag = 0):
        self.pagina = pag
        self.titulo = titulo

    def dados(self):

        if self.pagina == 0:
            return f'Título: {self.titulo}\nPág.: {self.pagina}. Abra o livro para começar a leitura.'

        elif self.pagina == 10:
            return f'Título: {self.titulo}\nPág.: {self.pagina}. Limite de página atingido.'
        else:
            self.pagina += 1
            return f'Título: {self.titulo}\nPág.: {self.pagina - 1} -> Pág.: {self.pagina}'

    def __str__(self):
        return f'\nVocê está na página: {self.pagina}\n'

leitura = Livro('Chapéuzinho Vermelho', 1)

def main():
    while True:
        print(leitura)

        mudarPg = input('Pular página (s/n): ')

        if mudarPg == 's' or mudarPg == 'S':
            print(leitura.dados())
        else:
            print('Leitura finalizada, por hoje.')
            break

main()
