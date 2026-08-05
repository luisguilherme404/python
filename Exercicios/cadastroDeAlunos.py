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

0 - Sair
1 - Adicionar
2 - Listar
3 - Média
4 - Melhor aluno

anotação: .items() é usado somente para DICIONÁRIOS

"""
import meuModulo
import time

alunos = []

def adicionar():
    try:
        nome = input('Informe seu nome: ')
        idade = int(input('Informe sua idade: '))
        nota = float(input('Informe sua nota: '))
        
        aluno = {
            'Nome': nome, 
            'Idade': idade, 
            'Notas': nota
            }

        alunos.append(aluno)    #adicionar mais alunos no final da lista
    except ValueError:
        print('Achou que ia quebrar o código né bacana?')
        time.sleep(2)


def lista():
    if len(alunos) == 0:    #se não houver alunos cadastrados mostrar a mensagem
        print('ATENÇÃO: nenhum aluno cadastrado.')

    else:
        print('========= ALUNOS CADASTRADOS =========\n')

        for percorrer in alunos: #percorrer acessa cada chave/valor do dicionário
            print(percorrer)

def media():

    if len(alunos) == 0:
        print('Não é possível dividir por ZERO.')

    soma = 0

    for percorrer in alunos:
        soma += percorrer['Notas']  #percorrer acessa somente os valores da chave 'Notas'
    media = soma / len(alunos)

    print(f'Média: {media:.2f}')
  

def melhorNota():
    melhorNota = 0
    estudante = ''

    if len(alunos) == 0:    #len lê a quantidade de elementos dentro da variável
        print('ATENÇÃO: nenhum aluno cadastrado.')   

    else:    
        for percorrer in alunos:
            if percorrer['Notas'] > melhorNota: #percorrer acessa somente os valores da chave 'Notas'
                melhorNota = percorrer['Notas'] #percorrer acessa somente os valores da chave 'Notas'
                estudante = percorrer['Nome']   #percorrer acessa somente os valores da chave 'Nome'

            print(f'Parabéns pelo esforço, {estudante}.\nSua nota é a maior alcançada: {melhorNota}.')

while True:

    #main.py:
    try:
        print('\n* Escolha uma opção:')
        print('0 - Sair')
        print('1 - Cadastro do aluno')
        print('2 - Lista de alunos cadastrados')
        print('3 - Média das notas dos alunos')
        print('4 - Aluno com a maior nota')
        escolha = int(input('\n-> Escolha uma opção: '))
        print('\n')

        if escolha == 0:
            print('Programa finalizado...')
            time.sleep(1)
            break

        elif escolha == 1:
            adicionar()
            
        elif escolha == 2:
            lista()

        elif escolha == 3:
            media()

        elif escolha == 4:
            melhorNota()

        else:
            
            for i in range(1, 11):
                print('Escolhe só o que tem no menu de opções. LERDÃO! `-´')
                time.sleep(1)

    except KeyboardInterrupt:
        meuModulo.msgExcecao(True)
        break    

    except ValueError:
        print('\nFecha o programa direito, meu camarada `-´\n')
        time.sleep(2)
        break