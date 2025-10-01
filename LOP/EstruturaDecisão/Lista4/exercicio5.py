VALOR_ALCOOL = 3.97
VALOR_GASOLINA = 5.89

VALOR_ALCOOL_DESCONTO_20L = 0.03
VALOR_ALCOOL_DESCONTO_MAIS_DE_20L = 0.05

VALOR_GASOLINA_DESCONTO_20L = 0.04
VALOR_GASOLINA_DESCONTO_MAIS_DE_20L = 0.06

print("+===========================================+")
print("|            Posto   do   Marquin Jr        |")
print("|===========================================|")
print("|Álcool: Até 20L, desconto de 3% por litro  |")
print("|    Acima de 20L, desconto de 5% por litro |")
print("|-------------------------------------------|")
print("|Gasolina: Até 20L, desconto de 4% por litro|")
print("|    Acima de 20L, desconto de 6% por litro |")
print("+===========================================+")

print("\nBem-vindo ao posto do Marqin Jr")

tipo_combustivel = input("Selecione o tipo de conbustível vendido\nDigite 'A' para Álcool ou digite 'G' para Gasolina: ")
litros_vendidos = float(input("\nDigite quantos litros foram comprados: "))

if tipo_combustivel in ['A', 'G']:

    if litros_vendidos < 0:
        print("Quantidade de litros de combustível vendidos inválida")

    else:
        if tipo_combustivel == 'A':

            valor_combustivel = litros_vendidos * VALOR_ALCOOL

            if litros_vendidos <= 20:
                valor_compra = (valor_combustivel - (valor_combustivel * VALOR_ALCOOL_DESCONTO_20L))

            else:
                valor_compra = (valor_combustivel - (valor_combustivel * VALOR_ALCOOL_DESCONTO_MAIS_DE_20L))

            print(f"O valor da sua compra de Álcool no Posto do Marquin Jr é de: R${valor_compra:.2f}")

        else:

            valor_combustivel = litros_vendidos * VALOR_GASOLINA

            if litros_vendidos <= 20:
                valor_compra = (valor_combustivel - (valor_combustivel * VALOR_GASOLINA_DESCONTO_20L))

            else:
                valor_compra = (valor_combustivel - (valor_combustivel * VALOR_GASOLINA_DESCONTO_MAIS_DE_20L))

            print(f"O valor da sua compra de Gasolina no Posto do Marquin Jr é de: R${valor_compra:.2f}")

        print("\nObrigado e volte sempre :)")

else:
    print("Opção de conbustível inválida")