# =========VARIÁVEIS=========
"""
nome = "louis"
idade = 11
altura: 1.80
é_estudante = True
notas_mat = 98
notas_pt = notas_ing = 120
media = (98+120)/3  #218

print("A nota de inglês dele é:", notas_ing)
print("A nota de português dele é:", notas_pt)
print("A nota de matemática dele é:", notas_mat)
# =========VARIÁVEIS=========
"""

# =========OPERADORES=========

a = 10
b = 3

soma = a + b   # 13
subtracao = a - b    # 7
multiplicacao = a * b    # 30
divisao = a / b   # 3.333333333
divisao_inteira = a // b   # 3
modulo = a % b   # 1 (resto da divisão inteira)
exponenciacao = a ** b   # 1000

# =========COMPARAÇÃO=========

a = 10
b = 3


igual = a == b   # False
diferente = a != b   # True
maior_que = a > b   # True
menor_que = a < b   # False
maior_ou_igual = a >= b   # True
menor_ou_igual = a <= b   # False

# =========OPERADORES LÓGICOS=========

a = 10
b = 3


resultado_and = (a > 5) and (b < 5)   # True
resultado_or = (a > 15) or (b < 5)   # True
resultado_not = not (a > 5)   # False

# =========ESTRUTURAS CONDICIONAIS (IF, ELSE, ELIF = ELSE IF)=========

"""
if idade >= 18:
    print('\nVocê é maior de idade, pode prosseguir.')
else: 
    print("\nAguarde a maioridade para tirar sua habilitação.")

if media >= 90 and media >= 100:
        print("Very so good!!!")
elif media >= 70:
     print("Muito bem.")
else: 
     print("Aí não dá jogador")

"""
"""

cont = 0;
qtdTermos = 0

# =========LAÇOS (FOR E WHILE)=========
    
#print(frutas);
print('\nSequência de 20 termos a partir do 2. Razão = 2: ')
for variávelQueEuQuiser in range (1, 21):
    print(variávelQueEuQuiser * 2)

print('Valores inteiros até 8, a partir do valor da variável -> cont <-')
cont = -100;
qtdTermos = 0

while cont <= 8:
    print(cont * 1)
    qtdTermos +=1
    cont += 1

"""



# =========CONTROLE DOS LAÇOS (BREAK, CONTINUE E PASS)=========
"""
cont = 0;
qtdTermos = 0

while True:

    print(cont)
    cont += 1;
    qtdTermos += 1;

    if cont == 350:
        break

print("Qtd de termos:", qtdTermos)
print("\n")

for i in range(10):     
    if i % 2 == 0:      #se o termo for par o continue é executado e volta para o for
                        #se o termo for impar o print é executado e imprime o número impar
        continue
    print(i)
"""
    
# =========ESTRUTURA DE DADOS (LISTAS)=========

frutas = ["maçã", "uva", "melancia", "morango", "manga"]

"""
print(frutas[4])    #variável[~posição~] acessa o termo selecionado de acordo com a posição
print(frutas[2])    #variável[~posição~] acessa o termo selecionado de acordo com a posição
print(frutas[0])    #variável[~posição~] acessa o termo selecionado de acordo com a posição
print("\n")    
print(frutas[-1])    #variável[~-posição~] acessa o termo selecionado de acordo com a posição de trás p/ frente
print(frutas[-3])    #variável[~-posição~] acessa o termo selecionado de acordo com a posição de trás p/ frente
print(frutas[-5])    #variável[~-posição~] acessa o termo selecionado de acordo com a posição de trás p/ frente

frutas.append("carambola")  #adiciona no final da lista
print('Append:', frutas)

frutas.insert(0, "melão")
print('Insert:', frutas)    #adiciona um elemento numa posição específica

frutas.remove("melancia")   #remove um elemento da lista
print('Remove:', frutas)

frutaRemovida = frutas.pop(-2)  #remove e retorna um elemento numa posição específica da lista
print('Pop:   ', frutas)
print('Pop -> Fruta removida:',frutaRemovida)

frutas.reverse()
print('Reverse:', frutas)

frutas.sort()
print('Sort:', frutas)

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
print('Numeros originais:', numeros)

quadrados = [x ** 2 for x in numeros if x % 2==0]   # 'x' recebe os numeros PARES ao QUADRADO
print('Números pares ao quadrado:', quadrados)
"""

# =========ESTRUTURA DE DADOS (TUPLAS)=========

"""
print("\n========= TUPLA =========")

ponto = (3, 4)
print("Sequência:", ponto)
print('\nFirst position:', ponto[0])
print('Second position:', ponto[1])

print("\n")

minhaTupla = (1, 2, 3, 2, 4, 2)
print("Sequência:", minhaTupla)
print(f"Quantas vezes o '{minhaTupla[1]}' aparece:", minhaTupla.count(2))                       #devolve o número de vezes que o elemento (2) aparece na tupla
print(f"Posição em que o primeiro '{minhaTupla[1]}' aparece:", minhaTupla.index(2))             #devolve a posição em que aparece o primeiro elemento (2)
print(f"Posição do '{minhaTupla[1]}' (a partir da posição 2):", minhaTupla.index(2, 2))         #devolve a posição em que aparece o primeiro elemento (2) a partir da posição 2
print(f"Posição do '{minhaTupla[1]}' (início: pos 3; fim: pos 5):", minhaTupla.index(2, 4, 6))  #devolve a posição em que aparece o primeiro elemento (2) a partir da posição 2 e terminando na posição 6 (sim, passando a pos 5)  
print(f"Qtd de elementos na sequência:", len(minhaTupla))   #devolve a qtd de elementos da Tupla

# ========= DICIONÁRIOS =========

pessoa = {"nome": "Louis", "idade": 20, "altura": 1.80} #chave = "nome" | valor = "Louis"

print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Altura (metros):", pessoa["altura"])

print("Todas as chaves:", pessoa.keys())            #imprime todas as chaves do dicionário
print("Todos os valores:", pessoa.values())         #imprime todas os valores do dicionário
print("Todos os itens:", pessoa.items())            #imprime todos os pares de chaves-valores do dicionário

pessoa.update({"profissão": "Almoxarife"})          #atualiza o dicionário adicionando outro par de chaves-valores
print("Dicionário atualizado:", pessoa.items())
"""

#========= CONJUNTOS (set) =========

"""
Um conjunto é uma estrutura de dados mutável e não ordenada que permite armazenar uma coleção de elementos únicos.
Os conjuntos são delimitados por chaves {} ou são criados utilizando a função set().
Os conjuntos suportam operações matemáticas de conjuntos, como a união (|), a interseção (&), a diferença (-) e a diferença simétrica (^).
"""
"""
frutas = {"cupuaçu", "jaca", "ameixa", "amora"}
numeros = set([1, 2, 3, 2, 3, 4, 2])

conj1 = {1, 2, 5, 7, 9}
conj2 = {3, 4, 7, 9}

uniao = conj1 | conj2
print("-> União dos conjuntos:", uniao)                #exibe os valores dos dois conjuntos unidos

intersecao = conj1 & conj2
print("-> Interseção dos conjuntos:", intersecao)      #exibe os valores que pertencem aos dois conjuntos

diferenca = conj1 - conj2
print("-> Diferença dos conjuntos:", diferenca)        #remove tudo que se repete do conj1 em conj2 (removeu 7 e 9, restou: 1, 2, 5)

diferenca = conj2 - conj1
print("-> Diferença dos conjuntos pt2:", diferenca)    #remove tudo que se repete do conj2 em conj1 (removeu 7 e 9, restou: 3, 4)

diferencaSimetrica = conj1 ^ conj2
print("-> Diferença simétrica:", diferencaSimetrica)   #remove os elementos semelhantes dos dois conjuntos

#========= MÉTODOS E CONJUNTOS =========

frutas = {"cupuacu", "jaca", "ameixa", "amora"}

frutas.add("tomate")        #adiciona um elemento ao conjunto
print("Add:", frutas)

frutas.remove("cupuacu")    #remove um elemento existente no conjunto
print("Remove:", frutas)

frutas.discard("amora")     #remove um elemento CASO ele já exista no conjunto
print("Discard:", frutas)

frutas.clear()
print("Limpeza:", frutas)   #limpa o conjunto e exibe set()

"""
"""
As estruturas de dados em Python nos oferecem grande flexibilidade e potência para armazenar e manipular dados em nossos programas. 
As listas são úteis para coleções ordenadas e mutáveis, as tuplas para coleções ordenadas e imutáveis, os dicionários para armazenar 
pares de chave valor e os conjuntos para coleções não ordenadas de elementos únicos.

"""
"""

#========= FUNÇÕES =========

def saudacoes():
    print("Hello World.")
    
saudacoes() #imprime "Hello World."

#========= PARÂMETROS E ARGUMENTOS =========
nome = "LOUiS"

def saudacoes(estudante):
    print(f"Olá {estudante}!")

saudacoes(nome)    

#========= VALORES DE RETORNO =========
def soma(a, b):
    return a + b

resultado = soma(3, 4)
print("Resultado:", resultado)

#========= FUNÇÕES ANÔNIMAS (lambda) =========
#função comum
def quadrado(x):
    return x ** 2

print("Quadrado:", quadrado(4))

#função anônima
quadrado = lambda x: x ** 2
print("Quadrado (ANÔNIMA):", quadrado(4))

num = quadrado(10)
print("Quadrado:", num)

#========= ESCOPO DAS VARIÁVEIS (LOCAL VS GLOBAL)  =========

def funcao():
    variavel_local = 10
    print("Váriável local:", variavel_local)   #acessível SOMENTE dentro da função

variavel_global = 20

def funcao2():
    print("Váriável global:", variavel_global)

funcao()
funcao2()
print("Váriável global:", variavel_global)
#print(variavel_local)

#========= FUNÇÕES DEFINIDAS PELO USUÁRIO  =========

def calcularMedia(*numeros):    #utiliza-se o '*' antes do argumento quando se tem vários elementos como uma sequência        
    soma = sum(numeros) #soma dos elementos
    qtd = len(numeros)  #quantidade de elementos
    media = soma / qtd
    print("Soma:", soma)
    print("Qtd:", qtd)
    return media

print("Media:", calcularMedia(10, 15, 20, 25, 30))  #atribuição dos valores para *numeros

def somar3(x):
    return x + 3

print(f"Soma:", somar3(5))

somar = lambda x: x + 7
print(f"Soma (ANÔNIMA):", somar(5))

#========= DOCUMENTAÇÃO DE FUNÇÕES (DOCSTRINGS)  =========
#para a boa prática é bom documentar o propósito da função

def area_retangulo(base, altura):
    """
"""
    Calcula a área de um retângulo.


    Args:
        base (float): A base do retângulo.
        altura (float): A altura do retângulo.


    Returns:
        float: A área do retângulo.
    """
"""
    return base * altura

print("Área do retangulo:", area_retangulo(23.4, 9.88))

#========= FUNÇÕES COM NÚMERO VARIÁVEL DE ARGUMENTOS  =========

def somaVariavel(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    
    return total

print("Primeira soma:", somaVariavel(2, 4, 6))
print("Segunda soma:", somaVariavel(3, 5, 7))
    """

#========= MANEJO E EXCEÇÕES (TRY, EXCEPT e FINALLY) =========
#Em Python, tratamento (manejo) de exceções é um mecanismo que permite que seu programa 
#continue funcionando ou trate um erro de forma controlada, em vez de simplesmente encerrar com uma mensagem de erro.

"""
num = 0   #sem int para testar o except TypeError
qtd = 5

#TRY:o bloco try contém um código que pode gerar uma exceção (divisão é por zero), quando isso acontece a execução pula para o bloco 
# except. Sáida = Erro: divisão por zero 
try:
    media = qtd / num
    print(f'(Deu certo) Média: {media}')

#EXCEPT: aqui é especificado qual tipo de exceção se deseja lidar, pode haver inúmeros blocos EXCEPT
except ZeroDivisionError:
    print('Erro: divisão por zero!')
except TypeError:
    print("Atenção: você está tenatando calcular int com str, confira o input e corrija")
except FileNotFoundError:
    print('Atenção: arquivo não encontrado')

#FINALLY: usado para tarefas de limpeza ou liberação de recursos finalização de arquivos possuindo exceções ou não
#finally:
    #arquivo.close


def funcao(idade):
    if idade < 18:
        raise Exception("Entrada proibida para menores de idade") #raise lança uma exceção, exception cria uma msg personalizada

    print('Bem vindo à festa!')

try:    #tenta executar
    funcao(18)

except Exception as var: #caso tenha a exceção, a mensagem de Exception é armazenada em "var" 
    print(str(var))  #exibe a msg armazenada em "var"

"""

#========= ENTRADA/SAÍDA DE DADOS =========
"""
try:
    nome = input('Informe seu nome: ')
    idade = input('Informe sua idade: ')
    print('Eai, ' + nome + '!')
    print(f'Você tem {idade} anos.')
    
except KeyboardInterrupt:
    print("Programa finalizado com shortcut do teclado")
"""

#========= LEITURA E ESCRITA DE ARQUIVOS =========

#LEITURA:
"""
arquivo = open("dados.txt", 'r')    #"r"/'r' -> modo leitura
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

#ESCRITA:
arquivo = open('dados.txt', 'w')
arquivo.write('Hello World!')
arquivo.close()

#--------- SEMPRE FECHAR OS ARQUIVOS ( arquivo.close() ) PARA LIBERAR RECURSOS DO SISTEMA ---------

#WITH: encerra o programa automaticamente após sair do bloco
with open("dados.txt", 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
"""

#========= MÓDULOS =========

#Módulo é um arquivo que contém definições de funções, classes e variáveis que podem ser utilizadas em outros programas

import math     #funções matemáticas
resultado = math.sqrt(144)
print('Sem import sqrt', resultado)

from math import sqrt #funções específicas do módulo math
resultado = sqrt(49)
print('Com import sqrt:', resultado)

import random
import datetime

num = random.randint(0, 1)
print('Nº aleatório entre 1 e 20: ', num)

dataAtual = datetime.datetime.now()
print('Data atual:', dataAtual)

import meuModulo

meuModulo.saudar("LOUiS")
resultado = meuModulo.calcular(15, 17)
print("Soma = ", resultado)

print('{}'.format(resultado))
print(type(resultado))