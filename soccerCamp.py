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
Nome do jogador mais velho.
Nome do jogador mais novo.
Média de idade dos jogadores.           -> ok
Total de gols marcados pela equipe.     -> ok
"""
qtdJ = 0    #quantidade de jogadores
golsTotais = 0  #total de gols da equipe
golsInd = 0
somaIdade = 0
mediaIdade = 0

while True:
    fim = input("\nDigite s-sair ou c-continuar : ")

    if fim == "s" or fim == "S":
        break

    jogador = {"nome" : input("Informe um nome: "), 
               "idade": int(input("Infome a idade: ")), 
               "gols" : int(input("Informe a quantidade de gols marcados: ")) }


    if qtdJ == 0:
        maisVelho = jogador["idade"]
        maisNovo = jogador["idade"]

    qtdJ += 1
    somaIdade += jogador["idade"]
    golsTotais += jogador["gols"]


    if jogador["idade"] > maisVelho:
        maisVelho = jogador["nome"]

    if jogador["idade"] < maisNovo:
        maisNovo = jogador["nome"]     

if mediaIdade > 0   :
    mediaIdade = somaIdade / qtdJ
    

print("\nJogador mais velho:", maisVelho )
print("Jogador mais novo:", maisNovo )
print("Qtd de jogadores cadastrados:", qtdJ)
print("Total de gols:", golsTotais)
print("Soma das idades:", somaIdade)
print("Media das idades:", mediaIdade)



