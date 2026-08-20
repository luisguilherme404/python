"""
    ===== DEV = Luís Guilherme Campista da Silva =====

2 - Crie uma classe 'Retangulo' que:
* Se iniciada com um valor, crie um quadrado (largura = altura)
* Se instanciada com dois valores, crie um retângulo normal 

"""

from rich import print
from rich.traceback import install
install()

class Retangulo:
    def __init__(self, a = 0, l = 0):
        self.altura = a
        self.largura = l

    def __str__(self):
        if self.altura <= 0:
            return 'Erro, um dos dados é menor ou igual a 0.'
        elif self.altura == self.largura:
            return f'-> QUADRADO: Altura = {self.altura} | Largura = {self.largura}'
        else:
            return f'-> RETÂNGULO: Altura = {self.altura} | Largura = {self.largura}'

objeto1 = Retangulo()
print(objeto1.__str__())

objeto2 = Retangulo(3, 3)
print(objeto2.__str__())

objeto3 = Retangulo(3, 6)
print(objeto3.__str__())
