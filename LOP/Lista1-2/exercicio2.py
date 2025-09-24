num1 = float(input("Digite o 1º número: "))
num2 = float(input("Digite o 2º número: "))
num3 = float(input("Digite o 3º número: "))

if num1 > num2 and  num1 > num3:
    print(f"O maior número é o {num1:.2f}")
elif num2 > num3 and num2 > num1:
    print(f"O maior número é o {num2:.2f}")
else:
    print(f"O maior número é o {num3:.2f}")