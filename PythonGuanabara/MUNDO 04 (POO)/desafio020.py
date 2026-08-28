"""
020 - Cria a classe Gamer, onde podemos cadastrar nome, nick e os jogos favoritos de uma pessoa.
Crie também um método que permita mostrar a ficha do gamer.

"""

from rich.panel import Panel

class Gamer:

    def __init__(self, nome = None, nick = None):
        self.nome = nome
        self.nick = nick

    def jogosFav(self, jogos = None):
        self.jogosFavoritos = jogos

    def __str__(self):
        return f'{self.jogosFavoritos}'


nome = input('Informe seu nome: ')
nick = input('Informe seu nick: ')

gamer1 = Gamer(nome, nick)

print('\n{:=^20} GAMES FAVORITOS {:=^20}'.format('', ''))

lista = []

while True: 


    jogos = input('Informe o nome do jogo: ')
    sair = int(input('Deseja informar outro jogo (1 - sim/ 0 - não): '))
    if sair == 1:
        continue

    if sair == 0:
        break

    listaJogos = {
        'Jogo': jogos
        }
    
    lista.append(listaJogos)


    for i in lista:
        print(i)

