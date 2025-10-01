AUMENTO_ATE_50 = 0.05
AUMENTO_ATE_100 = 0.10
AUMENTO_ACIMA_100 = 0.15

print("+================================================+")
print("|         Reajuste         de         Preço      |")
print("+================================================+")
print("|      PREÇO ANTIGO      | PERCENTUAL DE AUMENTO |")
print("|------------------------------------------------|")
print("| Até R$50              |            5%          |")
print("|------------------------------------------------|")
print("| Entre R$50 e R$100    |            10%         |")
print("|------------------------------------------------|")
print("| Acima de R$100        |            15%         |")
print("+================================================+\n")

preco_produto = float(input("Digite aqui o preço antigo do seu produto: "))

if preco_produto <= 0:
    print("Preço inválido")

else:
    preco_produto_ajustado = 0

    if preco_produto <= 50:
        preco_produto_ajustado = (preco_produto + (preco_produto * AUMENTO_ATE_50))

    elif preco_produto <=100:
        preco_produto_ajustado = (preco_produto + (preco_produto * AUMENTO_ATE_100))
    else:
        preco_produto_ajustado = (preco_produto + (preco_produto * AUMENTO_ACIMA_100))

    print(f"O preço do produto após o reajuste é de: R${preco_produto_ajustado:.2f}")

    if preco_produto_ajustado <= 80:
        print("Barato")

    elif preco_produto_ajustado <= 120:
        print("Normal")

    elif preco_produto_ajustado <= 200:
        print("Caro")

    else:
        print("Muito caro")