media = 0

tamanho = 10


for n in range(tamanho):
    num = float(input("Digite um número: "))

    media += num

media = media/tamanho

print(f'Média: {media:.2f}')