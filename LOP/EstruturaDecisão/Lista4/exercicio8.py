print("+=============================================+")
print("|       Calculadora   do   Marquin            |")
print("|=============================================|")
print("|Escolha a opção:                             |")
print("|1- Soma entre 2 números....................: |")
print("|                                             |")
print("|2- Diferença entre 2 números (maior pelo me- |")
print("|nor).......................................: |")
print("|                                             |")
print("|3- Produto entre 2 números.................: |")
print("|                                             |")
print("|4- Divisão entre 2 números (O denominador não|")
print("|pode ser 0)................................: |")
print("|                                             |")
print("+=============================================+")

opcao = int(input("Digite a sua opção desejada: "))

if opcao not in [1, 2, 3, 4]:
    print("Opção inválida")

else:

    num1 = float(input("Digite o 1º número: "))
    num2 = float(input("Digite o 2º número: "))

    if opcao == 1:
        soma = (num1 + num2)
        print(f"O resultado da soma entre {num1} e {num2} é de: {soma:.2f}")

    elif opcao == 2:
        if num1 > num2:
            diferenca = (num1 - num2)

        else:
            diferenca = (num2 - num1)


        print(f"O resultado da diferença entre {num1} e {num2} é de: {diferenca:.2f}")

    elif opcao == 3:
        produto = (num1 + num2)
        print(f"O resultado do produto entre {num1} e {num2} é de: {produto:.2f}")

    else:
        if num2 == 0:
            print("Divisão por zero")

        else:
            divisao = (num1 / num2)

        print(f"O resultado da divisão entre {num1} e {num2} é de: {divisao:.2f}")
