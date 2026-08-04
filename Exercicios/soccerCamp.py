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
Nome do jogador com mais gols.          -> ok
Quantidade de gols desse jogador.       -> ok
Nome do jogador mais velho.             -> ok 
Nome do jogador mais novo.              -> ok 
Média de idade dos jogadores.           -> ok
Total de gols marcados pela equipe.     -> ok
"""
qtdJ = 0    #quantidade de jogadores
qtdGols = 0    #quantidade de gols
golsTotais = 0  #total de gols da equipe
somaIdade = 0
mediaIdade = 0

maisGols = 0
maisVelho = 0
maisNovo = 0

nomeMaisGols = "Sem info"
nomeVelho = "Sem info"
nomeNovo = "Sem info"

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

if qtdJ > 0   :
    mediaIdade = somaIdade / qtdJ

print("\n========= RESUMO =========\n")  
print("-> Nº cadastros:", qtdJ)
print("-> Total de gols:", golsTotais)
print("-> Soma das idades:", somaIdade)
print("-> Media das idades:", mediaIdade)
print(f"\n-> Jogador com mais gols: {nomeMaisGols} ({maisGols} gols)")
print(f"-> Jogador mais velho: {nomeVelho} ({maisVelho} anos)" )
print(f"-> Jogador mais novo: {nomeNovo} ({maisNovo} anos)\n" )