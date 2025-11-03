num1 = 0
num2 = 0

for i in range(1, 3):
    num_digitado = int(input("Digite um número: "))

    if i == 1:
        num1 = num_digitado

    elif i == 2 and num_digitado == 0:
        print("O segundo número não pode ser zero\nPois não existe divisão por 0")
        num_digitado = int(input("Digite um outro número: "))

        num2 = num_digitado

    else:
        num2 = num_digitado

print(f"Divisão: {num1/num2:.2f}")
