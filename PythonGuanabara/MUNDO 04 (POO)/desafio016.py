from rich import print
from rich import inspect
#para exibir um atributo de classe use: {self.__class__.empresa} ou {Funcionario.empresa}

class Funcionario:

    #atributos de classe
    empresa = 'LUVICS'

    def __init__(self, nome, setor, cargo):

        #atributos de instância 
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentcao(self) -> str:
        return f'-> Empresa: [on white]{self.__class__.empresa}[/] \n-> Nome: [red]{self.nome}[/]\n-> Setor: {self.setor}\n-> Cargo: {self.cargo}'

Funcionario.empresa = 'Mabella' 

pessoa1 = Funcionario('Louis', 'Adm', 'Diretor')
print(pessoa1.apresentcao())
inspect(pessoa1, methods=True)  #inspect exibe os atributos

pessoa2 = Funcionario('May', 'Proprietária', 'Patroa')
print(pessoa2.apresentcao())
inspect(pessoa2)  #inspect exibe os atributos

inspect(Funcionario)
#inspect(Funcionario, all= True)