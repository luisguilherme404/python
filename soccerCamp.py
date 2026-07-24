"""
🏆 Exercício 7 — Campeonato de Futebol

O programa deve permitir informar infinitos jogadores.

Para cada jogador, informe:

Nome
Idade
Quantidade de gols marcados

Digite "fim" como nome para encerrar.

No final mostre:

Quantidade de jogadores cadastrados.    -> ok 
Nome do jogador com mais gols.
Quantidade de gols desse jogador.
Nome do jogador mais velho.             -> ok 
Nome do jogador mais novo.              -> ok 
Média de idade dos jogadores.           -> ok
Total de gols marcados pela equipe.     -> ok
"""
qtdJ = 0    #quantidade de jogadores
qtdGols = 0    #quantidade de jogadores
golsTotais = 0  #total de gols da equipe
somaIdade = 0
mediaIdade = 0

while True:
  
    nome = input("\nInforme um nome ('s/S' para finalizar): ")

    if nome == 's' or nome == 'S':
        break

    idade = int(input("Infome a idade: "))
    gols = int(input("Informe a quantidade de gols marcados: "))


    if qtdJ == 0:
        maisVelho = idade
        maisNovo = idade
        nomeVelho = nome
        nomeNovo = nome

    if qtdGols == 0:
        maisGols = gols
        nomeMaisGols = nome

    qtdJ += 1
    somaIdade += idade
    golsTotais += gols

    if gols > maisGols:
        maisGols = gols
        nomeMaisGols = nome


    if idade >= maisVelho:
        maisVelho = idade
        nomeVelho = nome

    if idade < maisNovo:
        maisNovo = idade     
        nomeNovo = nome

if mediaIdade > 0   :
    mediaIdade = somaIdade / qtdJ
    
print(f"Jogador com mais gols: {nomeMaisGols}. QTD = ({maisGols} gols)")
print(f"Jogador mais velho: {nomeVelho} ({maisVelho})" )
print(f"Jogador mais novo: {nomeNovo} ({maisNovo})" )
print("Qtd de jogadores cadastrados:", qtdJ)
print("Total de gols:", golsTotais)
print("Soma das idades:", somaIdade)
print("Media das idades:", mediaIdade)



