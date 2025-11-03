nums_negativos = 0

for _ in range(10):
    num_digitado = float(input("Digite um número: "))

    if num_digitado < 0:
        nums_negativos += 1

print(f"A quantidade de números negativos digitados foram: {nums_negativos}")