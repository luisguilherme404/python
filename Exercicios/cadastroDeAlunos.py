"""
Exercício 2 – Cadastro de alunos

Crie um programa que permita cadastrar alunos usando funções.

Cada aluno deve ter:

Nome
Idade
Nota

Crie funções para:

Adicionar aluno
Listar alunos
Mostrar a média das notas
Mostrar o aluno com a maior nota

Use uma lista de dicionários para armazenar os dados.

Exemplo:

1 - Adicionar
2 - Listar
3 - Média
4 - Melhor aluno
5 - Sair
"""

alunos = []

while True:

    def adicionar():

        nome = input('Informe seu nome: ')
        idade = int(input('Informe sua idade: '))
        nota = float(input('Informe sua nota: '))
        
        aluno = {
            'Nome': nome, 
            'Idade': idade, 
            'Notas': nota
            }

        alunos.append(aluno)


    def lista():
        for percorrer in alunos: #.items() é usado somente para DICIONÁRIOS
            print(percorrer)

    def media():
        soma = 0

        for percorrer in alunos:
            soma += percorrer['Notas']

        media = soma / len(alunos)

        print(f'Média: {media:.2f}')

    def melhorNota():
        for percorrer in alunos:
            melhorNota = 0

            if percorrer['Notas'] > melhorNota:
                melhorNota = percorrer['Notas']

        print(melhorNota)

    print('\nEscolha uma opção:')
    print('0 - Sair')
    print('1 - Adicionar aluno')
    print('2 - Listar alunos')
    print('3 - Média das notas dos alunos')
    print('4 - Aluno com a melhor nota')
    escolha = int(input('-> Escolha uma opção: '))
    print('\n')

    if escolha == 0:
        break

    elif escolha == 1:
        adicionar()
        
    elif escolha == 2:
        lista()

    elif escolha == 3:
        media()
    elif escolha == 4:
        melhorNota()