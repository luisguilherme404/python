#DECLARAÇÃO DE CLASSE
class Gafanhoto:

    """
    Classe Gafanhoto
    Definição do aluno do Gustavao Guanabara, vulgo Gafanhoto.

    variavel = Gafanhoto()
    """

    def __init__(self, n = 'Nulo', i = 0): #método construtor
        #atributos de instancia
        self.nome = n
        self.idade = i

    #métodos de instancia
    def aniversario(self):
        self.idade += 1

    def __str__(self): #dunder(__) method
        return f'\n{self.nome} é Gafanhoto e fez {self.idade} anos de idade.\n'

    def __getstate__(self):
        return f'Estado -> Nome: {self.nome} | Idade: {self.idade}'
        
#declaração de objeto


g1 = Gafanhoto(n = 'LOUiS', i = 19)
#print(g1.nome)
#print(g1.idade)
g1.aniversario()
print('Mensagem:', g1)   #só funciona devido a função __str__
print('Estado em dicionário (atributo):', g1.__dict__)  #exibição em dicionário -> atributo
print('Estado personalizado (método):', g1.__getstate__())  #exibição do estado de maneira personalizada por ser método -> método
print('Classe:', g1.__doc__)   #docstring da classe
print(g1.__class__)

g2 = Gafanhoto(n = 'maYra', i = 20)
g2.aniversario()
print(g2)
print(g2.__dict__)
print(g2.__getstate__())
print(g2.__doc__)
