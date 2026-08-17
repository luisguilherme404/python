import shelve
carros = []
materiaisRetirados = []

def cadastroDeEquipes():
    print('{:=^30}\n\tCADASTRO\n{:=^30}'.format('', ''))

    nome = input('\nInforme o nome do funcionário: ')
    turma = input('Infome o número da frota: ')
    matricula = input('Informe a matrícula do funcionário: ')

    with shelve.open('dados/dadosEletricistas') as dadosEletricistas:

        funcionario = {
            'Nome': nome,
            'Turma': turma,
            'Matrícula': matricula
        }

        if 'usuarios' not in dadosEletricistas:
            dadosEletricistas['usuarios'] = []

        carros = dadosEletricistas['usuarios']
        carros.append(funcionario)
        dadosEletricistas['usuarios'] = carros

def listaDeEquipes():

    with shelve.open('dados/dadosEletricistas') as dadosEletricistas:
        lista = dadosEletricistas['usuarios']

        print('{:=^40}\n\tLISTA DE EQUIPES\n{:=^40}'.format('',''))

        for i in lista:
            print(f'\nNome: {i['Nome']}')
            print(f'Turma: {i['Turma']}')
            print(f'Matrícula: {i['Matrícula']}\n')

def registroDeRetiradas():
    print('{:=^40}\n\tMATERIAIS RETIRADOS\n{:=^40}'.format('',''))

    #nome = input('Informe o funcionário que retirou o material: ')
    matricula = input('Informe a matrícula de quem retirou o material: ')
    data = input('Informe a data de retirada: ')  #preciso adicionar uma máscara de datas para esta função: dd/mm/aaaa
    with shelve.open('dados/materiaisRetirados') as lista:
        if 'retiradas' not in lista:
            lista['retiradas'] = []

        materiaisRetirados = lista['retiradas']
        while True:
            material = input('Informe o material retirado: ')
            qtd = int(input('Informe a quantidade do material: '))


            retirada =  {
                'Matrícula': matricula,
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

        lista['retiradas'] = materiaisRetirados

def listaDemateriaisRetirados():

    with shelve.open('dados/materiaisRetirados') as lista:
        lista = lista['retiradas']

    print('\n{:=^50}\n\tLISTA DE MATERIAIS RETIRADOS\n{:=^50}'.format('', ''))

    for i in lista:
        print(f'Matrícula: {i['Matrícula']}')
        print(f'Data: {i['Data']}')
        print(f'Material: {i['Material']}')
        print(f'Quantidade: {i['Quantidade']}\n')
