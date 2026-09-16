from abc import ABC, abstractmethod


class BebidaQuente(ABC):

    def preparar(self):
        print('\n{:=^9} PREPARO DA BEBIDA {:=^9}'.format('', ''))
        self.ferverAgua()
        self.misturar()
        self.servir()
        

    def ferverAgua(self):
        print(f'1 - Fervendo à 100° Celsius')

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

class Cafe(BebidaQuente):

    def misturar(self):
        print(f'2 - Misturando o café.')    

    def servir(self):
        print('3 - Servindo o café, aproveite.\n')


class Cha(BebidaQuente):

    def misturar(self):
        print(f'2 - Misturando as ervas com a água fervida.')

    def servir(self):
        print(f'3 - Servindo o chá para os convidados.\n')

class Leite(BebidaQuente):

    def misturar(self):

        print(f'2 - Misturando o leite com achocolatado em pó.')
    
    def servir(self):
        print(f'3 - Servindo o leite com achocolatado para a criança.\n')

