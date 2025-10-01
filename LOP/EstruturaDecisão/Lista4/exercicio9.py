TAXA_MG = 0.07
TAXA_SP = 0.12
TAXA_RJ = 0.15
TAXA_MS = 0.08

valor_produto = float(input("Digite o valor do produto sem taxa: "))
estado_destino = input("\nDigite qual é o estado destino do produto\n(MG - Minas Gerais, SP - São Paulo, RJ - Rio de Janeiro ou MS - Mato Grosso do Sul): ")

if valor_produto <= 0:
    print("Valor do produto inválido")

else:

    if estado_destino in ['MG', 'SP', 'RJ', 'MS']:

        if estado_destino == 'MG':
            valor_produto_com_taxa = (valor_produto + (valor_produto * TAXA_MG))
            print(f"O valor do produto em Minas Gerais é de: R${valor_produto_com_taxa}")


        elif estado_destino == 'SP':
            valor_produto_com_taxa = (valor_produto + (valor_produto * TAXA_SP))
            print(f"O valor do produto em São Paulo é de: R${valor_produto_com_taxa}")

        elif estado_destino == 'RJ':
            valor_produto_com_taxa = (valor_produto + (valor_produto * TAXA_RJ))
            print(f"O valor do produto no Rio de Janeiro é de: R${valor_produto_com_taxa}")

        else:
            valor_produto_com_taxa = (valor_produto + (valor_produto * TAXA_MS))
            print(f"O valor do produto no Mato Grosso do Sul é de: R${valor_produto_com_taxa}")

    else:
        print("Estado inválido")