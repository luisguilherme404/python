carros = []
materiaisRetirados = []

def cadastroDeEquipes():
    print('{:=^30}\n\tCADASTRO\n{:=^30}'.format('', ''))

    nome = input('\nInforme o nome do funcionário: ')
    turma = input('Infome o número da frota: ')
    matricula = input('Informe a matrícula do funcionário: ')

    funcionario = {
        'Nome': nome,
        'Turma': turma,
        'Matrícula': matricula
    }

    carros.append(funcionario)

def listaDeEquipes():

    print('{:=^40}\nLISTA DE EQUIPES\n{:=^40}'.format('',''))

    for i in carros:
        print(f'\nNome: {i['Nome']}')
        print(f'Turma: {i['Turma']}')
        print(f'Matrícula: {i['Matrícula']}\n')

def registroDeRetiradas():
    print('{:=^40}\n\tMATERIAIS RETIRADOS\n{:=^40}'.format('',''))

    nome = input('Informe o funcionário que retirou o material: ')
    data = input('Informe a data de retirada: ')  #preciso adicionar uma máscara de datas para esta função: dd/mm/aaaa
    while True:
        material = input('Informe o material retirado: ')
        qtd = int(input('Informe a quantidade do material: '))

        retirada =  {
            'Nome': nome,
            'Data': data,
            'Material': material,
            'Quantidade': qtd
        }
        
        materiaisRetirados.append(retirada)

        addOrNot = input('Deseja adicionar outro material (s/n): ')
        if addOrNot == 's' or addOrNot == 'S':
            continue
        elif addOrNot == 'n' or addOrNot =='N':
            break
        else:
            print('Informe uma opção válida!')
            continue

def listaDemateriaisRetirados():
    print('\n{:=^50}\n\tLISTA DE MATERIAIS RETIRADOS\n{:=^50}'.format('', ''))

    for i in materiaisRetirados:
        """print(f'\nNome: {carros['Nome']}')
        print(f'Turma: {carros['Turma']}')
        print(F'Matrícula: {carros['Matrícula']}')
        print(f'Material: {i['Material']}')
        print(f'Quantidade: {i['Quantidade']}\n')"""
        print(i)
