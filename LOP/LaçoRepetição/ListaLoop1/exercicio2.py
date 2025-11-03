num1 = 0
num2 = 0
nums_digitados = 0

while nums_digitados < 2:
    num_digitado = int(input("Digite um número: "))

    if nums_digitados == 0:
        num1 = num_digitado

    elif nums_digitados == 1 and num_digitado == 0:
        print("O segundo número não pode ser zero\nPois não existe divisão por 0")
        num_digitado = int(input("Digite um outro número: "))

        num2 = num_digitado

    else:
        num2 = num_digitado

    nums_digitados += 1

print(f"Divisão: {num1/num2:.2f}")
