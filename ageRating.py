"""
Peça a age do usuário.

Mostre:

Menor de idade
Adulto
Idoso

Considere:

<18
18–59
60+

Depois diga se pode dirigir.
"""

age = int(input("\nInput your age, please: "))      #int no inicio para entender que é um número inteiro e não uma string

if age < 18:
    print("--> You can't drive. Minors can't get a driver's license.\n")

elif age >= 18 and age < 60:
    print("--> You need to get your driver's license to be able to drive anywhere in the country. Drive safely!\n")

else:
    print("--> Maybe you shouldn't drive. I'm so sorry!\n")