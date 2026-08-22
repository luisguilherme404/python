"""
2. Classe Cachorro
Crie uma classe Cachorro com:

nome
raca
idade

Crie os métodos:

latir()
mostrar_dados()
"""

from rich import print
from rich.traceback import install
install()

class Cachorro:
    def __init__(self, nome = None, raca = None, idade = None):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def latir(self):
        return f'[yellow bold]{self.nome}[/]: Au au, ruf ruf'

    def mostrar_dados(self):
        return f'\nNome: [yellow bold]{self.nome}[/] | Raça: {self.raca} | Idade: {self.idade}'

animal1 = Cachorro('Simba', 'pinscher', 9)
print(animal1.latir(), animal1.mostrar_dados())

print('\n')

animal2 = Cachorro('Kenai', 'Pinscher', 1)
print(animal2.latir(), animal2.mostrar_dados())

animal3 = Cachorro()
print(animal3.mostrar_dados())