#========= ORIENTAÇÃO =========

while True:
    nome = input('\nSeu nome: ')
    if nome == '0':
        break

    print('Eai, {:+<50} (À ESQUERDA)'.format(nome))
    print('Eai, {:=^50} (CENTRALIZADO)'.format(nome))
    print('Eai, {:*>50} (À DIREITA)'.format(nome))