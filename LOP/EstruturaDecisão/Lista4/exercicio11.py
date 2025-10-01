print("+=============================================+")
print("|           Banco    do    Marquin            |")
print("|=============================================|")
print("|Saques a partir de R$5 até R$9.998           |")
print("|                                             |")
print("|Cédulas disponíveis:                         |")
print("|R$2, R$5, R$10, R$20, R$50, R$100 e R$200    |")
print("|                                             |")
print("+=============================================+")

saque = int(input("\nDigite o quanto você quer sacar: "))

if saque < 5 or saque > 9998:
    print("Valor de saque inválido")

else:

    qtd_notas_200 = (saque // 200)
    sobra = (saque % 200)

    qtd_notas_100 = (sobra // 100)
    sobra = (sobra % 100)

    qtd_notas_50 = (sobra // 50)
    sobra = (sobra % 50)

    qtd_notas_20 = (sobra // 20)
    sobra = (sobra % 20)

    qtd_notas_10 = (sobra // 10)
    sobra = (sobra % 10)

    qtd_notas_5 = (sobra // 5)
    sobra = (sobra % 5)

    qtd_notas_2 = (sobra // 2)
    sobra = (sobra % 2)

    print(f"Foram retiradas:\n{qtd_notas_200} notas de R$200\n{qtd_notas_100} notas de R$100\n{qtd_notas_50} notas de R$50\n{qtd_notas_20} notas de R$20\n{qtd_notas_10} notas de R$10\n{qtd_notas_5} notas de R$5\n{qtd_notas_2} notas de R$2")