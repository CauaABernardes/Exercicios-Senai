num = int(input("Digite um número: "))

if num % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")

if num % 3 == 0 and num % 5 == 0:
    print("O número é múltiplo de 3 e de 5")
elif num % 3 == 0:
    print("O número é múltiplo de 3")
elif num % 5 == 0:
    print("O número é múltiplo de 5")
else:
    print("O número não é múltiplo de 3 nem de 5")