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

print("-> Informe dois números para calcularmos\n")

num1 = int(input("(1st number) Informe um número inteiro: "))
num2 = int(input("(2nd number) Informe um número inteiro: "))

print(f"-> Números informados: {num1}, {num2}")

op = input("\nInforme qual operador deseja usar (+, -, *, /, **, %): ")

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
    print("\n========= OPERADOR 'MÓDULO (RESTO)' SELECIONADO =========")
    print(f"Operação: {num1} {op} {num2}")
    print(f"Resultado: {exp}")

else:
    print("Operador inválido. Selecione apenas os propostos. LERDÃO!")