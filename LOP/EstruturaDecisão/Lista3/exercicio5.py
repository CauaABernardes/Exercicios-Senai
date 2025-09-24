PRECO_MACA = 1.80
PRECO_MACA_MAIS_QUE_5 = 1.50

PRECO_MORANGO = 2.50
PRECO_MORANGO_MAIS_QUE_5 = 2.20

DESCONTO = 0.10

PRECO_MINIMO_PARA_DESCONTO = 25
KG_MINIMO_PARA_DESCONTO = 8

print("+================================================+")
print("|           Frutas     do     Marquin            |")
print("|================================================|")
print("|..............| ...Até 5 KG... |  Acima de 5 kg |")
print("| 1 - Morango: | R$ 2,50 por kg | R$ 2,20 por kg |")
print("| 2 - Maçã:    | R$ 1,80 por kg | R$ 1,50 por kg |")
print("|              |                |                |")
print("| 3 - Morango e maçã...........................: |")
print("| 4 - Sair.....................................: |")
print("+================================================+\n")

opcao = int(input("Digite a sua opção desejada: "))

if opcao == 1:
    qtd_kg = float(input("Digite quantos kg de morango você quer comprar: "))

    if qtd_kg <= 0:
        print("Valores inválidos")
    else:
        if qtd_kg <= 5:
            valor_compra = qtd_kg * PRECO_MORANGO
        else:
            valor_compra = qtd_kg * PRECO_MORANGO_MAIS_QUE_5

        if valor_compra > PRECO_MINIMO_PARA_DESCONTO or qtd_kg > KG_MINIMO_PARA_DESCONTO:
            valor_compra -= (valor_compra * DESCONTO)

        print(f"O valor total de sua compra foi de: R${valor_compra:.2f}\nObrigado por comprar conosco")

elif opcao == 2:
    qtd_kg = float(input("Digite quantos kg de maçã você quer comprar: "))

    if qtd_kg <= 0:
        print("Valores inválidos")
    else:
        if qtd_kg <= 5:
            valor_compra = qtd_kg * PRECO_MACA
        else:
            valor_compra = qtd_kg * PRECO_MACA_MAIS_QUE_5

        if valor_compra > PRECO_MINIMO_PARA_DESCONTO or qtd_kg > KG_MINIMO_PARA_DESCONTO:
            valor_compra -= (valor_compra * DESCONTO)

        print(f"O valor total de sua compra foi de: R${valor_compra:.2f}\nObrigado por comprar conosco")

elif opcao == 3:
    qtd_kg_morango = float(input("Digite quantos kg de morango você quer comprar: "))
    qtd_kg_maca = float(input("Digite quantos kg de maçã você quer comprar: "))

    if qtd_kg_maca < 0 or qtd_kg_morango < 0:
        print("Valores inválidos")
    else:
        valor_compra = 0

        qtd_kg_total = qtd_kg_morango + qtd_kg_maca

        if qtd_kg_morango <= 5:
            valor_compra += qtd_kg_morango * PRECO_MORANGO
        else:
            valor_compra += qtd_kg_morango * PRECO_MORANGO_MAIS_QUE_5

        if qtd_kg_maca <= 5:
            valor_compra += qtd_kg_maca * PRECO_MACA
        else:
            valor_compra += qtd_kg_maca * PRECO_MACA_MAIS_QUE_5

        if valor_compra > PRECO_MINIMO_PARA_DESCONTO or qtd_kg_total > KG_MINIMO_PARA_DESCONTO:
            valor_compra -= (valor_compra * DESCONTO)

        print(f"O valor total de sua compra foi de: R${valor_compra:.2f}\nObrigado por comprar conosco")

elif opcao == 4:
    print("Te vejo na próxima :)")

else:
    print("Opção inválida")