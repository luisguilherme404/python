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

# =========ESTRUTURA DE DADOS (TUPLAS)=========

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

#========= CONJUNTOS (set) =========

"""
Um conjunto é uma estrutura de dados mutável e não ordenada que permite armazenar uma coleção de elementos únicos.
Os conjuntos são delimitados por chaves {} ou são criados utilizando a função set().
Os conjuntos suportam operações matemáticas de conjuntos, como a união (|), a interseção (&), a diferença (-) e a diferença simétrica (^).
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
As estruturas de dados em Python nos oferecem grande flexibilidade e potência para armazenar e manipular dados em nossos programas. 
As listas são úteis para coleções ordenadas e mutáveis, as tuplas para coleções ordenadas e imutáveis, os dicionários para armazenar 
pares de chave valor e os conjuntos para coleções não ordenadas de elementos únicos.

"""

