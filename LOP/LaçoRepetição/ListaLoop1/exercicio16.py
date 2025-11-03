valor_total_estoque = 0
num_mercadorias = 0

resposta = 'S'

while resposta.upper() in ['S', 'SIM', 'SS']:
    valor_item = float(input(f"Digite o valor o da mercadoria: "))
    valor_total_estoque += valor_item
    num_mercadorias += 1

    resposta = input("Mais mercadorias? (S/N): ")

media_total = valor_total_estoque / num_mercadorias

print(f"Valor total das mercadorias: R${valor_total_estoque:.2f}")
print(f"Média total das mercadorias: R${media_total:.2f}")