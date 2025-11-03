codigo_maior_preco = int(input("Digite o código do 1º produto: "))
maior_preco = float(input("Digite o preço do 1º produto: "))

media_preco_produtos = 0

for item in range(2, 16):
    codigo_produto = int(input(f"Digite o código do {item}º produto: "))
    preco_produto = float(input(f"Digite o preço do {item}º produto: "))

    if preco_produto > maior_preco:
        maior_preco = preco_produto
        codigo_maior_preco = codigo_produto

    media_preco_produtos += preco_produto

media_preco_produtos = media_preco_produtos/ 15

print(f"O produto de mais alto valor foi o produto de código {codigo_maior_preco}, custando R${maior_preco:.2f}")
print(f"A média de preço dos produtos é de: R${media_preco_produtos:.2f}")