"""
Crie um programa que:

Peça dois números.
Peça uma operação:
+
-
*
/
%
**
Execute a operação utilizando if/elif.
Se o usuário escolher uma operação inválida, mostre uma mensagem de erro.

Exemplo:

Primeiro número: 8
Segundo número: 2
Operação: **

Resultado: 64

Treina

input
if
operadores
"""
operadores = {"+", "-", "*", "/", "**", "%"}

while True:
    print("\n-> Informe dois números para calcularmos\n")

    num1 = int(input("(1st number) Informe um número inteiro: "))
    num2 = int(input("(2nd number) Informe um número inteiro: "))

    print(f"-> Números informados: {num1}, {num2}")
    
    op = input("\nInforme qual operador deseja usar (+, -, *, /, **, %): ")

    if op not in operadores:
        print("Operador inválido. Selecione apenas os propostos. LERDÃO!")
        continue       #enquanto o operador estiver incorreto o código retorna para o inicio do while
    

    if op == '+':
        soma = num1 + num2
        print("\n========= OPERADOR 'SOMA' SELECIONADO =========")
        print(f"\nOperação: {num1} {op} {num2}")
        print(f"-> Resultado: {soma}")

    elif op == '-':
        sub = num1 - num2
        print("\n========= OPERADOR 'SUBTRAÇÃO' SELECIONADO =========")
        print(f"\nOperação: {num1} {op} {num2}")
        print(f"Resultado: {sub}")

    elif op == '*':
        times = num1 * num2
        print("\n=========  OPERADOR 'MULTIPLICAÇÃO' SELECIONADO =========")
        print(f"\nOperação: {num1} {op} {num2}")
        print(f"Resultado: {times}")

    elif op == '/':
        divisao = num1 / num2
        print("\n========= OPERADOR 'DIVISÃO' SELECIONADO =========")
        print(f"\nOperação: {num1} {op} {num2}")
        print(f"Resultado: {divisao}")

    elif op == '%':
        resto = num1 % num2
        print("\n========= OPERADOR 'MÓDULO (RESTO)' SELECIONADO =========")
        print(f"\nOperação: {num1} {op} {num2}")
        print(f"Resultado: {resto}")

    elif op == '**':
        exp = num1 ** num2      #expoente
        print("\n========= OPERADOR 'EXPONENCIAÇÃO' SELECIONADO =========")
        print(f"Operação: {num1} {op} {num2}")
        print(f"Resultado: {exp}")

    #else:
        #print("Operador inválido. Selecione apenas os propostos. LERDÃO!")
    
    while True:     #tudo que está abaixo é verdadeiro até eu definir um break para parar este laço
        stop = int(input("\nRealizar outro cálculo (0 - sair/ 1 - continuar): "))

        if stop == 0:
            print("Programa finalizado.")
            break   #só se usa break com while True

        elif stop == 1:
            break   #só se usa break com while True

        else:
            print("Escolha a opção 0 ou 1")
    
            