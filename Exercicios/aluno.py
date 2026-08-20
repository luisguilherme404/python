"""
1 - Crie uma classe 'Aluno' que permita ser instanciada de 3 formas:
* Sem parâmetros
* Passando apenas o nome
* Passando o nome e a matrícula

"""
from rich import print
from rich.traceback import install 
install()

class Aluno:
    def __init__(self, n = 'None', m = 'None'):
        self.nome = n
        self.matricula = m

    def __str__(self):
        return f'\n-> [green]Estudante[/]: [bold]{self.nome}[/] | [blue bold]Matrícula[/]: [bold]{self.matricula}[/] :+1:'

estudante1 = Aluno()
estudante2 = Aluno(n = 'LOUIS')
estudante3 = Aluno(n = 'Joaõzinho', m = 'E202020')

print(estudante1.__str__())
print(estudante2.__str__())
print(estudante3.__str__())
