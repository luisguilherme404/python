class ContaBancaria:

    """
    Crie uma conta bancária que permita fazer saques e depósitos.    
    """

    def __init__(self, id, nome, saldo = 0):
        self.id = id 
        self.titular = nome
        self.saldo = saldo
        print(f'\nConta {self.id} criada com sucesso.')

    def __str__(self):
        return f'Id: {self.id} | Titular: {self.titular} | Saldo: R$ {self.saldo:,.2f}\n'

    def deposito(self, valor):
        self.saldo += valor
        print(f'Depósito de R$ {valor:,.2f} na conta {self.id} autorizado.')
        #pass    #não fazer nada

    def saque (self, valor):

        if valor > self.saldo:
            print(f'Saque de R$ {valor:,.2f} NEGADO. Saldo INSUFICIENTE.')

        else:
            self.saldo -= valor
            print(f'Saque de R$ {valor:,.2f} da conta {self.id} autorizado.')
        #pass    #não fazer nada

conta1 = ContaBancaria(id = 10, nome = 'Luís G.', saldo = 1947.15 )
print(conta1)
conta1.deposito(valor = 100)
print(conta1)
conta1.saque(valor = 500)
print(conta1)
conta1.saque(valor = 300_000) # 300 mil, a linguagem permite o underline para organização neste caso
print(conta1)
#print(conta1.__doc__)
