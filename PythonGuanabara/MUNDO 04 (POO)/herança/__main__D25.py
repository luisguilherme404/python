from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distance):
        self.distancia = distance
        #self.frete = shipment

    @abstractmethod
    def calcularFrete(self):
        pass

class Moto(Transporte):
    fator = 0.5

    def calcularFrete(self):
        if self.distancia > 0:
            valor = self.distancia * Moto.fator
            print(f'Frete aceito.\nValor: R$ {valor:.2f}\n')
        else:
            print('Informe uma quilometragem válida.\n')

class Caminhao(Transporte):
    fator = 1.20
    distMin = 50

    def calcularFrete(self):

        if self.distancia < Caminhao.distMin:
            print(f'Frete para {self.distancia} km indisponível. Distância mínima: {Caminhao.distMin} km.\n')
        
        else:
            calculo = Caminhao.fator * self.distancia
            print(f'Frete aceito. Valor: R$ {calculo:.2f}.\n')

class Drone(Transporte):
    fator = 9.5
    distMax = 10

    def calcularFrete(self):

        if self.distancia <= 0:
            print('Informe uma quilometragem maior que zero.\n')

        elif self.distancia > Drone.distMax:
            print(f'Frete para {self.distancia} km indisponível. Distância máxima: {Drone.distMax} km\n')

        else:
            calculo = Drone.fator * self.distancia
            print(f'Frete aceito.\nValor: R$ {calculo:.2f}\n')
        
veiculo0 = Moto(10)
veiculo1 = Caminhao(50)
veiculo2 = Drone(1001)

print(f'Moto:')
veiculo0.calcularFrete()

print(f'Caminhão:')
veiculo1.calcularFrete()

print(f'Drone:')
veiculo2.calcularFrete()
