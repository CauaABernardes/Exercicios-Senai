qtd_estoque_atual = int(input("Digite a quantidade atual do produto em estoque: "))
qtd_estoque_max = int(input("Digite a quantidade máxima do produto em estoque: "))
qtd_estoque_min = int(input("Digite a quantidade mínima do produto em estoque: "))

qtd_estoque_media = ((qtd_estoque_max + qtd_estoque_min)/2)

if qtd_estoque_atual < 0 or qtd_estoque_min < 0 or qtd_estoque_max < 0:
    print("Valor inválido para quantidade para estoque atual, máximo ou mínimo")

elif qtd_estoque_min > qtd_estoque_max:
    print("Valor inválido para quantidade para estoque máximo ou mínimo")


else:
    if qtd_estoque_atual >= qtd_estoque_media:
        print(f"O produto em estoque deve ter em média {qtd_estoque_media} em estoque.\nNão efetue a compra pois há {qtd_estoque_atual} produtos no estoque.")

    else:
        print(f"O produto em estoque deve ter em média {qtd_estoque_media} em estoque.\nEfetue a compra pois há {qtd_estoque_atual} produtos no estoque.")
