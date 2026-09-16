class Pessoa:   #classe generalizada   
    def __init__(self, name = '', age = 0):
        self.nome = name
        self.idade = age

        def fazerAniversario(self):
            self.idade += 1

class Aluno(Pessoa):
    def __init__(self, name, age, curso, turma):
        super().__init__(name, age)

        self.curso = curso
        self.turma = turma

    def fazerMatricula(self):
        pass

class Professor(Pessoa):
    def __init__(self, name, age, especialidade, nivel):
        super().__init__(name, age, especialidade, nivel)

        self.especialidade = especialidade
        self.nivel = nivel

    def darAula(self):
        pass   

class Funcionario(Pessoa):
    def __init__(self, name, age, cargo, setor):
        super().__init__(name, age, cargo, setor)

        self.cargo = cargo
        self.setor = setor

    def baterPonto(self):
        pass