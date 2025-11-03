num_mercadorias = int(input("Digite a quantidade de mercadorias disponíveis em seu estoque: "))

valor_total_estoque = 0

for item in range(1, num_mercadorias + 1):
    valor_item = float(input(f"Digite o valor o da mercadoria {item}: "))

    valor_total_estoque += valor_item

media_total = valor_total_estoque / num_mercadorias

print(f"Valor total das mercadorias: R${valor_total_estoque:.2f}")
print(f"Média total das mercadorias: R${media_total:.2f}")