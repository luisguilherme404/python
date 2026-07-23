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

    jogador = {"nome" : input("Informe um nome: "), "idade": int(input("Infome a idade: ")), "gols" : int(input("Informe a quantidade de gols marcados: ")) }


    if jogador["nome"] == "fim":
        break

    if qtdJ == 0:
        maisVelho = jogador["idade"]
        maisNovo = jogador["idade"]

    else:

        if jogador["idade"] > maisVelho:
            maisVelho = jogador["idade"]

        if jogador["idade"] < maisNovo:
            maisNovo = jogador["idade"]     


        qtdJ += 1
        golsTotais += jogador["gols"]
        somaIdade += jogador["idade"]

mediaIdade = somaIdade / qtdJ


    

     





print("\nQtd de jogadores cadastrados:", qtdJ)
print("Total de gols:", golsTotais)
print("Soma das idades:", somaIdade)
print("Media das idades:", mediaIdade)



